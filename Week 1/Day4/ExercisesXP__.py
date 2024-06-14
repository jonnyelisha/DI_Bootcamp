
Exercise1
def display_message():
    print("This is how functions work")
display_message()



Exercise2
def favorite_book(title):
        print(f"One of my favorite books is {title}")
    
favorite_book("Alice in Wonderland")


Exercise3

def describe_city(city, country = "USA"):
    print(f"{city} is in {country}")

describe_city("reere")
describe_city("Kentucky", "France")

Exercise4
import random


def number_acceptance():
    num1 = int(input(f"Give me a number from 1-100: "))
    if 1< num1 < 100:
        rand_num= random.randint(1,100)
        if num1 == rand_num:
            print("Success")
        else:
            print(f"Failure {num1}, {rand_num}")
    else:
        print("Choose another number")


number_acceptance()


size = {S,M,L}





Exercise 5
def make_shirt(size = "S",text = "I love Python"):
    print(f"Your size is {size} with it saying {text}")

make_shirt("Large")
make_shirt("Medium")
make_shirt("Medium", "Stuff")




Exercise#6
magicians_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(f"{magician}")

show_magicians(magicians_names)





#Exercise 7
import random
rand_temp = {}


def get_random_temp():
    rand_temp  = random.randint(-10,40)
    return rand_temp


def main():
    rand_temp =  get_random_temp()
    print(f"The temperature right now is {rand.temp} degrees Celcius")
    if rand_temp <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0<rand_temp< 16:
        print("Quite chilly! Don’t forget your coat”)
    elif 24< rand_temp <32:
        print("Quite chilly! Don’dfggfdt forget your coat”)
    else:
        print("Nah Fam")



import random

def get_random_temp():
    rand_temp = random.randint(-10, 40)
    return rand_temp

def main():
    rand_temp = get_random_temp()
    print(f"The temperature right now is {rand_temp} degrees Celsius")
    if rand_temp <= 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 < rand_temp < 16:
        print("Quite chilly! Don't forget your coat")
    elif 24 < rand_temp < 32:
        print("It's quite pleasant outside!")
    else:
        print("Nah, it's a beautiful day!")

if __name__ == "__main__":
    main()
