class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            stri=str(n)
            n=sum(int(digit)**2 for digit in stri)
        return True
        