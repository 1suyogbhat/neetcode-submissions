class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        tList = []

        for char in s:
            sList.append(char)

        for char in t:
            tList.append(char)

        # sList = r,a,c,e,c,a,r
        # tList = c,a,r,r,a,c,e

        clean_sList = sorted(sList) # a,a,c,c,e,r,r
        clean_tList = sorted(tList) # a,a,c,c,e,r,r

        if clean_sList == clean_tList:
            return True

        else:
            return False