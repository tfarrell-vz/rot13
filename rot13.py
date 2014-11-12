import os

import jinja2
import webapp2

# Construct the template directory path and assign it to `template_dir`
# __file__ refers to this file
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)

# Make a Handler class from which other Handlers can inherit. 
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_as_string(self, template, **kw):
		t = jinja_env.get_template(template)
		return t.render(kw)

	def render(self, template, **kw):
		self.write(self.render_as_string(template, **kw))

class MainPage(Handler):
	def get(self):
		self.render('index.html')

	def post(self):
		value = self.request.get('text')
		self.render('index.html', value=value)

app = webapp2.WSGIApplication([
							    ('/', MainPage),
								], debug=True)