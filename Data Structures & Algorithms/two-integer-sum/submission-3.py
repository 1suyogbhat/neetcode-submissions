class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seenMap = {} # value : index
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in seenMap:
                # seenMap[diff] = index of diff, diff being the first value we saw
                # because we only match via hashmap, first value is in the hashmap
                # and the second one is still in the array
                # i starts at 0 so index i = iterations - 1 
                return [seenMap[diff], i]
            seenMap[num] = i #if not in map, set num(value) to i (index)
                


      
