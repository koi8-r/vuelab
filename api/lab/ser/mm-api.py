from marshmallow import Schema, fields, marshalling


class GroupSchema(Schema):
    id = fields.Int()
    group = fields.Str()


class UserSchema(Schema):
    id = fields.Int()
    login = fields.Str(required=True)
    # groups = GroupSchema(many=True)


class User(object):
    def __init__(self, id, login) -> None:
        self.id = id
        self.login = login


us = UserSchema()


# Serialize, fixme: model.validate()
print(us.dumps(dict(id=1000, login='admin')))
print(us.dumps(User(1000, 'admin')))

# Deserialize
print(us.load(dict(id=65535, login='nobody')))

# UserSchema().validate()
