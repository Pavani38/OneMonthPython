def greet(name):
    return f"Hey {name}!"

def concatenate(word_one, word_two):
    return word_one + word_two

def age_in_dog_years(age):
    result = age * 4
    return result

print(greet('Pavani'))
print(greet('Chris'))

print(concatenate('Pavani','Gajula'))

print(age_in_dog_years(24))

print(concatenate(word_two="Pavani", word_one="Gajula"))

name = "Pavani"

def print_different_name():
    name = "Manasa"
    print(name)

print(name) #Pavani
print_different_name()#Manasa
print(name)#Pavani

#Challenge

def uppercase_and_reverse(fruit_name):

    return (fruit_name.upper())[::-1]

print(uppercase_and_reverse("banana"))
