from marshmallow import Schema


class ResponseSchema(Schema):

    def dump_from(self, **kwargs):
        return self.dump(kwargs)
