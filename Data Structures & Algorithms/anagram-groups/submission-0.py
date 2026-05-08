class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input = array of strings, input = [cat, tac, lop, hel, pol]
        #output = create sublists of all anagrams, return these sublists
        #in this string the output should be:
        # [[hel], [cat, tac], [lop, pol]] -> any order is okay

    
    #for every word in the array we have to put it in a hashmap
    #where the key of the hashmap is the sorted version of that word, and the value
    # is the set of anagrams from the list of that sorted word

    #if a key(sorted version of a word) is not in the map, add it
    # after adding it, also add that, at that key, there is a value, and that value is
    # the unsorted original array version of that word
    # in the very end return the list of the values

        anagramHash = {} #hashmap of anagrams

        for word in strs:
            key = "".join(sorted(word)) #sort the word and make it one word separated
            # by nothing, "cat" sorted returns [a,c,t], we need act, join the word with nothing in between

            if key not in anagramHash:
                anagramHash[key] = [] #make key a key, no current values
                
            anagramHash[key].append(word) #make the value the unsorted original version

        return list(anagramHash.values()) #takes all values for each key and prints a list of them
















