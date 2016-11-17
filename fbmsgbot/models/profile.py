class Profile():
    
    def __init__(self, **kwargs):
        self.first_name = kwargs['first_name']
	self.last_name = kwargs['last_name']
	self.profile_pic = kwargs['profile_pic']
	self.locale = kwargs['locale']
	self.timezone = kwargs['timezone']
	self.gender = kwargs['gender']

