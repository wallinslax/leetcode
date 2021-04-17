class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        head = 0
        tail = len(s)-1
        deleteCount=1
        while head<tail and deleteCount>=0:
            if s[head]==s[tail]:
                head+=1
                tail-=1
            else:
                if isPalindrome(s[head+1:tail +1]):
                    return True
                if isPalindrome(s[head:tail-1 +1]):
                    return True
                return False
        return True
def isPalindrome(s:str)->bool:
    s = list(s)
    head = 0
    tail = len(s)-1
    while head<tail:
        if s[head]==s[tail]:
            head+=1
            tail-=1
        else:
            return False
    return True
