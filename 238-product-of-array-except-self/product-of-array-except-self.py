class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        S=1
        zero = 0
        for x in nums:
            if x ==0:
                zero +=1
            else:
                S*=x
        ans=[]
        for x in nums:
            if zero ==0:
                ans.append(S//x)
            elif zero-(x==0)==0:
                ans.append(S)
            else :
                ans.append(0)
        return ans