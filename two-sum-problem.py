from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for value in nums[:]:
            if value >= target:
                nums.remove(value)
        
        for i, value in enumerate(nums):
            operand_b_list = nums[:]
            operand_b_list.remove(value)
            
            for j, operand_b in enumerate(operand_b_list):
                if value + operand_b == target:
                    return [nums.index(value), nums.index(operand_b)]
        
solution = Solution()
print(solution.twoSum(nums = [1, 2, 3, 4, 5, 6, 7], target = 6))
