
import jinja2
import webapp2
import json
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from google.appengine.api import users


jinja_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

def get_key(me):
    return ndb.Key("Visitor", me.user_id())

def get_visitor():
    me = users.get_current_user()
    if not me:
        return None
    my_key = get_key(me)
    return my_key.get()

class Visitor(ndb.Model):
    id = ndb.StringProperty(required=False)
    fullname = ndb.StringProperty(required=False)
    givenname = ndb.StringProperty(required=False)
    imageurl = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)

class InfoPage(webapp2.RequestHandler):
    def get(self):
       user = users.get_current_user()
       if not user: #User is not signed in
           info = jinja_env.get_template('templates/info.html')
           jinja_values = {
               'log_url': users.create_login_url('/')
               }
            self.response.write(info.render(jinja_values))
        else:
            my_visitor = get_visitor()
            if not my_visitor:
                my_visitor = Visitor(
                    id = user.user_id(),
                    name = user.nickname(),
                    email = user.email())

                    my_visitor.put()
            userhome = jinja_env.get_template('templates/home.html')

            jinja_values = {
                    'name': user.nickname(),
                    'email_addr': user.email(),
                    'user_id': user.user_id(),
                    'log_url': users.create_logout('/'),
            }

app = webapp2.WSGIApplication([
    ('/', InfoPage),
])
