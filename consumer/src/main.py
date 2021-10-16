import logging
import os
import signal
import socket
from threading import Thread, Event
from time import sleep

import redis

logging.basicConfig(level=logging.INFO)


class Consumer(Thread):
    def __init__(self, topic: str, stop_event: Event):
        super(Consumer, self).__init__(daemon=True)
        self.topic = topic
        self.stop_event = stop_event

    def run(self):
        logger = logging.getLogger(self.topic)

        logger.info(f'consuming topic {self.topic}')

        redis_host = os.environ.get('REDIS_HOST', 'redis')
        try:
            client = redis.StrictRedis(host=redis_host, decode_responses=True)
            client.info()
        except (redis.exceptions.ConnectionError, socket.gaierror) as ex:
            logger.error(ex)
            self.stop_event.set()
            return

        # max_wait_time = timedelta(seconds=60)
        # last_data = datetime.now()
        while not self.stop_event.wait(0):  # and datetime.now() - last_data < max_wait_time:
            data = client.lpop(self.topic)
            if data is not None:
                logger.info(f'fetched data: {data}')
                # last_data = datetime.now()
            sleep(0.1)

        logger.info(f'done')


def main():
    logger = logging.getLogger('main')
    logger.info('startup')
    topics = (
        'users',
        'tweets',
    )

    stop_event = Event()

    def handle_sigterm(*_):
        logging.getLogger().info('caught SIGTERM')
        stop_event.set()

    signal.signal(signal.SIGTERM, handle_sigterm)
    signal.signal(signal.SIGINT, handle_sigterm)

    threads = tuple(
        Consumer(topic, stop_event) for topic in topics
    )

    logger.info('running threads')

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    logger.info('done')


if __name__ == '__main__':
    main()
