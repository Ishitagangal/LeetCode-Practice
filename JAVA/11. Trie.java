// 1. Implement simple trie
public class TrieNode {
    char ch;
    HashMap<Character, TrieNode> children;
    boolean isEnd;

    public TrieNode(char ch){
        this.ch = ch;
        this.children = new HashMap<Character, TrieNode> ();
        this.isEnd = false;
    }
}
class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode(' ');
    }
    
    public void insert(String word) {
        TrieNode node = this.root;
        for(Character ch: word.toCharArray()){
            if(node.children.containsKey(ch))
                node = node.children.get(ch);
            else {
                TrieNode new_node = new TrieNode(ch);
                node.children.put(ch, new_node);
                node = new_node;
            }
        }
        node.isEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode node = this.root;
        for(Character ch: word.toCharArray()){
            if(!node.children.containsKey(ch)) return false;
            node = node.children.get(ch);
        }
        return node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = this.root;
        for(Character ch: prefix.toCharArray()){
             if(!node.children.containsKey(ch)) return false;
            node = node.children.get(ch);
        }
        return true;
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

 // 2. Design file system
 class FileSystem {
    class TrieNode{
        String name;
        int val = -1;
        HashMap<String, TrieNode> children = new HashMap<>();

        public TrieNode(String name){
            this.name = name;
        }
    }
    TrieNode root;

    public FileSystem() {
        this.root = new TrieNode("");
        
    }
    
    public boolean createPath(String path, int value) {
        String[] components = path.split("/");
        TrieNode node = this.root;
        // 0th index is "" when "/a/b/c" is split over "/"
        for(int i = 1; i< components.length; i++){
            String curr = components[i];
            if(!node.children.containsKey(curr)){
                if(i == components.length - 1)
                    node.children.put(curr, new TrieNode(curr));
                else
                    return false;
            }
            node = node.children.get(curr);
        }
        if(node.val != -1)
            return false;
        node.val = value;
        return true;
    }
    
    public int get(String path) {
        String[] comps = path.split("/");
        TrieNode node = this.root;

        for(int i = 1; i< comps.length; i++){
            String curr = comps[i];
            if(!node.children.containsKey(curr)) return -1;
            node = node.children.get(curr);
        }
        return node.val;
        
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * boolean param_1 = obj.createPath(path,value);
 * int param_2 = obj.get(path);
 */