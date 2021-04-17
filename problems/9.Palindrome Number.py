class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) == 1:
            return True
        elif len(x)==2 and x[0]==x[1]:
            return True
        else:
            return x[0]==x[-1] and self.isPalindrome(x[1:len(x)-1])