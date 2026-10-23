
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Approach:
        1. Split the string s into a list of words using split().
        2. Check whether the length of pattern matches the number of words.
        3. If the lengths are different, return False.
        4. Create two empty dictionaries:
           - char_to_word maps each pattern character to a word.
           - word_to_char maps each word back to a pattern character.
        5. Traverse pattern and words together using zip().
        6. If a character already exists in char_to_word but maps to
           a different word, return False.
        7. If a word already exists in word_to_char but maps to
           a different character, return False.
        8. Store both mappings in their respective dictionaries.
        9. If all mappings are valid, return True.
        """

        words = s.split()  # Split s into individual words

        if len(pattern) != len(words):  # Check if lengths match
            return False  # Different lengths cannot follow the pattern

        char_to_word = {}  # Map pattern characters to words
        word_to_char = {}  # Map words to pattern characters

        for char, word in zip(pattern, words):  # Traverse both together
            if char in char_to_word and char_to_word[char] != word:
                return False  # Character maps to a different word

            if word in word_to_char and word_to_char[word] != char:
                return False  # Word maps to a different character

            char_to_word[char] = word  # Store character-to-word mapping
            word_to_char[word] = char  # Store word-to-character mapping

        return True  # All mappings follow the pattern
