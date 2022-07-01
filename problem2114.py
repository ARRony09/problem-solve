"""class Solution(object):
    def mostWordsFound(self, sentences):
        :type sentences: List[str]
        :rtype: int

        list=[]
        for sentence in sentences:
            a=len(sentence.split())
            list.append(a)
        return max(list)



s=Solution()
print(s.mostWordsFound(["please wait", "continue to fight", "continue to win"]))

"""
'''
class Solution(object):
    def interpret(self, command):
        list=[]
        for i in range(len(command)):
            if command[i]=='G':
                list.append('G')
            elif '('==command[i]:
                if ')'==command[i+1]:
                    list.append('o')
                elif 'a' == command[i+1]:
                    list.append('al')


        s="".join(list)
        print(list)
        return s

s=Solution()
print(s.interpret("(al)G(al)()()G"))'''

class Solution:
    def sortSentence(self, s):
        new_s=s.split()
        new_s.sort(key=lambda x:x[-1])
        list=[]
        for i in new_s:
            list.append(i[:-1])
        a=' '.join(list)
        return a

s=Solution()
print(s.sortSentence("Myself2 Me1 I4 and3"))
