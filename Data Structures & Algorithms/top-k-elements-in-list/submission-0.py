class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an array and int k, return the k-most frequent elements
        # if k = 2, return the 2 most frequent elements within that array

        # iterate through the array if the element is the first time weve seen it
        # add to hash map as a key, and make the value the numberof times seen, 
        # so right now just once

        # next number, if not seen yet do the same, otherwise if seen, increment 
        #the value in some way to indicate that its been seen again

        #once done for each number, go through the list of values, the lists with that 
        #have the kth biggest length and above can be printed

        kMap = {} #hashmap 
        for num in nums:
            if num not in kMap:
                kMap[num] = [] #make the number a key in the hashmap if first sight
            kMap[num].append(num) #append anything to increase length

        # now we have a hashmap that includes all numbers and the amount of times
        #go thru list of values to find kth highest and above lengths to return

        kList = kMap.values() #kList = list of values
        #sub lc - have list, return top k highest length keys

        #sort kList in des order so highest values come first 
        kList = sorted(kList, key=len, reverse=True)

        res = [] # create new empty list
        for i in range(k): #iterate through the sorted list of map values k-times
            res.append(kList[i][0]) #apply the pattern and keep adding to res
        return res #after k times, return the list 'res'

        #pattern for appending (order doesn't matter for return statement)
        #k = 1, return kList[0][0] (first element of first sub list)
        #k = 2, return kList[0][0], kList[1][0] (same as k=1 and first element of second sublist)
        # this works because the hashmaps values is the same as the key:
        # 1 : 1,1,1,1
        # 2: 2,2
        #so thats why when returning the element from kList, the value is the key
        # making it so we dont need to go find the key again






