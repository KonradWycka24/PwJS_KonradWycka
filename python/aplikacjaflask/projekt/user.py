class User:
    def __init__(self,logi,haslo):
        self.logi = logi
        self.haslo = haslo

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.logi
