from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name
    

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        User.__init__(self, name)

    def get_role(self):
        return 'Admin'
    
    def has_permission(self, permission):
        return True

class RegularUser(User):
    def __init__(self, name, allowed_permissions=None):
        User.__init__(self, name)
        self.allowed_permissions = allowed_permissions or ['read']
        
    def get_role(self):
        return 'Regular User'
    
    def has_permission(self, permission):
        return permission in self.allowed_permissions
    

user1 = AdminUser('Carlos')
user2 = RegularUser('Pedro')


print(f'User 1 Name:{user1.name}')
print(f'Role: {user1.get_role()}')


print(f'\nUser 2 Name:{user2.name}')
print(f'Role: {user2.get_role()}')


print(user1.has_permission('delete'))
print(user2.has_permission('delete'))