class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join([char for char in s if char.isalnum()]).lower()
        left = 0
        right = len(newS)-1
        while left < right:
            if newS[left] != newS[right]:
                return False
            left+=1
            right-=1   
        return True 


        