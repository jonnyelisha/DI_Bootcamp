#Exercise1

import random
def get_words_from_file(file_location):
    with open(file_location) as file:
        contents = file.read().split()
    return contents

words_list = []
def get_random_sentence(length: int):
    global words_list
    if length > len(words_list):
        raise ValueError("Sample larger than population or is negative")
    random_words = random.sample(words_list, length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    global words_list
    print("This program generates a random sentence from a list of words.")
    print("You can specify the length of the sentence you want to generate.")
    while True:
        try:
            length = int(input("Enter the length (between 2 and 20) of the sentence: "))
            if length <= 1 or length > 20:
                print("Please integer between 2 and 20.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    file_location = "Week2/Day 4/words.txt"
    words_list = get_words_from_file(file_location)
    print(get_random_sentence(length))

if __name__ == "__main__":
    main()



#Exercise 2: Working With JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


"""Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file."""


contents_dict = json.loads(sampleJson)  # json.loads reads a json string
print(contents_dict["company"]["employee"]["payable"]["salary"])
contents_dict["company"]["employee"]["birth_date"] = "1998-08-30"
new_json_file_location = "Week2/Day 4/new_data.json"

with open(new_json_file_location, mode="w") as file:
    json.dump(contents_dict, file)
