
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach:
        1. If n is less than or equal to 2, return n because there
           are n distinct ways to climb the stairs.
        2. Initialize prev2 = 1 to store the number of ways to reach
           the previous second step.
        3. Initialize prev1 = 2 to store the number of ways to reach
           the previous step.
        4. Iterate from step 3 to n.
        5. Calculate current as the sum of prev1 and prev2 because
           each step can be reached by taking either 1 or 2 steps.
        6. Update prev2 to prev1 and prev1 to current.
        7. Return prev1 as the total number of ways to reach step n.
        """

        if n <= 2:  # Handle the base cases
            return n  # There are n ways for 1 or 2 steps

        prev2 = 1  # Store ways to reach step 1
        prev1 = 2  # Store ways to reach step 2

        for i in range(3, n + 1):  # Calculate ways from step 3 to n
            current = prev1 + prev2  # Add ways from the previous two steps
            prev2 = prev1  # Move the previous result back one step
            prev1 = current  # Store the current result

        return prev1  # Return the total number of ways
