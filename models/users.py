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

#Import the "new"AppEngine Database module. (ndb means new data base)
from google.appengine.ext import ndb

class User(ndb.Model):
    """Details about a user of the app
    
    Properties:
    	user_id: the ID of the identified Google Account.
    	  (UserProperty is not used because, the user's email address 
    	  could change.)
    	  https://cloud.google.com/appengine/docs/standard/python/users/userobjects
    	name: first name, last name
    	major: major of the student
    	classification: student classification
    	emails: user email
    	birth date : user birthday
    	hidden: hide user from public list
	"""

    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    major = ndb.StringProperty()
    classification = ndb.StringProperty()
    hidden = ndb.BooleanProperty()
    email = ndb.StringProperty()
    birth_date = ndb.DateProperty()