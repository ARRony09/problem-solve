class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        list=[]
        for i in magazine:
            list.append(i)
        for i in ransomNote:
            if i in list:
                list.remove(i)
            elif i not in list:
                return False
        return True
        """if ransomNote in magazine:
            return True
        elif ransomNote in magazine[::-1]:
            return True
        else:
            return False
            "fffbfg"
"effjfggbffjdgbjjhhdegh"
            """

s=Solution()
print(s.canConstruct('fffbfg','effjfggbffjdgbjjhhdegh'))
