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
                self.error(404)
                self.response.write('ERROR (Device and/or Key missing)')

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
                self.error(404)
                self.response.write('ERROR (Device missing)')

app = webapp2.WSGIApplication([
    ('/', SetPage),
], debug=True)
