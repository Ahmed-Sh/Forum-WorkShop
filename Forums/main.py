import models

ahmed = models.Members("Ahmed", 42)
keem = models.Members("Kareem", 30)
omar = models.Members("Omar", 15)

ahmed.get_member_data()
#Ahmed.set_member_data()

post_1 = models.Posts("Python", "Python is a nice language to learn.")
post_2 = models.Posts("Math", "Math is always fun :)")
post_3 = models.Posts("Happiness", "Hope to achieve it in the afterlife.")


post_1.get_contents()
#post1.set_contents()
