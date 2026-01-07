class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        current  = 0
        left = 0
        right = 0 
        found = []
        for i,char in enumerate(s):
            #move right if char[right] not in found
            #move left by amount of first found  if 

            if char in found:
                #pop everything up until first found and subtract the indexes from count
                while char in found:
                    found.pop(0)
                    current -= 1
            
            found.append(char)
            current+=1
            right+=1

            if current > res:
                res = current
        return res