class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
        member_list = MemberStore.members
        if member in member_list:
            print("Please Choose another Name")
        else:
            MemberStore.members.append(member)
            member.id = MemberStore.last_id
            MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_name(self, name):
        all_members = self.get_all()
        result = None
        for member in all_members:
            answer = []
            if member.name == name:
                answer.append(member)
                result = answer
        return result

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False
        return result

    def update(self, member):
        all_members = self.get_all()
        if member in all_members:
            member.name = input("Enter your Name: ")
            member.age = int(input("Enter Your Age: "))
        return member



    def delete(self, id):
        member =  self.get_by_id(id)
        MemberStore.members.remove(member)
        

class PostsStore:
    posts = []
    last_id = 1

    def add(self, post):
        PostsStore.posts.append(post)
        post.id = PostsStore.last_id
        PostsStore.last_id += 1

    def get_all(self):
        return PostsStore.posts

    def get_by_id(self, id):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result

    def entity_exists(self, post):
        result = True
        if self.get_by_id(post.id) is None:
            result = False
        return result

    def delete(self, id):
        if self.get_by_id(id):
            PostsStore.posts.remove(self.get_by_id(id))
        else:
            print("This Id doesn't exist !!!")
