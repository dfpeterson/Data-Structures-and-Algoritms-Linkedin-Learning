from collections import deque

#lists are not as efficient for queues for insertions and deletions
#deque is optimized
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.append(item) #adds to right side

    def dequeue(self):
        return self.items.popleft() #behaves like pop[0] but faster
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0] #wants the front
    
    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue('Agent Q')
    q.enqueue('Agent M')
    q.enqueue('007')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    print(q)