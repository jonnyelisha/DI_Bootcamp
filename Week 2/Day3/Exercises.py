#Exercise1:


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other):
        if isinstance(other, Currency) and other.currency == self.currency:
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if isinstance(other, Currency) and other.currency == self.currency:
            self.amount += other.amount
            return self
        elif isinstance(other, (int, float)):
            self.amount += other
            return self
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

# Example usage
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  
print(int(c1))  
print(repr(c1))  
print(c1 + 5)  
print(c1 + c2)  
print(c1)  
c1 += 5
print(c1)  
c1 += c2
print(c1)  
#Exercise 2: Import

func.py:


def sum_numbers(a, b):
    print(a + b)
exercise_one.py:

from func import sum_numbers

sum_numbers(5, 10)
#Exercise 3

import string
import random

def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(5))

print(generate_random_string())
#Exercise 4: Current Date


import datetime

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

print(get_current_date())


#Exercise 5

import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    next_new_year = datetime.datetime(now.year + 1, 1, 1)
    time_left = next_new_year - now
    return f"The 1st of January is in {time_left.days} days and {time_left.seconds // 3600}:{(time_left.seconds % 3600) // 60}:{time_left.seconds % 60} hours."

print(time_until_new_year())
#Exercise 6: Birthday And Minutes


import datetime

def minutes_since_birthday(birth_date_str):
    birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    now = datetime.datetime.now()
    minutes_lived = (now - birth_date).total_seconds() // 60
    return f"You have lived for {int(minutes_lived)} minutes."

print(minutes_since_birthday("1990-05-15"))
#Exercise 7: Faker Module

python
Copy
from faker import Faker

fake = Faker()

users = []

def add_user():
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users.append(user)

for _ in range(5):
    add_user()

print(users)
