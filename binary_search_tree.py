from logging import root
from msilib.schema import Class
from turtle import left, right


class BinarySearchTree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data == self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)

    def in_order_traversal(self):
        elemnets=[]
        if self.left:
            pass

        return elemnets


def build_tree(elements):
    print("Building tree with these elements: ",elements)
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__=='__main__':
    numbers=build_tree([17, 4, 1, 20, 9, 23, 18, 34])