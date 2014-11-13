import os
import string

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
		text = self.request.get('text')

		lowercase = string.ascii_lowercase
		uppercase = string.ascii_uppercase

		rot13_text = ""
		for char in text:
			if char.isalpha():
				if char.islower():
					index = lowercase.find(char)
					index = (index+13) % 26
					rot13_text += lowercase[index]
			else:
				rot13_text += char


			
		self.render('index.html', input_text=text, rot13_text=rot13_text)

app = webapp2.WSGIApplication([
							    ('/', MainPage),
								], debug=True)