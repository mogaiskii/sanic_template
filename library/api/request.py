from collections import namedtuple

from marshmallow import Schema


class RequestSchema(Schema):
    def get_object(self, data):
        load_data = self.load(data)

        obj = namedtuple(type(self).__name__, list(load_data.keys()))
        for k,v in load_data.items():
            setattr(obj, k, v)

        return obj
