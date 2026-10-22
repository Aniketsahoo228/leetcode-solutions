class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        """
        Approach:
        1. Convert the digits list into a string using map(str, digits).
        2. Join all the digits into one string using "".join().
        3. Convert the joined string into an integer using int().
        4. Add 1 to the integer and store it in new_value.
        5. Convert new_value back into a string using str().
        6. Convert each character back into an integer using map(int, ...).
        7. Store the resulting digits in a list and return it.
        """

        value = int("".join(map(str,digits)))
        new_value = value + 1 
        digits = list(map(int,str(new_value)))
        return digits            