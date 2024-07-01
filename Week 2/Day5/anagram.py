from anagram_checker import AnagramChecker

class AnagramChecker:
    def load_word_list(self, file_path):
        with open(file_path, 'r') as file:
            return [word.strip().upper() for word in file.readlines()]

def main():
    anagram_checker = AnagramChecker()
    anagram_checker.word_list = anagram_checker.load_word_list('sowpods.txt')

    while True:
        print("Please enter a word (or 'q' to quit):")
        user_input = input().strip()

        if user_input.lower() == 'q':
            break

        anagrams = anagram_checker.get_anagrams(user_input)

        print(f"Your word is: \"{user_input.upper()}\"")
        if anagram_checker.is_valid_word(user_input):
            print("This word is valid.")
            if anagrams:
                print(f"Anagrams for your word: {', '.join(anagrams)}")
            else:
                print("No anagrams found for your word.")
        else:
            print(f"\"{user_input.upper()}\" is not a valid word.")

if __name__ == "__main__":
    main()