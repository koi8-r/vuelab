import types


class String(str):
    @property
    def raw_type(self):
        return self.__class__.__base__


def dumper(cls):
    print(vars(cls))
    U = types.new_class(cls.__model_name__, (object,))
    U.login = cls.__annotations__['login'].raw_type
    return U


class User(object):
    __model_name__ = 'User'
    __include__ = ['all']

    def __init__(self):
        pass

    login: String()



u = dumper(User)
print(u.login)


