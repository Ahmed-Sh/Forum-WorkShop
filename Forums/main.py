import models
import store

ahmed = models.Members("Ahmed", 42)
ahmed_2 = models.Members("Ahmed", 25)
keem = models.Members("Kareem", 30)
omar = models.Members("Omar", 15)
yaser = models.Members("Yaser", 44)

post_1 = models.Posts("Python", "Python is a nice language to learn.")
post_2 = models.Posts("Math", "Math is always fun :)")
post_3 = models.Posts("Happiness", "Hope to achieve it in the afterlife.")

member_store = store.MemberStore()
member_store.add(ahmed)
member_store.add(omar)
member_store.add(ahmed_2)
member_store.add(keem)
print(member_store.get_by_id(4))
print(member_store.get_by_name("Ahmed"))
member_store.update(keem)
print(member_store.get_by_id(4))
member_store.delete(4)
member_store.delete(10)
print("\n")
try:
    print(member_store.entity_exists(ali))
except NameError:
    print("This is not a used Name !!!!")
print("\n")
print(yaser)
# Ahmed.set_member_data()


print(post_1)
# post1.set_contents()

posts_store = store.PostsStore()
posts_store.add(post_1)
posts_store.add(post_2)
posts_store.add(post_3)
print("\n")
print(posts_store.get_by_id(2))
print(posts_store.get_by_id(5))
print(posts_store.entity_exists(post_2))
print("\n")
