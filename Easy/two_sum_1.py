class Solution:
    
    def twoSum(self, nums:list, target: int) -> list[int]:
        
        result_sum_index = [] # Список с результирующими индексами для суммы

        if self.check_condition(nums, target):
            srez = None
            for i,v in enumerate(nums):
                if v > target:
                    srez = i
                    break
            
            if srez and 0 <= srez <= len(nums):
                nums = nums[:srez]

            for i in range(0, len(nums)):
                if 0 <= i+1 <= len(nums)-1:
                    if nums[i] + nums[i+1] == target:
                        result_sum_index.extend([i, i+1])
                    
        return result_sum_index

    def check_condition(self, nums:list, target: int) -> bool:
        
        if 2 <= len(nums) <= 10**4 or -10**9 <= target <= 10**9:
            for index, value in enumerate(nums,1):
                if not(-10**9 <= value <= 10**9):
                    return False
            return True

        return False