class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = defaultdict(list)
        for num in nums: 
            res[num]=1+ res.get(num, 0)

        
        arr = []
        for num,cnt in res.items():
            arr.append([cnt,num])
        arr.sort()
        res2 = []
        while len(res2) <k:
            res2.append(arr.pop()[1])
        return res2