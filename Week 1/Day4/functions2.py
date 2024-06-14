## Ask her exactly what is going on there n

students =['Harry','Hermione', 'Ron', 'Shlomi']
students2  = ['Maria', 'Jeff', 'Masf', 'Menachem']

def wizard(student_list):
    for name in student_list:
        print(f'{name}, you are a wizard')

wizard(students2)

def students_house():
    for i, name in enumerate(students):
        students[i] = f'{name}'  - 'house: Gryfinndor'
     

students_house()
print(students)
