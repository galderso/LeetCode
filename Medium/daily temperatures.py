class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        left = 0
        right =0
        found = False
        results = []
        while left < len(temperatures):
            if left == len(temperatures)-1:
                results.append(0)
                break
            right = left + 1
            found = False
            for i in range(len(temperatures)):
                if right >= len(temperatures):
                    break
                if temperatures[right]> temperatures[left]:
                    results.append(right-left)
                    left+=1
                    found = True
                    break
                else:

                    right+=1
            if not found:      
                results.append(0)
                left += 1
        return results