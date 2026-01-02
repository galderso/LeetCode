class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            srt = ''.join(sorted(s))
            res[srt].append(s)
        return list(res.values())