class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = []  # Create an empty list

        for items in s:
            if items.isalnum():  # Keep letters and numbers
                chars.append(items.lower())  # Add lowercase character to the list

        string = "".join(chars)  # Join all characters into one string
        if string == string[::-1]:  # Compare with reversed string
            return True
        else:
            return False
    
        