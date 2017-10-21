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

import author_pages

class AuthorPage(webapp2.RequestHandler):
    """The cbradfo6 author page of the GiR App Labs at AAMU app."""

    def get(self):
        """HTTP GET handler for the tlarsen Users page."""

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("What's up, It's Court!")


author_pages.add_page('cbradfo6', AuthorPage)
