class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ['I','V','X','L','C','D','M']
        value = [1,5,10,50,100,500,1000]
        output = 0
        for x in range(len(s)):
            if s[x] == 'I' and ('V' in s[x:] or'X' in s[x:]): 
                output-=value[symbol.index(s[x])]
            elif s[x] == 'X' and ('L' in s[x:] or'C' in s[x:]): 
                output-=value[symbol.index(s[x])]
            elif s[x] == 'C' and ('D' in s[x:] or'M' in s[x:]): 
                output-=value[symbol.index(s[x])]
            else:
                output+=value[symbol.index(s[x])]
        return output