import stores
import models

member_store = stores.MemberStore()

member1 = models.Member("Mohammed", 20)
member2 = models.Member("Mohammed", 22)
member3 = models.Member("Abdo", 25)

members = member1, member2, member3

for member in members:
    member_store.add(member)

post_store = stores.PostsStore()

post1 = models.Post("Agriculture", "Agriculture is amazing", member1.id)
post2 = models.Post("Engineering", "I love engineering", member1.id)

post3 = models.Post("Medicine", "Medicine is great", member2.id)
post4 = models.Post("Architecture", "Spectacular art", member2.id)
post5 = models.Post("Astronomy", "Space is awesome", member2.id)

post6 = models.Post("Geology", "Earth is our friend", member3.id)
post7 = models.Post("ComputerSci", "Our passion", member3.id)
post8 = models.Post("Algorithms", "Yeah, more of that", member3.id)
post9 = models.Post("Operating Systems", "Ewww", member3.id)

posts = post1, post2, post3, post4, post5, post6, post7, post8, post9

for post in posts:
    post_store.add(post)


