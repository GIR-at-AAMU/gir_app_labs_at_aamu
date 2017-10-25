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


class Place(ndb.Model):
	"""Stores location of event.
	
	For example: a location of event that a group voted on.
	
	Properties:
		physical_location: Where group decides to meet.
		when_open: Hrs location is open, JSON-Encoded, like:
		  "{ # for each day of the week...
		  	 'Monday': [
		  	   ('09:00', '17:00'),  # open/close
		  	 ],
		  	 etc.
		  }"
		parking: Is parking available?
		outdoors: Outdoors or not?
		name: TBD		
	"""
		
	physical_location = ndb.GeoPtProperty()
	when_open = ndb.JsonProperty()
	outdoors = ndb.BooleanProperty()
