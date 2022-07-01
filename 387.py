from collections import deque
class Solution(object):
    def firstUniqChar(self, s):
        de=deque(s)
        for i in range(len(s)):
            a=de.popleft()
            if a not in de:
                return s.index(a)
            else:
                de.append(a)
        return -1

s=Solution()
print(s.firstUniqChar("loveleetcode"))
