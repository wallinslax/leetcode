class Solution:
    def intToRoman(self, num: int) -> str:
        map = [['M',1000],
               ['CM',900],
               ['D' ,500],
               ['CD',400],
               ['C' ,100],
               ['XC', 90],
               ['L' , 50],
               ['XL', 40],
               ['X' , 10],
               ['IX',  9],
               ['V' ,  5],
               ['IV',  4],
               ['I' ,  1],
              ]
        #print(map)
        l = ''
        for x in map:
            while x[1]<=num:
                num -= x[1]
                l += x[0]
        return l