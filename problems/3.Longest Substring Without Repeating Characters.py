class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        subString = ''
        for char in s:
            if char in subString:
                repeatIdx = subString.index(char)
                if repeatIdx == len(subString) -1:
                    subString = ''
                else:
                    subString = subString[repeatIdx+1:]   
            subString += char
            maxLen = max(maxLen,len(subString))
        return maxLen