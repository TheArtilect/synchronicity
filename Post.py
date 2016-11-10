
from google.appengine.ext import db

class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    creator = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    likes = db.StringListProperty()

    #   need to add the user that created it, likes, comments



    def rendered_content(self):
        return self.content.replace("\n", "<br>")


def blog_key(name = 'default'):
    return db.Key.from_path('/', name)
