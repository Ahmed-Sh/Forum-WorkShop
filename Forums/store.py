import itertools, copy

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
        return (member for member in self.get_all() if member.name == name)

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
        result = member
        all_members = self.get_all()

        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                break
        return result

    def delete(self, id):
        member =  self.get_by_id(id)
        MemberStore.members.remove(member)

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id is post.member_id:
                member.posts.append(post)

        for member in all_members :
            yield member

    def get_top_two(self, all_posts):
        members_with_posts = list(self.get_members_with_posts(all_posts))

        members_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

        yield members_with_posts[0]
        yield members_with_posts[1]

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



