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

from pages import base


class Page(base.Page):
    """The / home page of the GiR App Labs @ AAMU app."""

    def template_values(self):
        values = super(Page, self).template_values()
        values['message'] = 'Hello, World!'
        return values

    def get(self):
        """HTTP GET handler for the "Hello, world!" app."""

        self.render('index.html', self.template_values())


Page.add_page('/')

