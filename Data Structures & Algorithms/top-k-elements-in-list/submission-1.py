class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kMap = {} 
        for num in nums:
            if num not in kMap:
                kMap[num] = [] 
            kMap[num].append(num) 

        kList = kMap.values() 
        kList = sorted(kList, key=len, reverse=True)

        res = [] 
        for i in range(k):
            res.append(kList[i][0]) 
        return res 
        
    




