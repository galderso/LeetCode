class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
   
        left = 1
        right =max(piles)
        while left <= right:
            mid = (left+right)//2
            total = 0
            for pile in piles:
                total+=math.ceil(float(pile)/mid)
            if total <= h:
   
                right =mid-1
            else:
                left = mid +1
        return left