from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        operand_a_list = nums[:]
        
        for value in nums:
            if value >= target:
                operand_a_list.remove(value)
        
        for i, value in enumerate(operand_a_list):
            operand_b_list = operand_a_list[:]
            operand_b_list.remove(value)
            
            for j, operand_b in enumerate(operand_b_list):
                if value + operand_b == target:
                    solution_indices = [nums.index(value), nums.index(operand_b)]
                    self.display_solution(solution_indices, nums, target)
                    return solution_indices
                    
    def display_solution(self, solution_indices, nums, target):
        print('List of integers: ' + str(nums))
        print('Solution indices: ' + str(solution_indices))
        print(str(nums[solution_indices[0]]) + ' + ' + str(nums[solution_indices[1]]) + ' = ' + str(target))
        
solution_a = Solution().two_sum(list(range(1, 6)), 3)
solution_b = Solution().two_sum(list(range(1, 8)), 6)
solution_c = Solution().two_sum(list(range(8900, 100001, 21)), 93316)
