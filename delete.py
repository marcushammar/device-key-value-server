#!/usr/bin/env python

import os
import urllib

from google.appengine.ext import ndb

import webapp2

class Value(ndb.Model):
    device_id = ndb.StringProperty()
    device_key = ndb.StringProperty()
    device_value = ndb.StringProperty()

class Device(ndb.Model):
    device_id = ndb.StringProperty()

class Delete(webapp2.RequestHandler):

    def get(self):
        device_id = self.request.get('device','')

        q = Value.query(Value.device_id == device_id)
        for p in q:
            p.key.delete()

        q = Device.query(Device.device_id == device_id)
        for p in q:
            p.key.delete()

        self.response.write('OK')

app = webapp2.WSGIApplication([
    ('/delete/', Delete),
], debug=True)
