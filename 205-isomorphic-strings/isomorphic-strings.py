
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Approach:
        1. Create an empty dictionary to map characters from s to t.
        2. Traverse both strings simultaneously using zip(s, t).
        3. If a character x from s is not in the dictionary, map it to y.
        4. If x already exists, check whether it maps to the current y.
        5. If the mapping does not match, return False.
        6. Create a new empty dictionary to check the reverse mapping.
        7. Traverse both strings again and map characters from t to s.
        8. If a character y already exists but maps to a different x,
           return False.
        9. If both mappings are valid, return True.
        """

        seen = {}  # Store mappings from s characters to t characters

        for x, y in zip(s, t):  # Traverse both strings together
            if x not in seen:  # Check if x has been mapped
                seen[x] = y  # Map x to y
            else:
                if seen[x] != y:  # Check for inconsistent mapping
                    return False  # Characters do not follow the same mapping

        seen = {}  # Reset the dictionary for reverse mapping

        for x, y in zip(s, t):  # Traverse both strings again
            if y not in seen:  # Check if y has been mapped
                seen[y] = x  # Map y back to x
            else:
                if seen[y] != x:  # Check for inconsistent reverse mapping
                    return False  # Multiple characters map to the same character

        return True  # Both mappings are valid
