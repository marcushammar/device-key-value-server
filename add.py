#!/usr/bin/env python

import os
import urllib

from google.appengine.ext import ndb

import webapp2

class Device(ndb.Model):
    device_id = ndb.StringProperty()

class Add(webapp2.RequestHandler):

    def get(self):
        device = Device()
        device.device_id = self.request.get('device')
        device.put()
        self.response.write('OK')

app = webapp2.WSGIApplication([
    ('/add/', Add),
], debug=True)
