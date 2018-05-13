import marshmallow as mm
import types


class UserSchema(mm.Schema):
    login = mm.fields.String(required=True)
    User = types.new_class('User', (object,))

    @mm.post_load
    def unpack(self, data):
        u = self.User()
        for a in self.declared_fields:
            setattr(u, a, data[a])
        return u


u = UserSchema().load(dict(id=0, login='root'))
# u.validate()
