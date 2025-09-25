class User:
    def __init__(self, id, username, password, fullname = None, email = None):
        self.id = id if id else None
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        
    def to_dict(self):
        return {
            'id': str(self.id) if self.id else None,
            'username': self.username,
            'fullname': self.fullname,
            'email': self.email
        }