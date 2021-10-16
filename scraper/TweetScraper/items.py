import json
from typing import Any

from scrapy import Item, Field


class ItemJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if 'to_json' in dir(o):
            return o.to_json()
        return json.JSONEncoder.default(self, o)


class Tweet(Item):
    id_ = Field()
    raw_data = Field()
    query = Field()
    query_time = Field()

    def to_json(self):
        return dict(self['raw_data'])


class User(Item):
    id_ = Field()
    raw_data = Field()

    def to_json(self):
        return dict(self['raw_data'])
