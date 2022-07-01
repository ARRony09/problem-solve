from collections import deque
import numbers
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
    
    def front(self):
        return self.buffer[-1]
        

def produce_binary(num):
    pq=Queue()
    pq.enqueue("1")

    for i in range(num):
        front=pq.front()
        print("  ",front)
        pq.enqueue(front+"0")
        pq.enqueue(front+"1")
        pq.dequeue()
    #pq.enqueue(num%2)

if __name__=='__main__':
    produce_binary(10)
