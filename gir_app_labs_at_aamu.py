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

from authors import aeagle
from authors import amason6
from authors import amcgee3
from authors import aoa0006
from authors import asessom
from authors import cbradfo6
from authors import dwilso57
from authors import egardner2
from authors import jander37
from authors import jbeatty
from authors import jlindber
from authors import jmedina
from authors import jnoland
from authors import klule
from authors import lsteele3
from authors import mhughe
from authors import mmaneice
from authors import nmai
from authors import pparrick
from authors import smartine
from authors import tlarsen
from authors import tthomp37
from authors import ualexan1

from authors import author_pages

class HomePage(webapp2.RequestHandler):
    """The / home page of the "Hello, world!" app."""

    def get(self):
        """HTTP GET handler for the "Hello, world!" app."""

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


routes = [('/', HomePage),]
routes.extend(author_pages.routes())

app = webapp2.WSGIApplication(routes, debug=True)
