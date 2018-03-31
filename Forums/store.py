class MemberStore:
    members = []

    def add(self, member):
        self.members.append(member)

    def get_all(self):
        return MemberStore.members


class PostsStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return PostsStore.posts





