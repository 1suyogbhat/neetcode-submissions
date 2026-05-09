class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #more efficent way, O(n)

        # build freq map
        # build a list of buckets
        # fill in the buckets 
        # and read right to left
        # the first k buckets (elements) that are non-zero will be the top k frequent

        #hashmap is for calculating frequency, 4 : 3, 4 appears 3 times in the array
        
        freq = {} 
        for num in nums:
            if num not in freq:  
                freq[num] = 0
            freq[num] += 1
            
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([]) #made a list named buckets with length num+1 slots

        # buckets = [[], [], [], [], [], [], []]
        # index of bucket = frequecy of the element in that index
        # key from freq = element value @ index freq[num]

        for num, count in freq.items(): #.items() returns the key-value pair
            buckets[count].append(num) #so for buckets at the count index (HM value), add num (HM key)

        res = []
        for i in range(len(buckets)-1, -k, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
            

        
                
                

        

        
        
    




