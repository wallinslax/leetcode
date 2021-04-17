class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]*(num+1)
        if num == 0: 
            return result
        result[1]=1
        
        power = 1
        m = 0
        for i in range(2, num+1):
            print(i)
            if i == power*2:
                result[i] = 1
                power *= 2
                m = 1
            else:
                result[i]= result[m]+result[power]
                m += 1
            
        return result