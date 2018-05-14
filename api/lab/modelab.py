import types
import json
from schema import Schema, And, Use, Or, Optional
from pprint import pprint as pp
from aiohttp import web
from aiohttp.web import Request, Response, HTTPRequestEntityTooLarge
from aiohttp.streams import StreamReader


def run(this):
    web.run_app(this)


def consume():
    def decorator(fn):
        def wrap(req: Request):
            return fn(req)
        return wrap
    return decorator


def route(this, verb='GET', path='/'):
    def decorator(fn):
        this.router.add_route(verb, path, fn)
        return fn
    return decorator


httpd = web.Application()
httpd.route = types.MethodType(route, httpd)
httpd.run = types.MethodType(run, httpd)
httpd.MAX_UPLOAD_SIZE = 1024  # 1024**2 = 1M


class namedict(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, val):
        self[key] = val


group_schema = Schema({
    'id': And(int, lambda n: 0 <= n <= 65535),
    'group': And(str, len)
})

user_schema = Schema({
    'id': And(int, lambda n: 0 <= n <= 65535),
    'login': And(str, len),
    'groups': And(Use(lambda i:
                      [i] if not isinstance(i, list)
                      else i),
                  [group_schema])
})

data = json.loads('''{
    "id": 65535,
    "login": "nobody",
    "groups": [{
        "id": 1000,
        "group": "wheel"
    }]
}''', object_hook=lambda d: namedict(**d))

print(json.dumps(data, indent=4))

user_schema.validate(data)



@httpd.route(path='/')
async def index(req: Request):
    assert req.__class__ is Request
    accept = req.headers.get('accept') or '*/*'
    return Response(status=200, text='index', content_type='text/plain')


@consume()
@httpd.route(verb='POST', path='/')
@consume()
async def io(req: Request):
    bytes_body = await req.read()
    encoding = req.charset or 'utf-8'
    ct = req.content_type
    print((bytes_body, encoding, ct,))


    # return Response(status=200, text=type(req.text()).__name__)
    return Response(status=200, text='OK')


httpd.run()
