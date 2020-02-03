from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for value in nums[:]:
            if value >= target:
                nums.remove(value)
                
        for value in enumerate(nums):
            print(value)
        
solution = Solution()
print(solution.twoSum(nums = [1, 2, 3, 4, 5, 6, 7], target = 6))
