from collections import defaultdict
class Node(object):
    def __init__(self):
        self.key_set = set([])
        self.prev, self.next = None, None 

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)        

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None
    
    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList(object):
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node
        return

    def insert_after(self, x): # creates a new node betweem x and x.next, returns this
        node, temp = Node(), x.next
        x.next, node.prev = node, x
        node.next, temp.prev = temp, node
        return node
    
    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.next = x.next
        x.next.prev = prev_node
        return

    def get_head(self):
        return self.head_node.next
    
    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node
    
class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleLinkedList()
        self.key_counter = defaultdict(int) # key:freq
        self.node_freq = {0:self.dll.get_sentinel_head()} # freq : Node, update this and remove from here whenever frequency changes

    def remove_key_from_previous_frequency(self, freq, key):
        node = self.node_freq[freq]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(freq)
        return

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.key_counter[key] += 1
        current_frequency, previous_frequency = self.key_counter[key], self.key_counter[key]-1
        if current_frequency not in self.node_freq:
            # No need to test if pf = 0 since frequency zero points to sentinel node
            # create new node and insert it after the previous frequency node
            self.node_freq[current_frequency] = self.dll.insert_after(self.node_freq[previous_frequency])
        # add key to current frequency node after creating it
        self.node_freq[current_frequency].add_key(key)
        if previous_frequency > 0: # remove this key from old frequency node since we moved the key over to the new frequency
            self.remove_key_from_previous_frequency(previous_frequency, key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_counter:
            self.key_counter[key] -= 1
            current_frequency, previous_frequency = self.key_counter[key], self.key_counter[key]+1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if current_frequency != 0:
                if current_frequency not in self.node_freq:
                    self.node_freq[current_frequency] = self.dll.insert_before(self.node_freq[previous_frequency])
                self.node_freq[current_frequency].add_key(key)
            self.remove_key_from_previous_frequency(previous_frequency, key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() > 0 else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()