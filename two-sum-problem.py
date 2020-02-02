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
            
        original_list_element_count = len(nums_dict_list)
        invalid_candidates = []
        
        for num_dict in nums_dict_list:
            if num_dict['value'] >= target:
                invalid_candidates.append(num_dict)
        
        for candidate in invalid_candidates:
            nums_dict_list.remove(candidate)
        
        new_list_element_count = len(nums_dict_list)
        removed_item_count = original_list_element_count - new_list_element_count
        
solution = Solution()
solution.twoSum(nums = [1, 2, 3, 4, 5, 6, 7], target = 6)
