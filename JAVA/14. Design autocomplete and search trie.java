import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class AutocompleteSystem{
class TrieNode {
    Map<Character, TrieNode> children;
    Map<String, Integer> counts;
    boolean isWord;
    public TrieNode() {
        children = new HashMap<Character, TrieNode>();
        counts = new HashMap<String, Integer>();
        isWord = false;
    }
}
TrieNode root;
String prefix;


public AutocompleteSystem(String[] sentences, int[] times) {
    root = new TrieNode();
    prefix = "";
    
    for (int i = 0; i < sentences.length; i++) {
        add(sentences[i], times[i]);
    }
}

private void add(String s, int count) {
    TrieNode curr = root;
    for (char c : s.toCharArray()) {
        TrieNode next = curr.children.get(c);
        if (next == null) {
            next = new TrieNode();
            curr.children.put(c, next);
        }
        curr = next;
        curr.counts.put(s, curr.counts.getOrDefault(s, 0) + count);
    }
    curr.isWord = true;
}

public List<String> input(char c) {
    if (c == '#') {
        add(prefix, 1);
        prefix = "";
        return new ArrayList<String>();
    }
    
    prefix = prefix + c;
    TrieNode curr = root;
    for (char cc : prefix.toCharArray()) {
        TrieNode next = curr.children.get(cc);
        if (next == null) {
            return new ArrayList<String>();
        }
        curr = next;
    }
    
    PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>((a, b) -> (a.getValue() == b.getValue() ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue()));
    pq.addAll(curr.counts.entrySet());
    
    List<String> res = new ArrayList<String>();
    
    int k = 3;
    while(!pq.isEmpty() && k > 0) {
        res.add((String) pq.poll().getKey());
        k--;
    }
    // min heap
    PriorityQueue<Map.Entry<String, Integer>> minQueue = new PriorityQueue<>((a,b) -> (a.getValue() == b.getValue()? b.getKey().compareTo(a.getKey()): a.getValue() - b.getValue()));
    for(Map.Entry<String, Integer> e: curr.counts.entrySet()){
        minQueue.offer(e);
        if(minQueue.size() > k){
            minQueue.poll();
        }
    }
    List<String> res2 = new ArrayList<String>();
    while(!minQueue.isEmpty()){
        res2.add(0, minQueue.poll().getKey());
    }
    return res;
}
}