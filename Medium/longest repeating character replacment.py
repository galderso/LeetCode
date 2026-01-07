class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0

        charset = set(s)
        for i in charset:
           count =0
           left =0
           for right in range(len(s)):
                if s[right] == i:
                    count+=1


                while (right-left+1) -count>k:
                    if s[left] ==i:
                        count-=1
                    left+=1 

                res = max(res, right-left+1)
      
        return res