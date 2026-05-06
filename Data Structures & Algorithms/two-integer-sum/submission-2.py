class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force way, comparing every other combination of number to = target

        for i in range(len(nums)): # for every number in nums
            for j in range(i + 1, len(nums)): #we cycle all the numbers to the right
                if nums[i] + nums[j] == target: # if 2 elements equal target
                    return [i, j] # return their index
        
    
      
