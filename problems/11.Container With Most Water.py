class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        maxArea = 0
        # triverse all water level
        for waterLevel in set(height):
            #find left bound
            for x in range(len(height)):
                if height[x]>=waterLevel:
                    leftBound = x
                    break
            #find right bound
            for x in reversed(range(len(height))):
                if height[x]>=waterLevel:
                    rightBound = x
                    break
                    
            #calculate area
            area = (rightBound-leftBound)*waterLevel
            if area>maxArea:
                maxArea = area
        return maxArea
#----------------------------------------------------------------
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        maxArea = 0
        leftBound = 0
        rightBound = len(height)-1
        while leftBound<rightBound:
            maxArea = max(maxArea, min(height[rightBound],height[leftBound])*(rightBound-leftBound) )
            if height[leftBound] < height[rightBound]:
                leftBound+=1
            else:
                rightBound-=1
        return maxArea
