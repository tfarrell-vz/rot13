import os

import jinja2
import webapp2

# Construct the template directory path and assign it to `template_dir`
# __file__ refers to this file
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# Make a Handler class from which other Handlers can inherit. 
class Handler(webapp2.RequestHandler):
	def write(self, content):
		self.response.out.write(content)

	def render_as_string(self):
		return None

	def render(self):
		return None

class MainPage(Handler):
	def get(self):
		self.write("Hello, world!")

app = webapp2.WSGIApplication([
							    ('/', MainPage),
								], debug=True)