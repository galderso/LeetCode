class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =  nums
        res2 = 1
        count =0
        for num in nums:
            if num != 0:
                res2=res2*num
            else:
                count=count +1
        if count>1:
            return [0]*len(nums)
        
        for i in range(0,len(nums)):
            print(res2)
            if count ==0:
                res[i]=res2//nums[i]
            else:
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = res2
        return res