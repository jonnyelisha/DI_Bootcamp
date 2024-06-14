from functools import reduce


def uppers_list(string):
    return string.upper()

fruit = ["dpple", "doeo", "das"]

map_obj = map(uppers_list, fruit)

print(list(map_obj))

#filter

def start_with_A(string):
    return string[0] == "B"

fruits2 = ["Apple","Banana"]

filtered = list(filter(starts_with_A, fruits2)
print(filtered)

def sum_numbers(*args):
    for arg in args:
        


##for data analysis, you have numbers that are mixed with floats and integers
        map - go to each row and convert
