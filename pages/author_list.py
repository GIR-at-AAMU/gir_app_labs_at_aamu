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

from pages import base


class Page(base.Page):
    """List of authors of the GiR App Labs at AAMU app."""

    URL_PATH = '/a'
    TEMPLATE_FILE = 'author_list.html'

    _authors = {}

    @classmethod
    def user_path(cls, user_name):
	return cls.URL_PATH + '/' + user_name

    @classmethod
    def add_author(cls, user_name, handler):
	cls._authors[user_name] = {
          'id': user_name,
          'name': '',
          'url': cls.user_path(user_name),
        }
        base.Page.add_handler(cls.user_path(user_name), handler)

    @classmethod
    def add_author_page(cls, page):
	cls._authors[page.USER_NAME] = {
          'id': page.USER_NAME,
          'name': page.DISPLAY_NAME,
          'url': page.url_path(),
        }
        page.add_page()
 
    def template_values(self):
        author_ids = self._authors.keys()
        author_ids.sort()
	authors = [self._authors[aid] for aid in author_ids]

        values = super(Page, self).template_values()
        values.update({
          'num_authors': len(authors),
          'authors': authors,
        })
        return values


Page.add_page()

