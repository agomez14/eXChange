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
#import webapp2
from operator import itemgetter
import facebook
from xhtml2pdf import pisa
import cStringIO as StringIO
import time
import cookielib
import jinja2
import os
import webapp2
#import logging
#import logging
#import jinja2
#import os
#import webapp2
from google.appengine.ext import webapp
# from twilio.rest import TwilioRestClient

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

 class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.delete_cookie('userid')
        
        template = jinja_environment.get_template('homepage.html')
        self.response.out.write(template.render(template_values))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
class signUphandler(webapp2.RequestHandler):
  def get(self):
args = dict(client_id=FACEBOOK_APP_ID, redirect_uri=self.request.path_url)
args["client_secret"] = FACEBOOK_APP_SECRET  #facebook APP Secret
args["code"] = self.request.get("code")
response = cgi.parse_qs(urllib.urlopen(
    urllib.urlencode(args)).read())
access_token = response["access_token"][-1]
rofile = json.load(urllib.urlopen(
    "https://graph.facebook.com/me?" +
    urllib.urlencode(dict(access_token=access_token))))
"""in above step, profile object gets basic profile information about the
facebook user.
In the step below, User Model Class is initialized with profile information
and saved in db.
"""
 friends = graph.get_connections('me', 'friends')  
 count = 5
 crushes = []
 crush = raw_input()
  for friend in friends :
   if crush == str(friend['name']):
    crushes.append(crush)
    count = count + 1;
    if count > 5
      break 
user = User(key_name=str(profile["id"]), id=str(profile["id"]),
            name=profile["name"], access_token=access_token,
            profile_url=profile["link"], crushes=crushes)
user.put()
self.redirect('/homepage')
class crushesHandler(webapp2.RequestHandler)
 crushes = User(crushes=crushes)
 for crush in crushes
  likes = { crush['name'] : g.get_connections(crush['id'], "likes")['data']   
  interests = { crush['name'] : g.get_connections(crush['id'], "interests")['data'] 
  relationshipstatus = { crush['name'] : g.get_connections(crush['id'], "relationshipstatus")['data'] 
   relationshipstatus = { crush['name'] : g.get_connections(crush['id'], "status")['data'] 
  rebound = Crushes(Crushes_id = crush['id'],Name= crush['name'],likes = like,interests = interest,relationshipstatus = relationshipstatus,status = status)
   #template_values = {'education':edus, 'user':user, }
    #template = jinja_environment.get_template('education.html')
    #self.response.out.write(template.render(template_values))
   self.redirect('/homepage')  
   # user = facebook.get_user_from_cookie(self.request.cookies, key, secret)
    #access_token = 'CAAKDh2VA4l8BAKJxB5IRzI4OhDInZCXsqb1Xqs8dbIXZCprgTKcHGbtfkYmz8B4MNIZAKKUTvZCIRCv3jW894T5ZAHBxe5YrorNQGV6uvGVrOsqeoDql7GdPSl8u5H011hlw7WZCpdiPY86k2J6IWFjkZAVopZAxcd01HP0LKfNV5MJBaeGXyCAS2RFHYvKEBqpQQZCmI68Tt7wWGnVDKMENIC9kQtSaoZA74ZD'
    #if user =
    #graph = facebook.GraphAPI(user[access_token])
    #profile = graph.get_object("me")
    #friends = graph.get_connections('me', 'friends')  
    #likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']   
    #interests = { friend['name'] : g.get_connections(friend['id'], "interests")['data'] 
    #relationshipstatus = { friend['name'] : g.get_connections(friend['id'], "interests")['data'] 
class HomePageHandler(webapp2.RequestHandler):
def get(self):
user = User(key_name=str(profile["id"]), id=str(profile["id"]),
            name=profile["name"], access_token=access_token,
            profile_url=profile["link"], crushes=crushes)
crushes = Crushes(Crushes_id = crush['id'],Name= crush['name'],likes = like,interests = interest,relationshipstatus = relationshipstatus,status = status)
template_values = {'crushes': crushes, 'user':user}
template = jinja_environment.get_template('homepage.html')
self.response.out.write(template.render(template_values))

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
