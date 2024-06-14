my_keys = ['Ten', 'Twenty', 'Thirty']
my_values = [10, 20, 30]
for i in zip(my_keys, my_values):
   print(i)


family = {'Rick':43,'Beth':13,'Morty':5, 'Summer': 8}

total_cost = 0

for name, age in family.items():
   if age < 3:
      ticket_price = 0
   elif 3<age<12:
      ticket_price = 10
   else:
      ticket_price = 15

   print(f"{name} ticket's cost ${ticket_price}.")

   total_cost += ticket_price
print(f"The total cost of the family is ${total_cost}.")

#Bonus
family = {} 

while True:  
   names = input("Enter a name of a famiily member: ")
   age = int(input("Enter an age: "))
   family[names] = age

 total_cost = 0

for names, age in family.items():
   if age < 3:

Exercise 3

brand = {
   "name": "Zara", "creation_date" : 1975 , "creator_name": "Amancio Ortega Gaona", "type_of_clothes": {"men", "women", "children", "home"}
,"international_competitors": {"Gap", "H&M", "Benneton"}, "number_of_stores": 7000, "major_color": {"France": "blue", "Spain" : "red", "US": {"pink","green"}}}


brand["number_of_stores"] = 2 
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")


brand{"country_creation"} = "Spain"

 if "international_competitors" in brand:
   brand{"international_competitors"}.append("Desigual")

delete.brand{}




users = ["users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {user: i for i, user in enumerate(users)}
print(disney_users_A)

disney_users_B = {i: user for i, user in enumerate(users)}
print(disney_users_B)

disney_users_C = dict(sorted([(user, i) for i, user in enumerate(users)]))
print(disney_users_C)

disney_users_A_i = {user: i for i, user in enumerate(users) if "i" in user}
print(disney_users_A_i)

disney_users_A_mp = {user: i for i, user in enumerate(users) if user.startswith(("m", "p"))}
print(disney_users_A_mp)

   
