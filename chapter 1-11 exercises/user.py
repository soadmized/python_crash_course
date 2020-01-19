class User():

    def __init__(self, first: str, last: str, id: int = 0, username: str = 'None'):
        self.first = first
        self.last = last
        self.id = id
        self.username = username
        self.login_attempts = 0


    def describe_user(self):
        user_info = "\nInformation about user:\n"
        user_info += "Name - {0} {1}\n".format(self.first.title(), self.last.title())
        user_info += "ID - {}, username - {}\n".format(self.id, self.username)
        print(user_info)
        return 0


    def greet_user(self):
        print("Hello, {0} {1}!!".format(self.first, self.last))


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


class Privilegies():

    def __init__(self, privs):
        self.privs = privs

    def show_privilegies(self):
        print("Admin has these privilegies: \n")
        for item in self.privs:
            print(item + "\n")


class Admin(User):

    def __init__(self, first, last, id, username, priv_list: list):
        self.priv_list = priv_list
        self.privs = Privilegies(priv_list)
        super().__init__(first, last, id, username)
