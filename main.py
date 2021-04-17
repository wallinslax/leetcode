# Get-Content lala | python.exe .\stdin.py
import sys
import io
import pickle
import problems.345_Reverse_Vowels_of_a_String
class Solution:
    def show(self, line):
        return line

if __name__ == '__main__':
    with open('input','rb') as f: 
        lines = f.readlines()
    for line in lines:
        textList = line.rstrip().decode("utf-8")
        textList = textList.replace('[','')
        textList = textList.replace(']','')
        inputArr = textList.split(',')
        inputArr = list(map(int,inputArr))
        print(inputArr)
        for i in inputArr:
            print(i)
        
        

    while True:
        try:
            line = next(lines)
            
            ret = Solution().show(line)

            out = str(ret);
            print(out)
        except StopIteration:
            break