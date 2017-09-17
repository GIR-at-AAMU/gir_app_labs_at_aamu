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

import webtest

import hello_world


def test_get():
    """Tests the HTTP GET handler of the hello_world HomePage."""

    test_app = webtest.TestApp(hello_world.app)
    response = test_app.get('/')

    assert response.status_int == 200
    assert response.body == 'Hello, World!'