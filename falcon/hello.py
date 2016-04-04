import falcon
import json

class Index:
    def on_get(self, req, resp):
        msg = {
            "messages": "hello, world"
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(msg)

application = falcon.API()
application.add_route('/', Index())
