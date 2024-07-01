class AnagramChecker:
    def __init__(self, text_file):
        self.word_list = self.load_word_list(text_file)

    def load_word_list(self, text_file):
        with open(text_file, 'r') as file:
            return [word.strip().upper() for word in file.readlines()]

    def is_valid_word(self, word):
        return word.upper() in self.word_list

    def get_anagrams(self, word):
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w) and w != word.upper():
                anagrams.append(w)
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1.upper()) == sorted(word2.upper())