class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        nums.sort()
        res = 1
        current = 1
        print(nums)
        for i in range(0,len(nums)):
            
            
            if nums[i-1] == nums[i]-1 :
                print("num[i]: ",nums[i]," num[i-1]: ",nums[i-1],"add one")
                current = current+1
            elif nums[i-1]==nums[i]:
                continue
            else:
                current = 1
            res = max(res,current)
            print(res)
        return res
        