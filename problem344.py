"""class Solution:
    def reverseString(self, s):
        #inplace algorithm
        n=len(s)
        for i in range(0,int(n/2)):
            s[i],s[n-i-1]=s[n-i-1],s[i]

        return s"""

class Solution:
    def commonChars(self, words):
        if len(words)==1:
            return list(words)
        first_word=words[0]
        words=[list(i) for i in words[1:]]
        list1=[]
        count=0
        for i in first_word:
            for j in range(len(words)):
                if i in words[j]:
                    words[j].remove(i)
                    count+=1
                if count==len(words):
                    list1.append(i)
            count=0
        return list1

s=Solution()
print(s.commonChars(["bella"]))
