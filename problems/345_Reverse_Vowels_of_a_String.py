class Solution:
    def reverseVowels(self, s: str) -> str:
        head = 0
        tail =len(s)-1
        s=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while head<tail:
            if s[head] not in vowels:
                head+=1
            if s[tail] not in vowels:
                tail-=1
            if s[head] in vowels and s[tail] in vowels:
                tmp = s[head]
                s[head] = s[tail]
                s[tail] = tmp
                head+=1
                tail-=1
            
        return ''.join(s)
