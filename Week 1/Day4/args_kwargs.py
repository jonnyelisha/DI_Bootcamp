##*args

def email_list(*usernames):
    email_list = []
    for user in usernames:
        user_email = user + "gmail.com"
        email_list.append(user_email)

    return email_list

print(email_list('Jonathan', etc.))

def (user_info_complicated(name = "jjj", email = "Fsda", age = 123))

def user_info2(name, email, age):
    details = {}
    details['name']  = name
    details['emails'] = email
    details['age'] = age
    return details