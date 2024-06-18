#Exercise1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [Bengal('Bengal', 5), Chartreux('Chartreux', 3), Siamese('Siamese', 2)]
sara_pets = Pets(all_cats)
sara_pets.walk()




#Exercise2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_speed = self.run_speed()
        other_speed = other_dog.run_speed()
        if my_speed * self.weight > other_speed * other_dog.weight:
            return f"{self.name} won the fight!"
        else:
            return f"{other_dog.name} won the fight!"

dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Lassie", 7, 30)
dog3 = Dog("Max", 3, 15)

print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog1))



#Exercise3
from exercise2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together.")

    def do_a_trick(self):
        if self.trained:
            import random
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")

dog1 = PetDog("Buddy", 5, 20)
dog2 = PetDog("Lassie", 7, 30)
dog3 = PetDog("Max", 3, 15)

dog1.train()
dog1.do_a_trick()
dog2.play(dog1, dog3)

#Exercise4
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the new addition!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name and not member['is_child']:
                return True
        return False

    def family_presentation(self):
        print(f"The {self.last_name} Family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

family.born(name='Baby Jack', age=0, gender='Male', is_child=True)
print(family.is_18('Michael'))
print(family.is_18('Baby Jack'))
family.family_presentation()



#Exercise5
from exercise4 import Family

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name and not member['is_child']:
                print(f"{member['incredible_name']} uses the power of {member['power']}")
            elif member['name'] == name and member['is_child']:
                raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")

    def incredible_presentation(self):
        print(f"*Here is our powerful family {self.last_name}*")
        super()
