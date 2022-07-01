
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        for i in list2:
            list1.append(i)
        list1.sort()
        return list1

s=Solution()
print(s.mergeTwoLists([1,2,4],[1,3,4]))
