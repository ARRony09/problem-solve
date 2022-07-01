from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        anagram,nagaram
        """
        """list=[]
        for i in s:
            list.append(i)

        for i in t:
            if i in list:
                list.remove(i)
        if len(list)==0:
            return True
        else:
            return False"""

        if Counter(s)==Counter(t):
            return True
        else:
            return False


s=Solution()
print(s.isAnagram("ab","a"))
