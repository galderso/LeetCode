class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        left =0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[left]< nums[right]:
                res = min(res, nums[left])
                break

            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return res