# Get-Content lala | python.exe .\stdin.py

class Solution:
    def show(self, line):
        return line

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            
            ret = Solution().show(line)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()