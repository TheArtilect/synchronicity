
import webapp2

from Handler import Handler
from NewPostPage import NewPost
from PostPage import PostPage
from SignUpPage import SignUpPage
from WelcomePage import WelcomePage

import Post
import User

from google.appengine.ext import db


class FrontPage(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * From Post ORDER BY created DESC LIMIT 10")
        self.render("frontpage.html", posts = posts)



app = webapp2.WSGIApplication([ ("/", FrontPage),
                                ("/newpost", NewPost),
                                ('/([0-9]+)', PostPage),
                                ("/signup", SignUpPage),
                                ("/welcome", WelcomePage)
                                ],
                                debug=True)
