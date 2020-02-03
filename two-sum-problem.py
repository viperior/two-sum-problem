from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        operand_a_list = nums[:]
        
        # Remove operands that are not possible due to being greater than the sum.
        # This would not be valid if negative numbers were allowed.
        for value in nums:
            if value >= target and target > 1:
                operand_a_list.remove(value)
        
        for i, operand_a in enumerate(operand_a_list):
            # Remove operand a from the list of operand b's to evaluate.
            operand_b_list = operand_a_list[:]
            operand_b_list.remove(operand_a)
            
            for j, operand_b in enumerate(operand_b_list):
                if operand_a + operand_b == target:
                    solution_indices = []
                    operand_a_index = nums.index(operand_a)
                    
                    # Handle case where elements repeat in input array.
                    if operand_a == operand_b:
                        nums_list_without_operand_a = nums[:]
                        del nums_list_without_operand_a[operand_a_index]
                        operand_b_index = nums_list_without_operand_a.index(operand_b) + 1
                    else:
                        operand_b_index = nums.index(operand_b)
                    
                    solution_indices = [operand_a_index, operand_b_index]
                    self.display_solution(solution_indices, nums, target)
                    return solution_indices
                    
    def display_solution(self, solution_indices, nums, target):
        print('List of integers:')
        
        # If input list is large, show only the first and last three elements.
        if len(nums) > 20:
            print(str(nums[0:3]) + '...' + str(nums[len(nums) - 4:len(nums) - 1]))
        else:
            print(str(nums))
        
        print('Solution indices: ' + str(solution_indices))
        print(str(nums[solution_indices[0]]) + ' + ' + str(nums[solution_indices[1]]) + ' = ' + str(target))
        
solution_a = Solution().two_sum(list(range(1, 6)), 3)
solution_b = Solution().two_sum(list(range(1, 8)), 6)
solution_c = Solution().two_sum([3, 3], 6)
solution_d = Solution().two_sum(list(range(8900, 100001, 21)), 93316)
solution_e = Solution().two_sum([0,4,3,0], 0)
