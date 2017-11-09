# Copyright 2017 The GiR @ AAMU Authors. All rights reserved.
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

import os
import urllib

import jinja2
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb


BASE_PY_DIR_PATH = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(os.path.dirname(BASE_PY_DIR_PATH), 'templates')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Page(webapp2.RequestHandler):
    """The base Page class for the GiR App Labs @ AAMU app."""

    _registry = {}

    @classmethod
    def routes(cls):
        return [(url, handler) for url, handler in cls._registry.items()]

    @classmethod
    def add_page(cls):
        cls.add_handler(cls.url_path(), cls)

    @classmethod
    def add_handler(cls, url, handler):
        cls._registry[url] = handler
    
    @classmethod
    def user_path(cls, user_name):
	return '/u/' + user_name

    @classmethod
    def url_path(cls):
        return cls.URL_PATH

    def template_values(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            linktext = 'Logout'
            username = user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            linktext = 'Login'
            username = ''

        return {
            'user_url': url,
            'user_linktext': linktext,
            'user_name': username,
        }

    @classmethod
    def template_file(cls):
        return cls.TEMPLATE_FILE

    def render(self, template_path, template_values):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template(template_path)
        self.response.write(template.render(template_values))

    def get(self):
        """HTTP GET handler for simple App Labs app pagss."""

        self.render(self.template_file(), self.template_values())

