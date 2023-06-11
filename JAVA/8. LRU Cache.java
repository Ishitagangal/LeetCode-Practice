class LRUCache {

    private class Node{
        Node prev;
        Node next;
        int key;
        int value;
        public Node(int key, int value)
        {
            this.key = key;
            this.next = null;
            this.prev = null;
            this.value = value;
        }
    }
    private int capacity;
    private HashMap<Integer, Node> hs = new HashMap<Integer, Node>();
    private Node head = new Node(-1,-1);
    private Node tail = new Node(-1,-1);
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        tail.prev = head;
        head.next = tail;
    }
    
    public int get(int key) {
        if(!hs.containsKey(key))
            return -1;
        Node current = hs.get(key);
        current.prev.next= current.next;
        current.next.prev = current.prev;
        
        move_to_tail(current);
        return hs.get(key).value;
    }
    
    public void put(int key, int value) {
        if(get(key) != -1)
        {
            hs.get(key).value = value;
            return;
        }
        if(hs.size() == capacity)
        {
            hs.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }
        Node insert = new Node(key,value);
        hs.put(key,insert);
        move_to_tail(insert);
    }
    private void move_to_tail(Node current)
    {
        current.prev = tail.prev;
        tail.prev = current;
        current.prev.next = current;
        current.next = tail;
    }

}
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */