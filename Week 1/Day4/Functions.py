#functions are useful if using repetitive tasks and easily apply them to reuse the codes
#you can easily call it back


def say_hello():
    print("Hello")

say_hello()

def say_hello(name):
    print(f'Hello, {name}')

say_hello('Jonathan')


def say_hello(username,language):
    if language == "EN":
        print(f'Hello,{username}')
    elif language == "FR":
        print(f'Salut ,{username}')
    else:
        print("Sorry, there is no language {language}")

say_hello('Juliana', 'EN')


def user_info(username, email, age, password):
    print("user info: ", username, email, age, password)

user_info("j23", "jdasd@gamfieo.com", 25, "asdasdasda")

#quarks - 


#keyword argument - defining the argument


#kwargs
def user_info(**kwargs):
    return kwargs

prin