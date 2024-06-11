from utils import unzip_with_7z
zip_file_path ='\7za.zip'
dest_path = './result' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 
# WRITE YOUR CODE BELOW
# ---------------------------------------- 
possible_letters = 'abcdefghijklmnopqrstuvwxyz'
for letter1 in possible_letters:
    for letter2 in possible_letters:
        find_me = letter1 + letter2
        secret_password = find_me + 'bcmpda'
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print('sucessfully found password: ', secret_password)
            break
    else:
        print('nope')
        continue
    break

