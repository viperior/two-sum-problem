from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        operand_a_list = nums[:]
        
        # Remove operands that are not possible due to being greater than the sum.
        for value in nums:
            # Abort optimization method if a negative number is detected.
            if value < 0:
                break
            
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
                    return solution_indices
                    
    def display_solution(self, solution_indices, nums, target):
        print('List of integers:')
        
        # If input list is large, show only the first and last three elements.
        if len(nums) > 20:
            print(str(nums[0:3]) + '...' + str(nums[len(nums) - 4:len(nums) - 1]))
        else:
            print(str(nums))
        
        print('Solution indices: ' + str(solution_indices))
        print(str(nums[solution_indices[0]]) + ' + ' + str(nums[solution_indices[1]]) + ' = ' + str(target) + '\n')

tests = [
    [list(range(1, 6)), 3],
    [list(range(1, 8)), 6],
    [[3, 3], 6],
    [list(range(8900, 100001, 21)), 93316],
    [[0,4,3,0], 0],
    [[0,4,3,1], 1],
    [[5, 5, 6, 7, 6, 9, 15, 27], 12],
    [[-10,7,19,15], 9],
    [[-10, -10, -20, -5, 50, 13], -20]
]

for i, test in enumerate(tests):
    print('Test case #' + str(i + 1))
    Solution().display_solution(Solution().two_sum(test[0], test[1]), test[0], test[1])
