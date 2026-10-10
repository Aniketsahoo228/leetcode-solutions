class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies[x] for x in range(len(candies)))
        arr = []
        for items in candies:
            if int(items) + extraCandies >= max_candies:
                arr.append(True)
            else:
                arr.append(False)    
        return arr
         