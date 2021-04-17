class Solution:
    def jumpForward(self,arr,whereNowIdx,currentJumpIdx):
        isNext = False
        if currentJumpIdx%2 == 1: #Odd Jump: Find smallest bigger
            #print('Odd Jump=',currentJumpIdx,'/whereNowIdx=',whereNowIdx)
            minBigVal = max(arr[(whereNowIdx+1):])
            minBigIdx = (whereNowIdx+1) + arr[(whereNowIdx+1):].index(minBigVal)
            if arr[whereNowIdx] <= minBigVal:
                isNext = True
                for j in range(whereNowIdx+1,len(arr)):
                    if arr[whereNowIdx] <= arr[j] < minBigVal:
                        minBigVal = arr[j]
                        minBigIdx = j
                        #print('minBigIdx=',minBigIdx)
                        #print('minBigVal=',minBigVal)
                whereNowIdx = minBigIdx
            #else:
            #    print('no Next, isNext=',isNext)
                                              
        else: # Even Jump: Find Largest smaller
            #print('Even Jump',currentJumpIdx,'/whereNowIdx=',whereNowIdx)
            maxSmlVal = min(arr[(whereNowIdx+1):])
            maxSmlIdx = (whereNowIdx+1) + arr[(whereNowIdx+1):].index(maxSmlVal)
            if arr[whereNowIdx] >= maxSmlVal:
                isNext = True
                for j in range(whereNowIdx+1,len(arr)):
                    if arr[whereNowIdx] >= arr[j] > maxSmlVal:
                        maxSmlVal = arr[j]
                        maxSmlIdx = j
                        #print('maxSmlIdx=',maxSmlIdx)
                        #print('maxSmlVal=',maxSmlVal)
                whereNowIdx = maxSmlIdx
            #else:
            #    print('no Next, isNext=',isNext)
            
            
        return whereNowIdx, isNext
    
    def oddEvenJumps(self, arr: List[int]) -> int:
        goodIdx = [len(arr)-1]
        for evaluatingIdx in range(len(arr)-1):
            # Initialize Index
            whereNowIdx = evaluatingIdx
            currentJumpIdx = 1
            isNext = True
            # Evaluate if evaluatingIdx is Good
            while whereNowIdx < len(arr) and isNext:
                whereNowIdx, isNext = self.jumpForward(arr,whereNowIdx,currentJumpIdx)
                if whereNowIdx == len(arr)-1:
                    goodIdx.append(evaluatingIdx)
                    break
                else:
                    currentJumpIdx += 1
            #print('goodIdx=',goodIdx)
        return len(goodIdx)
