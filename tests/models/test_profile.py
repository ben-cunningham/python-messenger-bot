import unittest, json

from fbmsgbot.models.profile import Profile

class TestProfile(unittest.TestCase):
   
    def test_constructor(self):
        
       profile = Profile(first_name='test_first',
	                  last_name='test_last',
			  profile_pic='test_pic',
			  locale='CANADA',
          		  timezone='PST',
			  gender='M')
	
	assert profile.first_name == 'test_first'
	assert profile.last_name == 'last_name'
	assert profile.gender == 'M' 
    
        

