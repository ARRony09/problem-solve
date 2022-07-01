"""stock_price=[]
stock_price.insert(0,10)
stock_price.insert(0,11)
stock_price.insert(0,12)
print(stock_price)
print(stock_price.pop())
print(stock_price.pop())"""

"""from collections import deque
q=deque()
q.appendleft(7)
q.appendleft(8)
q.appendleft(9)
print(q)
print(q.pop())"""


"""
class Queue:

    def __init__(self):
        self.buffer=deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

pq=Queue()

pq.enqueue(10)
pq.enqueue(10.1)
pq.enqueue(10.2)
pq.enqueue(10.3)
print(pq)
print(pq.dequeue())
print(pq.dequeue())
print(pq.is_empty())
print(pq.size())"""

"""
from collections import deque
import threading
import time

class Queue:

    def __init__(self):
        self.buffer=deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

pq=Queue()

def place_order(orders):
    for order in orders:
        print("Placing order for :",order)
        pq.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
        order=pq.dequeue()
        print("Serving order: ",order)
        time.sleep(2)


if __name__=='__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=place_order,args=(orders,))
    t2=threading.Thread(target=serve_order)

    t1.start()
    t2.start()"""

from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        students=deque(students)
        sandwiches=deque(sandwiches)
        while True:
            mismatch=0
            n=len(students)
            for i in range(n):
                a=students.popleft()
                if a == sandwiches[0]:
                    sandwiches.popleft()
                else:
                    students.append(a)
                    mismatch+=1
            if mismatch==n:
                break
        return len(students)
                

s=Solution()
print(s.countStudents([1,1,0,0],[0,1,0,1]))
            

