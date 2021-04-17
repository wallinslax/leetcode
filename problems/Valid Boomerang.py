class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points1 = points[0]
        points2 = points[1]
        points3 = points[2]
        if points1 == points2 or points2 == points3 or points3 == points1:
            return False
        # check if i is same value
        if points1[0] == points2[0] == points3[0]:
            return False
        # check if j is same value
        elif points1[1] == points2[1] == points3[1]:
            return False
        # check if i,j is increment
        elif points1[0]== points1[1] and points2[0]== points2[1] and points3[0]== points3[1]:
            return False
        return True
        
The other idea is to calculate the slope of AB and AC.
K_AB = (p[0][0] - p[1][0]) / (p[0][1] - p[1][1])
K_AC = (p[0][0] - p[2][0]) / (p[0][1] - p[2][1]) 
We check if K_AB != K_AC, instead of calculate a fraction.
Time O(1) Space O(1)       
class Solution:
    def isBoomerang(self, p):
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])