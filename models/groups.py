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

# Import the "new" AppEngine Database module.
from google.appengine.ext import ndb

class Group(ndb.Model):
    """A group of Users.
    
    Properties:
      owner_ids: The User IDs of the group owners
      member_ids: The User IDs of the group members
      exclusivity: How exclusive is the group?
        'exclusive') private invitation is required
        'invite-only') general invitation is required
        'open') no invitation is required
    """

    EXCLUSIVITIES = ('exclusive', 'invite-only', 'open')

    owner_ids = ndb.StringProperty(repeated=True)
    member_ids = ndb.StringProperty(repeated=True)
    exclusivity = ndb.StringProperty()

