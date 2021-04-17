class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1,1]
        if n==0 or n==1:
            return l[n]
        elif n>=2:
            for x in range(2,n+1):
                l.append(l[x-1]+l[x-2])
            return l[n]
        '''        
        if n >= 2:
            return self.climbStairs(n-2)+self.climbStairs(n-1)
        elif n==1:
            return 1
        else:
            return 1
        '''