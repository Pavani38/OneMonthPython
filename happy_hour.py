import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Anu"]

random_bar = random.choice(bars)
random_person_1 = random.choice(people)
random_person_2 = random.choice(people)

if random_person_1 == random_person_2:
        random_person_2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person_1} and {random_person_2}")
