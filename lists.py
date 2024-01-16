the_count = [1, 2, 3, 4, 6]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]

# this for-loop goes through a list
for number in the_count:
    print("this is count", number)

for stock in stocks:
    print("stock ticketer:", stocks)


for i in random_things:
    print ("Here's a random thing:", i)

# we can also build lists, first let's start with an empty one
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# now we can print them out too
print(people)

# and remove some
people.remove("Sarah")
print(people)

for person in people:
    print("Person is:", person)

# Challenge 
for i in range(1,11):
    print(f"squares of the number {i} is", i*i)

# here's how you access elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("They're are this many things:", len(random_things))
print("thing is a:", type(random_things))

another_list = random_things[-1]
print(another_list)
print(type(another_list))


