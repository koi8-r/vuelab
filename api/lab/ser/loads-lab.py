from collections import namedtuple
from json import loads
from pprint import pprint as pp
from types import SimpleNamespace as Namespace


class dictns(dict):
    """dict with attribute access"""
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, val):
        self[key] = val


# json __type__ field - namedtuple value error

data_in = '''
{
  "id": 0,
  "login": "root",
  "groups": [
    {
      "id": 1000,
      "group": "admin"
    }
  ],
  "extra": 0
}
'''


class GTO(object):
    def __init__(self, data):
        self.__dict__ = data

    @classmethod
    def loads(cls, id, group, **kwargs):
        to = object.__new__(cls)
        to.id = id
        to.group = group
        return to


class int_required(int):
    pass

class UTO(object):
    x:int_required = 0
    y:str
    g:object.__new__(GTO).__class__

    def __init__(self, data):
        # self.__dict__ = data  # self.vars
        for k, v in data.items():
            setattr(self, k, v)
        self.x = 'XYZ'

    @classmethod
    def loads(cls, id, login, groups, **kwargs):
        to = object.__new__(cls)
        to.id, to.login, to.groups = id, login, [GTO.loads(**g) for g in groups]
        return to

    def __str__(self) -> str:
        return '{id}:{login}'.format(**self.__dict__)


pp(UTO.loads(**loads(data_in)).groups[0].__class__)

pp(loads(data_in, object_hook=lambda d: UTO(d)).groups[0].__class__)  # given UTO want a GTO
pp(loads(data_in, object_hook=lambda d: Namespace(**d)))
pp(loads(data_in, object_hook=lambda d: namedtuple('X', d.keys())(*d.values())))


pp(vars(UTO))
print(UTO({}).x)
print(UTO({}).__annotations__['x'].__base__.__name__)
