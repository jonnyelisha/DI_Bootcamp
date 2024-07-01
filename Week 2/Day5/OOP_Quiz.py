#Part 1: Quiz
# 1. What is a class? A class is the blueprint for creating objects and defines the properties of the objects.
# 2. What is an instance? An instance is a specific object from a class
# 3. What is encapsulation? Binds data (attributes) and the methods that operate on that data within a single unit (the class)
# 4. What is abstraction? Hiding the implementation details and showing only the essential features of an object or a system to the user.
# 5: What is inheritance? Inheritance is a mechanism in which a new class is based on an existing class.
# 6. What is multiple inheritance? A class can inherit properties and methods from more than one parent class.
# 7. What is polymorphism? Polymorphism is the ability of objects of different classes to respond to the same method call.
# 8. What is the method resolution order or MRO? Is the order in which a programming language searches for a method in a class hierarchy when the method is called on an object


#Part 2: Creating a Deck of Cards Class

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return (f"{self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
deck = Deck()
deck.shuffle()

card = deck.deal()
print(card) 




    