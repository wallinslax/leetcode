class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1 or numRows >= len(s):
            return s
        rows = ['']*numRows
        direction = 1
        idxRow = 0
        for x in s:
            rows[idxRow]+= x
            
            if idxRow == 0:
                direction = 1
            elif idxRow == numRows-1:
                direction = -1
            idxRow += direction
        return ''.join(rows)