import models
import store

ahmed = models.Members("Ahmed", 42)
keem = models.Members("Kareem", 30)
omar = models.Members("Omar", 15)

post_1 = models.Posts("Python", "Python is a nice language to learn.")
post_2 = models.Posts("Math", "Math is always fun :)")
post_3 = models.Posts("Happiness", "Hope to achieve it in the afterlife.")


print(omar)
member_store = store.MemberStore()
member_store.add(ahmed)
member_store.add(omar)
member_store.add(keem)
member_store.add(keem)
print("\n")
print(member_store.get_all())
print(member_store.get_by_id(3))
print(member_store.get_by_id(5))
print(omar)
print("\n")
# Ahmed.set_member_data()


print(post_1)
# post1.set_contents()

posts_store = store.PostsStore()
posts_store.add(post_1)
posts_store.add(post_2)
posts_store.add(post_3)
print("\n")
print(posts_store.get_all())
print(posts_store.get_by_id(2))
print(posts_store.get_by_id(5))
print("\n")
