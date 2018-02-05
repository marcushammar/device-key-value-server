#!/usr/bin/env python

"""
Copyright 2018 Marcus Hammar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
