# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
import os

USER_AGENT = 'TweetScraper'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.RedisPipeline': 100,
}

# settings for where to save data on disk
# SAVE_TWEET_PATH = './Data/tweet/'
# SAVE_USER_PATH = './Data/user/'

EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 1000
}

DOWNLOAD_DELAY = 1.0

# settings for selenium
SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_BROWSER_EXECUTABLE_PATH = '/home/user/.local/firefox/firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = '/home/user/.local/bin/geckodriver'
SELENIUM_DRIVER_ARGUMENTS = ['-headless']  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

CLOSESPIDER_ITEMCOUNT = int(os.environ.get('CRAWLER_MAX_ITEMS', 0))
CLOSESPIDER_ERRORCOUNT = int(os.environ.get('CRAWLER_MAX_ERRORS', 1))
