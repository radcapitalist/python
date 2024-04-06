
class User:
    def __init__(self, id, username):
        self.id = id
        self._username = username
        self.followers = 0
        self.following = 0

    __slots__ = ['id', 'ssn', '_username', 'followers', 'following']

    def __repr__(self):
        return f"User('{self.id}', '{self.username}')"
    
    def __str__(self):
        return f"{self.username} ({self.id}), follower count: {self.followers}"
    
    @property
    def username(self):
        """ Gets the current username """
        return self._username
    
    @username.setter
    def username(self, value):
        """ Sets the username """
        self._username = value

    @username.deleter
    def del_username(self):
        """ Deletes the username """
        del self._username

    def ride(self):
        print(f"User {self.username} is riding")

    def follow(self, user):
        user.followers += 1
        self.following += 1
    

user_1 = User("001", "angela")
user_1.ssn = "150-43-6543"

print(user_1)
user_1.ride()

user_1.username = "cantankerous"
print(user_1)

user_1.username = "magnanimous"
print(user_1)

user_2 = User("002", "matilda")
user_2.follow(user_1)

user_3 = User("003", "diana")
user_3.follow(user_1)

print(user_1, user_2, user_3)

