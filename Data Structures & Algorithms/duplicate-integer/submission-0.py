class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for it in nums:
            if it in mp:
                return True
            
            mp[it] = mp.get(it, 0) + 1
        return False