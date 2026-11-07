class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for i in range (len(nums) - 1):
            my_map[nums[i]] = i
            if nums[i + 1] in my_map:
                return True
            
        return False