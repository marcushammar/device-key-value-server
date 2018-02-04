#!/usr/bin/env python

import os
import urllib

from google.appengine.ext import ndb

import webapp2

class Value(ndb.Model):
    device = ndb.StringProperty()
    key = ndb.StringProperty()
    value = ndb.StringProperty()

class SetPage(webapp2.RequestHandler):

    def get(self):
        device = self.request.get('device','')
        key = self.request.get('key','')
        value = self.request.get('value','')

        if (value == ''):
            q = Value.query(Value.device == device, Value.key == key)

            if q.iter().has_next():
                self.response.write(q.iter().next().value)
            else:
                self.response.write('ERROR')

        else:
            value = Value()
            value.device = self.request.get('device')
            value.key = self.request.get('key')
            value.value = self.request.get('value')
            value.put()
            self.response.write('OK')

app = webapp2.WSGIApplication([
    ('/', SetPage),
], debug=True)
