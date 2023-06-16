class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.head.next = self.head.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size +=1
    
    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.head.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -=1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.node_dict = dict() # key:Node
        self.freq_dict = collections.defaultdict(DLinkedList) # freq: linked list of nodes
        self.min_freq = 0
    
    def update(self,node):
        freq = node.freq
        self.freq_dict[freq].pop(node)
        if self.min_freq == freq and not self.freq_dict[freq]:
            self.min_freq +=1
        node.freq+=1
        freq = node.freq
        self.freq_dict[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.node_dict:
            return -1
        node = self.node_dict[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return

        if key in self.node_dict:
            node = self.node_dict[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq_dict[self.min_freq].pop()
                del self.node_dict[node.key]
                self.size -=1
            
            new_node = Node(key, value)
            self.node_dict[key] = new_node
            self.freq_dict[1].append(new_node)
            self.min_freq = 1
            self.size +=1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)