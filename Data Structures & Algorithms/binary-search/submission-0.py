class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left <= right: 
            mid = (left + right) // 2
            if (target > mid):
                left = mid + 1
            elif (target < mid):
                right = mid - 1
            elif (target == mid):
                return nums[mid]
        return -1