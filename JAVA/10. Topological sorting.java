// 2. find all recipes
class Node{
        int indegrees = 0;
        List<String> outnodes = new ArrayList<String>();

        public void add_indegree(){
            this.indegrees += 1;
        }
        public void append_nodes(String n){
            this.outnodes.add(n);
        }
    }
class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        HashMap<String, Node> graph = new HashMap<String, Node>();
        Queue<String> zeroDegrees = new LinkedList<String>();
        ArrayList<String> result = new ArrayList<String>();

        for(int i =0; i<recipes.length; i++){
            for(String ingredient: ingredients.get(i)){
                graph.putIfAbsent(recipes[i], new Node());
                graph.putIfAbsent(ingredient, new Node());
                graph.get(ingredient).append_nodes(recipes[i]);
                graph.get(recipes[i]).add_indegree();
            }
        }
        for(String supply:supplies){
            zeroDegrees.add(supply);
        }
        Set<String> recipesSet = new HashSet<>();
        recipesSet.addAll(Arrays.asList(recipes));

        while(!zeroDegrees.isEmpty()){
            String ingredient = zeroDegrees.poll();
            if(recipesSet.contains(ingredient)){
                result.add(ingredient);
            }
            if(!graph.containsKey(ingredient)) continue;
            for(String neighbor : graph.get(ingredient).outnodes){
                graph.get(neighbor).indegrees -=1;
                if(graph.get(neighbor).indegrees == 0)
                    zeroDegrees.add(neighbor);
            }
        }
        return result;
    }
}

// 1 course schedule, can finish
class Node{
        int indegrees = 0;
        List<Integer> outnodes = new ArrayList<Integer>();

        public void add_indegree(){
            this.indegrees += 1;
        }
        public void append_nodes(int n){
            this.outnodes.add(n);
        }
    }
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, Node> graph = new HashMap<Integer, Node>();
        Queue<Integer> zeroDegrees = new LinkedList<>();
        int totalDeps = 0;
        for(int i = 0; i<prerequisites.length; i++){
            int a = prerequisites[i][0];
            int b = prerequisites[i][1];
            graph.putIfAbsent(a, new Node());
            graph.putIfAbsent(b, new Node());
            graph.get(a).add_indegree();
            graph.get(b).append_nodes(a);
            totalDeps += 1;
        }
        for(Map.Entry<Integer, Node> entry: graph.entrySet()){
            if(entry.getValue().indegrees == 0){
                zeroDegrees.add(entry.getKey());
            }
        }
        int removedEdges = 0;
        while(!zeroDegrees.isEmpty()){
            int course = zeroDegrees.poll();
            for(int next: graph.get(course).outnodes){
                graph.get(next).indegrees -=1;
                removedEdges +=1;
                if(graph.get(next).indegrees ==0){
                    zeroDegrees.add(next);
                }
            }
        }
        return removedEdges == totalDeps;
    }
};

//3 Alien dictionary
class Solution {
    public String alienOrder(String[] words) {
        Map<Character, List<Character>> adjList = new HashMap<>();
        Map<Character, Integer> indegree = new HashMap<>();
        for(String word: words){
            for(char c: word.toCharArray()){
                indegree.put(c, 0);
                adjList.put(c, new ArrayList<>());
            }
        }

        for(int i =0; i< words.length - 1; i++){
            String word1 = words[i];
            String word2 = words[i+1];
            if(word1.length() > word2.length() && word1.startsWith(word2)) return "";
            for(int j =0; j<Math.min(word1.length(), word2.length()); j++){
                if(word1.charAt(j) != word2.charAt(j)){
                    adjList.get(word1.charAt(j)).add(word2.charAt(j));
                    indegree.put(word2.charAt(j), indegree.get(word2.charAt(j)) + 1);
                    break;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        Queue<Character> zeroDegree = new LinkedList<>();
        for(Character c: indegree.keySet()){
            if(indegree.get(c).equals(0)) zeroDegree.add(c);
        }

        while(!zeroDegree.isEmpty()){
            Character c = zeroDegree.poll();
            sb.append(c);
            for(Character d: adjList.get(c)){
                indegree.put(d, indegree.get(d) - 1);
                if(indegree.get(d).equals(0)) zeroDegree.add(d);
            }
        }
        if(sb.length() < indegree.size()) return "";
        return sb.toString();
        
    }
}