#Exercises 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat.name
        self.age = cat.age

def oldest_cat(cats):
    oldest_cat = max(cats,key = lambda cat: cat.age)
    return oldest_cat


cat1 = Cat("Jeff", 10)
cat2= Cat("Dad", 2)
cat3 = Cat("Bas", 23)

cats = [cat1, cat2, cat3]
oldest_cat = oldest_cat(cats)



print(f"The oldest cat is {oldest_cat.name} and and is {oldest_cat.age}.")

##Exercise2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog.")
else:
    print(f"{sarahs_dog.name} is the bigger dog.")




#Exercise 3
class song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics():
            print(line)

stairway = song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()
     

#Exercise4
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"The {self.name} has the following animals:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from the {self.name}.")
        else:
            print(f"{animal_sold} is not in the {self.name}.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        for group, animals in sorted_animals.items():
            print(f"{group}: {', '.join(animals)}")

ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

ramat_gan_safari.get_animals()
print()

ramat_gan_safari.sell_animal("Elephant")
print()

ramat_gan_safari.get_groups()

    