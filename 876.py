class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Solution(object):
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        itr=self.head

        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)


    def middleNode(self, head):
        self.head=None
        for data in head:
            self.insert_at_end(data)

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


if __name__ == '__main__':
    ll = Solution()
    ll.middleNode([1,2,3,4,5])
    ll.print()
