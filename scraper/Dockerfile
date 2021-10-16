FROM python:3.7 as base

ENV DEBIAN_FRONTEND noninteractive

ENV GECKODRIVER_VER v0.29.0
ENV GECKODRIVER_URL https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz

ENV FIREFOX_VER 87.0
ENV FIREFOX_URL https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2

RUN \
    apt update && \
    apt upgrade -y && \
    apt install -y \
        libdbus-glib-1-2 \
        libgtk3.0-cil \
        libx11-xcb1 \
       && \
    useradd -m user

USER user
ENV PATH=${PATH}:/home/user/.local/bin::/home/user/.local/firefox

COPY requirements.txt /home/user/
RUN \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /home/user/requirements.txt && \
    curl -L ${FIREFOX_URL} | \
        tar -C /home/user/.local/ -jxf- && \
        chmod -R 755 /home/user/.local/firefox && \
    curl -L  ${GECKODRIVER_URL} | \
        tar -C /home/user/.local/bin/ -zxf-


FROM base as runtime
COPY scrapy.cfg requirements.txt /home/user/
COPY TweetScraper /home/user/TweetScraper

WORKDIR /home/user
CMD scrapy crawl TweetScraper
