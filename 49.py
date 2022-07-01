from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        list=[]
        for i in range(0,len(strs)-1):
            for j in range(1,len(strs)):
                if Counter(strs[i])==Counter(strs[j]):
                    list.append([strs[i],strs[j]])
                    #strs.remove(strs[i])
        return list



s=Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
