class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i, v in enumerate(nums):
            if v in map:
                return True
            map[v] = i
        return False
        