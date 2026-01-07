class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = {}

        for i,num in enumerate(numbers):
            remainder =target-num

            if (target-remainder) in nums.keys():
 
                return [nums[target-remainder]+1, i+1]
            nums[remainder] = i