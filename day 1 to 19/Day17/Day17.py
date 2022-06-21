# example of defining class
class User:
    def __init__(self, user_id, username):  # if u use init then the variables need to be inputted
        self.id = user_id
        self.username = username
        self.followers = 0  # set default value
        self.following = 0

    def follow(self, user):  # a method always needs to have a self parameter.
        user.followers += 1
        self.following += 1


user1 = User("001", "BadEnforcer")
user2 = User("002", "Raj")
user1.follow(user2)
print(user2.followers)
print(user1.following)
