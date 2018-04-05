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


    def get_by_id(self,id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result


class PostsStore:
    posts = []
    last_id = 1

    def add(self, post):
        PostsStore.posts.append(post)
        post.id = PostsStore.last_id
        PostsStore.last_id += 1

    def get_all(self):
        return PostsStore.posts

    def get_by_id(self,id):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result
