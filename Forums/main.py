import models
import store

ahmed = models.Members("Ahmed", 42)
keem = models.Members("Kareem", 30)
omar = models.Members("Omar", 15)

print(ahmed)
# Ahmed.set_member_data()

post_1 = models.Posts("Python", "Python is a nice language to learn.")
post_2 = models.Posts("Math", "Math is always fun :)")
post_3 = models.Posts("Happiness", "Hope to achieve it in the afterlife.")

print(post_1)
# post1.set_contents()

member_store = store.MemberStore()
member_store.add("ahmed")
member_store.add("omar")
member_store.add("keem")
# print(member_store.get_all())
posts_store = store.PostsStore()
posts_store.add("post_1")
posts_store.add("post_2")
posts_store.add("post_3")
# print(posts_store.get_all())
