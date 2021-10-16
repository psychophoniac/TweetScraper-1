import json
import logging
import os
from typing import Union

import redis
from scrapy import Spider
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User, ItemJsonEncoder

logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()


class RedisPipeline:
    """
    pushes items into redis message broker
    """

    def __init__(self):
        redis_host = os.environ.get('REDIS_HOST', 'redis')
        self.redis_client = redis.StrictRedis(
            host=redis_host,
            decode_responses=True
        )

    def process_item(self, item: Union[Tweet, User], spider: Spider):
        if isinstance(item, Tweet):
            #logger.debug(f'found tweet: {item["id_"]}')
            self.redis_client.lpush('tweets', json.dumps(item, cls=ItemJsonEncoder))

        elif isinstance(item, User):
            #logger.debug(f'found user: {item["id"]}')
            self.redis_client.lpush('users', json.dumps(item, cls=ItemJsonEncoder))
        else:
            logger.warning(f'unknown item type: {type(item)}')
