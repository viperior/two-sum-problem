from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict_list = []
        current_num_index = 0
        
        for value in nums:
            current_num_dict = {}
            current_num_dict['index'] = current_num_index
            current_num_dict['value'] = value
            nums_dict_list.append(current_num_dict)
            current_num_index += 1
            
        for num_dict in nums_dict_list:
            if num_dict['value'] >= target:
                print('Invalid candidate detected: ' + str(num_dict['value']))
        
solution = Solution()
solution.twoSum(nums = [1, 2, 3, 4, 5, 6, 7], target = 5)
