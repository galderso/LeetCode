class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        for i in range(len(s2)):
            for j in range(i,len(s2)):
                st = s2[i : j + 1]
                st = sorted(st)
                if st == s1:
                    return True
        return False