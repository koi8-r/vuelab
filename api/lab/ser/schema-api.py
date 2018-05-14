from schema import Schema, Optional, And, Use, SchemaError

schema = Schema({'id': And(Use(int), lambda n: 0 <= n <= 65535, error='id must be between 0..65535'),
                 'login': str,
                 Optional('groups'): [str]})


data = dict(id='1000', login='admin', groups=['wheel'])

validated = schema.validate(data)

print(validated)


class V(object):
    def __init__(self, e=False):
        self.e = e

    def validate(self, data):
        if self.e:
            raise SchemaError('Fuuuuuu')
        return data

Schema(str, 'Not a string').validate('1')
Schema(lambda x: x == 0).validate(0)
assert 5 == Schema(V(e=False)).validate(5)
Schema(lambda x: x == 0).validate(0)
Schema([1, int, 0]).validate([1, 0, 2, 9])
