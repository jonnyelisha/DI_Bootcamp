
def uppers_list(string):
    return string.upper()

fruit = ["dpple", "doeo", "das"]

map_obj = map(uppers_list, fruit)

print(list(map_obj))

