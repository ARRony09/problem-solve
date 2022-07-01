class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        list1=[]
        list2=[]
        list3=[]

        for i in firstWord:
            s=str(ord(i)-97)
            list1.append(s)
        newlist=''
        first=int(newlist.join(list1))

        for i in secondWord:
            s=str(ord(i)-97)
            list2.append(s)
        newlist=''
        second=int(newlist.join(list2))


        for i in targetWord:
            s=str(ord(i)-97)
            list3.append(s)
        newlist=''
        target=int(newlist.join(list3))
        sum=first+second

        if sum==target:
            return True
        else:
            return False

s=Solution()
print(s.isSumEqual("aaa",'a','aaaa'))
