from google.appengine.ext import ndb
import logging
class User(ndb.Model):
 class User(ndb.Model):
    id = db.StringProperty(required=True) #facebook user-id
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty(required=True)
    profile_url = ndb.StringProperty(required=True)
    access_token = ndb.StringProperty(required=True)
    crushes = ndb.PickleProperty(required=True) 
 class Crushes(ndb.Model)
     Crushes.id = ndb.KeyProperty(kind=User, require=True)
     likes = ndb.TextProperty()
     interests = ndb.TextProperty()
     relationshipsstatus = ndb.TextProperty()
     status = ndb.TextProperty()
     