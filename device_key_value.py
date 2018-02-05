#!/usr/bin/env python

import os
import urllib

from google.appengine.ext import ndb

import webapp2

class Device(ndb.Model):
    device_id = ndb.StringProperty()

class Value(ndb.Model):
    device_id = ndb.StringProperty()
    device_key = ndb.StringProperty()
    device_value = ndb.StringProperty()

class SetPage(webapp2.RequestHandler):

    def get(self):
        device_id = self.request.get('device','')
        device_key = self.request.get('key','')
        device_value = self.request.get('value','')

        if (device_value == ''):
            q = Value.query(Value.device_id == device_id, Value.device_key == device_key)

            if q.iter().has_next():
                self.response.write(q.iter().next().device_value)
            else:
                self.response.write('ERROR')

        else:
            q = Device.query(Device.device_id == device_id)

            if q.count() != 0:

                q = Value.query(Value.device_id == device_id, Value.device_key == device_key)

                for p in q:
                    p.key.delete()

                value = Value()
                value.device_id = self.request.get('device')
                value.device_key = self.request.get('key')
                value.device_value = self.request.get('value')
                value.put()
                self.response.write('OK')
            else:
                self.response.write('ERROR')

app = webapp2.WSGIApplication([
    ('/', SetPage),
], debug=True)
