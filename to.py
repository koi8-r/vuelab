# -*- mode: python -*-
# vi: set ft=python :


# --- NamedTuple transfer object
# https://dbader.org/blog/records-structs-and-data-transfer-objects-in-python
# https://www.yeahhub.com/7-best-python-libraries-validating-data/
# collections.namedtuple (2.6+)
# typing import NamedTuple (3.6+) or construct like: Model(uid=int, login=str)


# ---
from typing import NamedTuple
from sys import getsizeof


class User(NamedTuple):
    # Validate annotated type or properties
    uid: int
    login: str
    @property
    def desc(self):
        return None


getsizeof(User(0, 'root'))



# ---
class Attr(dict):
    # Danger - check special attributes overwrite
    __getattr__ = dict.__getitem__
    # def __getattr__(self, key):
    #     self.__getitem__(key)



# ---
class Group(object):
    def __init__(self, id, group) -> None:
        self.uid = id
        self.group = group


class User(object):
    def __init__(self, id, login, groups) -> None:
        self.uid = id
        self.login = login
        self.groups = groups

    @classmethod
    def from_json(cls, d):
        print([k for k in d])
        #u = User()


s = '''
{
    "id": 0,
    "login": "root",
    "groups": [
        {"id": "65535", "group": "nobody"}
    ]
}
'''

import json
print(json.loads(s, object_hook=User.from_json))


# https://github.com/isagalaev/ijson/blob/master/ijson/backends/python.py
