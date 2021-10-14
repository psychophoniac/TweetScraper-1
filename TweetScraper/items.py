from scrapy import Item, Field


class Tweet(Item):
    id_ = Field()
    raw_data = Field()
    query = Field()
    query_time = Field()

class User(Item):
    id_ = Field()
    raw_data = Field()
