class Solution:
    def longestPalindrome(self, s: str) -> str: 
        if s=="":
            return ""
        
        for i in range(len(s),0,-1):
            #print(i)
            for j in range(len(s)+1-i):
                #print(j)
                x = s[j:j+i]
                if self.isPalindromic(x):
                    return x
    def isPalindromic(self, x: str) -> bool:
        if len(x) == 1:
            return True
        elif len(x)==2 and x[0]==x[1]:
            return True
        else:
            return x[0]==x[-1] and self.isPalindromic(x[1:len(x)-1])
            
            
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        if ls < 2:
            return s
        for i in range(ls):
            for j in range(i+1):  
                res = s[j:ls-i+j]
                if res == res[::-1]:          #check if the substring is a palindrome
                    return res