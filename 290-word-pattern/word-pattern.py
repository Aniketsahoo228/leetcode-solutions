
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Approach:
        1. Split the string s into a list of words using split().
        2. Check whether the length of pattern matches the number of words.
        3. If the lengths are different, return False.
        4. Create two empty dictionaries:
           - cw maps each character to its corresponding word.
           - wc maps each word to its corresponding character.
        5. Traverse the indices of pattern using range(len(pattern)).
        6. Get the current character c and word w using their indices.
        7. If c already exists in cw but maps to a different word, return False.
        8. If w already exists in wc but maps to a different character, return False.
        9. Store both mappings in their respective dictionaries.
        10. If all mappings are valid, return True.
        """

        words = s.split()  # Split s into individual words

        if len(pattern) != len(words):  # Check whether lengths match
            return False  # Different lengths cannot follow the pattern

        cw = {}  # Map characters to words
        wc = {}  # Map words to characters

        for i in range(len(pattern)):  # Traverse each index
            c = pattern[i]  # Get the current pattern character
            w = words[i]  # Get the corresponding word

            if c in cw and cw[c] != w:  # Check character mapping
                return False  # Character maps to a different word

            if w in wc and wc[w] != c:  # Check word mapping
                return False  # Word maps to a different character

            cw[c] = w  # Store character-to-word mapping
            wc[w] = c  # Store word-to-character mapping

        return True  # All mappings follow the pattern
