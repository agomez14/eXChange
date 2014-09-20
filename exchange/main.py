#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import jinja2
import os
import webapp2
from google.appengine.ext import webapp
# from twilio.rest import TwilioRestClient

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('homepage.html')
    self.response.out.write(template.render())


class ReferenceHandler(webapp2.RequestHandler):
  def get(self):
    template_values={}
    if users.get_current_user():
      template_values['current_user'] = users.get_current_user()
      template_values['logoutUrl'] = users.create_logout_url(dest_url = '/loginPage')
    template = jinja_environment.get_template('reference.html')
    self.response.out.write(template.render(template_values))


class SendSMS(webapp2.RequestHandler):
  def get(self):
    messages = Message.query().fetch()
    account_sid = "AC07891472f11bf7ef4e186c090b834529"
    auth_token  = "{{ auth_token }}"
    client = TwilioRestClient(account_sid, auth_token)
    # message = client.messages.create(body="Jenny please?! I love you <3",
      # to="        ",
      # from_="+1404620285029",
      # media_url="http://www.example.com/hearts.png")
    # print message.sid


app = webapp.WSGIApplication([
    ('/', MainHandler),
    ('/references', ReferenceHandler),
    ('/send_sms', SendSMS)    
]);
