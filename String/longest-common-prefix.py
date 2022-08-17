# source: https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        shortest = min(strs,key=len)
        
        for m in range(len(shortest)):
            for str in strs:
                if str[m]!=shortest[m]:
                    return prefix
                    break
            prefix += shortest[m]
        
        return prefix
        
       
