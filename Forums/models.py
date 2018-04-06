class Members():
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age
        self.id = 0

    def set_member_data(self, name = None, age = None):
        a = "Please write your Name: "
        self.name = input(a)
        b = "Please write your Age: "
        self.age = input(b)
        print ("Name: {0} \nAge: {1}".format(self.name, self.age))

    def __str__(self):
        return ("Member name: {0} \nMember age: {1} \nMember Id: {2}".format(self.name, self.age, self.id))

class Posts():
    def __init__(self, title = None, content = None):
        self.title = title
        self.content = content
        self.id = 0

    def set_contents(self, title = None, content = None):
        a = "Please write your post title: "
        self.title = input(a)
        b = "Please write your post: "
        self.content = input(b)
        print ("Post Title: {0} \nContents: {1}".format(self.title, self.content))

    def __str__(self):
        return ("Post Title: {0} \nContents: {1}".format(self.title, self.content))
