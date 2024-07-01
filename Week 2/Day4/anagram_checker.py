from collections import Counter
import random

#Using list comprehension 

words = [element.replace('\n', '').lower() for element in open('sowpods.txt', 'r').readlines()]

class AnagramChecker():

    