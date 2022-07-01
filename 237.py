class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.head=None
    def deleteNode(self, node):
        if self.head is None:
            return
        itr=self.head
        while itr:
            if itr.val==node:
                itr.next=itr.next.next
                break
            itr=itr.next

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data) + '-->' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

s=Solution()
print(s.deleteNode(print(5)))
