import os
import json
import falcon
from db import Session
from models import LocationHistory

class Index:
    def on_get(self, req, resp):
        msg = {
            "messages": "hello, world"
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(msg)

class LocationHistoryResource:
    def on_get(self, req, resp):
        s = Session()
        location_histories = s.query(LocationHistory).all()
        arr = []
        for row in location_histories:
            hash = {}
            hash['id'] = row.id
            hash['latitude'] = row.latitude
            hash['lognitude'] = row.lognitude
            hash['created_at'] = str(row.created_at)
            arr.append(hash)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(arr, sort_keys=True, indent=4)

    def on_post(self, req, resp):
        s = Session()
        location_history = LocationHistory(latitude=0, lognitude=0)
        s.add(location_history)
        s.commit()
        msg = {
            "messages": "ok"
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(msg)
        print(location_history)

        
application = falcon.API()
application.add_route('/', Index())
application.add_route('/location_history', LocationHistoryResource())
