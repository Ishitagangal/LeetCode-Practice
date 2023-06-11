class Solution {
    int maxTime = Integer.MIN_VALUE;
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        ArrayList<ArrayList<Integer>> subordinates = new ArrayList<ArrayList<Integer>>(n);
        for(int i = 0; i<n; i++) subordinates.add(new ArrayList<Integer>());

        for(int i =0; i <n; i++){
            if(manager[i] != -1) subordinates.get(manager[i]).add(i);
        }

        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.add(new Pair<>(headID, 0));

        while(!queue.isEmpty()){
            Pair<Integer, Integer> empPair = queue.poll();
            int currManager = empPair.getKey();
            int time = empPair.getValue();
            maxTime = Math.max(maxTime, time);

            for(int emp:subordinates.get(currManager)){
                queue.add(new Pair<>(emp, time+informTime[currManager]));
            }
        }
        return maxTime;


    }
}