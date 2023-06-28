class MyCircularQueue:

    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.t = [0]*k
        self.front = self.rear = -1
        
    def enQueue(self, value):
        if self.size == self.max_size: return False
        else:
            if self.rear == -1:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear + 1)%self.max_size
            self.t[self.rear] = value
            self.size += 1
            return True
        
    def deQueue(self):
        if self.size == 0: return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1)%self.max_size
        self.size -= 1
        return True
        

    def Front(self):
        return self.t[self.front] if self.size != 0 else -1

    def Rear(self):
        return self.t[self.rear] if self.size != 0 else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size



class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.tail.value
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity