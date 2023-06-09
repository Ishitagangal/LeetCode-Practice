class Solution {
    public ArrayList find_neighbors(String node){
        int[] dir = {-1, 1};
        ArrayList<String> neighbors = new ArrayList<String>();
        for(int i =0; i<4; i++){
            int x = (node.charAt(i) - '0');
            for(int d : dir){
                int y = (x + d +10) % 10;
                String next_num = node.substring(0, i) + (y+"") + node.substring(i+1);
                neighbors.add(next_num);
            }
        }
        return neighbors;
    }
    public int openLock(String[] deadends, String target) {
        Set<String> deadend = new HashSet();
        for(String d: deadends) deadend.add(d);

        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        Set<String> seen = new HashSet();
        seen.add("0000");
        int depth = 0;

        for(int steps = 0; !queue.isEmpty(); steps++){
            for(int i = queue.size(); i > 0; i--){
                String node = queue.poll();
                if(node.equals(target)) return steps;
                if(deadend.contains(node)) continue;
                ArrayList<String> neighbors = find_neighbors(node);
                for(String neighbor : neighbors){
                    if(!seen.contains(neighbor)){
                        seen.add(neighbor);
                        queue.offer(neighbor);
                    }
                }
            }
        }
        return -1;
    }
}