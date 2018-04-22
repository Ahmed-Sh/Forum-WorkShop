import models
import store

def create_members():
    member1 = models.Members("Ahmed", 42)
    member2 = models.Members("Kareem", 30)
    member3 = models.Members("Omar", 15)
    member4 = models.Members("Yaser", 44)
    print(member1)
    print(member2)
    print(member3)
    print(member4)
    print("*"*30)
    return member1, member2, member3, member4

def store_should_add_models(members_instances, member_store):
    for member in members_instances:
        member_store.add(member)

def stores_should_be_similar():
    member_store1 = store.MemberStore()
    member_store2 = store.MemberStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")

def print_all_members(member_store):
    print("=" * 30)
    for member in member_store.get_all():
        print(member)
    print("=" * 30)

def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)
    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")
    print("=" * 30)

def update_should_modify_object(member_store, member4):
    member4_copy = models.Members(member4.name, member4.age)
    member4_copy.id = 4
    if member4_copy is not member4:
        print("member4 and member4_copy are not the same !")
    print(member4_copy)
    member4_copy.name = "john"
    member_store.update(member4_copy)
    print(member_store.get_by_id(member4.id))
    print("=" * 30)

def catch_exception_when_deleting():
    try:
        member_store.delete(10)
    except ValueError:
        print("It should be an existence entity before deleting !")

members_instances = create_members()
member1, member2, member3, member4 = members_instances

member_store = store.MemberStore()

store_should_add_models(members_instances, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member4)

catch_exception_when_deleting()

print_all_members(member_store)

post_1 = models.Posts("Python", "Python is a nice language to learn.")
post_2 = models.Posts("Math", "Math is always fun :)")
post_3 = models.Posts("Happiness", "Hope to achieve it in the afterlife.")

'''
try:
    print(member_store.entity_exists(ali))
except NameError:
    print("This is not a used Name !!!!")

print(post_1)
posts_store = store.PostsStore()
posts_store.add(post_1)
posts_store.add(post_2)
posts_store.add(post_3)
print("\n")
print(posts_store.get_by_id(2))
print(posts_store.get_by_id(5))
print(posts_store.entity_exists(post_2))
print("\n")'''
