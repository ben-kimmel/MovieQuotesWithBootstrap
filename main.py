import os

import jinja2
import webapp2
from models import MovieQuote
from google.appengine.ext import ndb

# Jinja environment instance necessary to use Jinja templates.
def __init_jinja_env():
    jenv = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=["jinja2.ext.do", "jinja2.ext.loopcontrols", "jinja2.ext.with_"],
        autoescape=True)
    # Example of a Jinja filter (useful for formatting data sometimes)
    #   jenv.filters["time_and_date_format"] = date_utils.time_and_date_format
    return jenv

jinja_env = __init_jinja_env()

PARENT_KEY = ndb.Key("Entity", 'moviequote_root')


class MovieQuotesPage(webapp2.RequestHandler):
    def get(self):        
        mqq = MovieQuote.query(ancestor=PARENT_KEY).order(-MovieQuote.last_touch_date_time)
        template = jinja_env.get_template("templates/moviequotes.html")
        self.response.out.write(template.render({"moviequotes_query":mqq}))

class AddQuoteAction(webapp2.RequestHandler):
    def post(self): 
        if self.request.get("entity_key"):
            mq_key = ndb.Key(urlsafe=self.request.get('entity_key'))
            mq = mq_key.get()
            mq.quote = self.request.get("quote")
            mq.movie = self.request.get("movie")
            mq.put()
        else:       
            new_quote = MovieQuote(parent=PARENT_KEY, quote=self.request.get('quote'), movie=self.request.get('movie'))
            new_quote.put()
        self.redirect(self.request.referer)
        
class DeleteQuoteAction(webapp2.RequestHandler):
    def post(self):
        moviequote_key = ndb.Key(urlsafe=self.request.get('entity_key'))
        moviequote_key.delete()
        self.redirect(self.request.referer)

app = webapp2.WSGIApplication([
    ('/', MovieQuotesPage),
    ('/addquote', AddQuoteAction),
    ('/deletequote', DeleteQuoteAction)
], debug=True)
