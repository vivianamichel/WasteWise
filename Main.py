userData = {}
userPassword = {}
class User:
    def __init__(self, name, email, password, d, pdict):
        self.name = name
        self.email = email
        self.score = 0
        self.password = password
        self.data = d
        self.passwords = pdict
        self.data.update({name: self.score})
        self.passwords.update({email: password})

    def add_score(self, score):
        self.score += score
        self.data[self.name] = self.score

def login(self, email, password):
    if email in userPassword:
        if self.passwords[self.email] == password:
            print("youre in")
        else:
            print("incorrect password")
    else:
        print("Email not associated with user")
def scoreboard(dict):
        for name in sorted(dict, key = dict.get, reverse=True):
            print(name, dict[name])

viviana = User("viviana", "@@@", "123", userData, userPassword)
print(userPassword)
login(viviana, "@@@", "12")
