from schematics.models import Model
from schematics.types import IntType, StringType
import json


class User(Model):
    id = IntType()
    login = StringType(required=True)


u = User(dict(id=1000, login='admin'))
print(json.dumps(u.to_primitive(), indent=4))
