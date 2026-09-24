class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1= {}
        mp2= {}

        for it in s:
            mp1[it]= mp1.get(it,0)+1
        for it in t:
            mp2[it]= mp2.get(it,0)+1
        return (mp1==mp2)
