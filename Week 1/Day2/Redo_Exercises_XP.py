#Exercise1
#Instructions
#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_number


my_fav_numbers = {7, 13, 42, 99}
friend_fav_numbers = {3, 17, 31, 61}

my_fav_numbers.add(11)
my_fav_numbers.add(23)

my_fav_numbers.remove(99)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#Exercise2 
Question: Given a tuple which value is integers, is it possible to add more integers to the tuple?
Answer: It is not possible to add more integers to the tuple because it is immutable

#Exercise3 
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
print("There are", apple_count, "apples in the basket.")
print(basket)


#Exercise4
Question:  Difference between a float and integer
Answer:  float is a data type in Python that can represent a decimal number. The main difference between an integer and a float is that a float can have a fractional part, while an integer can only represent whole numbers.

Question: Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
Answer:  numbers = [num / 2 for num in range(3, 11)]

Question: Can you think of another way to generate a sequence of floats?
Answer: None that I can think of 

#Exercise5
Question: Use a for loop to print all numbers from 1 to 20, inclusive.
Answer: for num in range(1, 21):
    print(num)

Question: Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
Answer: for i in range(1, 21):
            if i % 2 == 0:
        print(i)

#Exercise6
Question: Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
Answer: my_name = "Jonathan "

while True:
    user_name = input("What is your name? ")
    if user_name == my_name:
        break


#Exercise7
Question:
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

Answer: 
favorite_fruits = input("Enter your favorite fruit(s) separated by a space: ").split()

fruit_to_check = input("Enter the name of a fruit: ")

if fruit_to_check in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")


#Exercise8
Question: Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

Answer: toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

print("Your pizza has the following toppings:")
for topping in toppings:
    print(f"- {topping}")

total_price = 10 + 2.5 * len(toppings)
print(f"The total price for your pizza is ${total_price:.2f}")

#Exercise9
Question: 
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.
Answer:
total_cost = 0

while True:
    age = int(input("Enter the age of a family member (or -1 to finish): "))
    if age == -1:
        break
    if age < 3:
        ticket_price = 0
    elif age < 13:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price
    print(f"The ticket for a person aged {age} costs ${ticket_price}")

print(f"The total cost for the family is ${total_cost}")

teenager_names = ["John", "Jane", "Bob", "Alice"]
for name in teenager_names[:]:
    age = int(input(f"Enter the age of {name}: "))
    if age < 16 or age > 21:
        teenager_names.remove(name)

print("The final list of teenagers allowed to watch the movie:", teenager_names)

#Exercise10
Question: 
Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
We need to prepare the orders of the clients:
Create an empty list called finished_sandwiches.
One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
I made your tuna sandwich
I made your avocado sandwich
I made your egg sandwich
I made your chicken sandwich


Answer: sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich}.")

print("\nAll orders have been completed.")
