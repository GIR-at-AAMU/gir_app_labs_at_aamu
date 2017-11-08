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

import webapp2

class AuthorsListPage(webapp2.RequestHandler):
    """List of authors of the GiR App Labs at AAMU app."""

    def get(self):
        """HTTP GET handler for the authors list page."""
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<html>\n <head>\n")
        self.response.write("  <title>Author List</title>\n")
        self.response.write(" </head>\n <body>\n")
        
        user_names = _registry.keys()
        user_names.sort()
        for user_name in user_names:
            self.response.write('<a href="/a/{}">{}</a><br>\n'.format(user_name, user_name))
        
        self.response.write(" </body>\n</html>\n")


_registry = {}


def routes():
    return [('/a', AuthorsListPage),] + [
            ('/a/' + user_name, handler)
            for user_name, handler in _registry.iteritems()]


def add_page(user_name, handler):
	_registry[user_name] = handler
