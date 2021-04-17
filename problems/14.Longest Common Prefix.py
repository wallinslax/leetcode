class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefixStr = ''
        # find smallest string
        minStr = min(strs,key=len)
        minLength = len(minStr)
        #print(minLength)
        #print(minStr)
        for idx in range(len(minStr)):
            for x in strs:
                #print("x="+x)
                if x[idx] != minStr[idx]:
                    return prefixStr
            prefixStr+= minStr[idx]
        return prefixStr