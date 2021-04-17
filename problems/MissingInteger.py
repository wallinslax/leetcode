# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if A == []:
        return 1
    A= list(set(A))
    for x in range(len(A)):
        if A[x]<=0 or A[x]>len(A):
            A[x] = 0
    for x in range(len(A)):
        while A[x] != x+1 and A[x] != 0:
            #put A[x] to it position
            temp = A[A[x]-1]
            A[A[x]-1] = A[x]
            A[x] = temp
    #print(A)
    for x in range(len(A)):
        if A[x] == 0:
            return x+1
    
    return len(A)+1