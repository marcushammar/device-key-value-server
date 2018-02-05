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
    device_timestamp = ndb.DateTimeProperty(auto_now=True)

class Delete(webapp2.RequestHandler):

    def get(self):
        device_id = self.request.get('device','')

        if (device_id == ''):
            self.error(404)
            self.response.write('ERROR (Device should not be empty)')
            return

        q = Value.query(Value.device_id == device_id)
        for p in q:
            p.key.delete()

        q = Device.query(Device.device_id == device_id)
        for p in q:
            p.key.delete()

        self.response.write('OK')

class Add(webapp2.RequestHandler):

    def get(self):
        device_id = self.request.get('device','')

        if (device_id == ''):
            self.error(404)
            self.response.write('ERROR (Device should not be empty)')
            return

        q = Device.query(Device.device_id == device_id)
        for p in q:
            p.key.delete()

        device = Device()
        device.device_id = device_id
        device.put()
        self.response.write('OK')

class SetOrGet(webapp2.RequestHandler):

    def get(self):
        device_id = self.request.get('device','')
        device_key = self.request.get('key','')
        device_value = self.request.get('value','')

        q = Device.query(Device.device_id == device_id)
        if q.count() != 1:
            self.error(404)
            self.response.write('ERROR (Device not found)')
            return

        if (device_key == ''):
            self.error(404)
            self.response.write('ERROR (Key should not be empty)')
            return

        if (device_value == ''):
            q = Value.query(Value.device_id == device_id, Value.device_key == device_key)

            if q.iter().has_next():
                self.response.write(q.iter().next().device_value)
            else:
                self.error(404)
                self.response.write('ERROR (Key not found)')

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
    ('/', SetOrGet),
    ('/add/', Add),
    ('/delete/', Delete),
], debug=True)
