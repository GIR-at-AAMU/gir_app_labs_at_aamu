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
from pages import author_list


class Page(base.Page):
    """The base of author pages in the GiR App Labs @ AAMU app."""

    USER_NAME = 'author'
    DISPLAY_NAME = ''
    MESSAGE = 'BASE AUTHOR PAGE'

    TEMPLATE_FILE = 'author.html'
    TEMPLATES_DIR = 'authors/'

    @classmethod
    def user_path(cls, user_name):
	return author_list.Page.user_path(user_name)

    @classmethod
    def url_path(cls):
        return cls.user_path(cls.USER_NAME)

    @classmethod
    def template_file(cls):
        return cls.TEMPLATES_DIR + cls.USER_NAME + '.html'

    def template_values(self):
        values = super(Page, self).template_values()
        values.update({
          'message': self.MESSAGE,
          'author': {
            'id': self.USER_NAME,
            'name': self.DISPLAY_NAME,
          },
        })
        return values


