import random

flavors = ["Butterscotch",
        "Chocolate",
        "Strawberry",
        "Pineapple",
        "Vanilla"]

friends = ["Manasa",
          "Sahitya",
          "Priyanka",
          "Kavya",
          "Shirisha",]

random_flavors = random.choice(flavors)
random_friend = random.choice(friends)


print(f"{random_friend} likes {random_flavors} icecream.")