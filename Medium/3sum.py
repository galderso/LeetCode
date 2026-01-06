class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        numbers =defaultdict(int)
        valid =[]
        for num in nums:
            numbers[num]=numbers[num]+1
        for i, num in enumerate(nums):
            numbers[nums[i]]=numbers[nums[i]]-1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                numbers[nums[j]]=numbers[nums[j]]-1
                if j-1 > i and nums[j]==nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if numbers[target]>0:
                    valid.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums)):
                numbers[nums[j]] += 1
        return valid
            