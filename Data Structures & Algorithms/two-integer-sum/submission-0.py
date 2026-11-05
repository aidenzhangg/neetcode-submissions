class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, n in enumerate (nums):
            need = target - n
            if need in my_map:
                return [my_map[need], i]
            
            my_map[n] = i