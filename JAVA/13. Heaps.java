// 1. Merge k sorted lists

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0) return null;
        if(lists.length == 1) return lists[0];

        ListNode head = new ListNode(-1);
        ListNode prev = head;
        // min pq, min heap
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> {return a.val - b.val;});
        for(int i =0; i<lists.length; i++){
            if(lists[i] != null)
                pq.offer(lists[i]);
        }

        while(pq.size() > 0){
            ListNode curr = pq.poll();
            prev.next = curr;
            prev = prev.next;
            if(curr.next != null)
                pq.offer(curr.next);
        }
        return head.next; 
    }
}

//2. top K most frequent elements
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if(k == nums.length) return nums;

        HashMap<Integer, Integer> frequencyMap = new HashMap<>();
        for(int n : nums){
            frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
        }

        Queue<Integer> minHeap = new PriorityQueue<>((n1, n2) -> frequencyMap.get(n1) - frequencyMap.get(n2));
        for(int num : frequencyMap.keySet()){
            minHeap.offer(num);
            if(minHeap.size() > k)
                minHeap.poll();
        }
        int[] result = new int[k];
        for(int i = k - 1; i >=0; i--){
            result[i] = minHeap.poll();
        }
        return result;
    }
}

//3. Find median in data stream
class MedianFinder {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public MedianFinder() {
    }
    
    public void addNum(int num) {
        maxHeap.offer(num);
        minHeap.offer(maxHeap.poll());
        if(maxHeap.size() < minHeap.size())
            maxHeap.offer(minHeap.poll());
    }
    
    public double findMedian() {
        if(maxHeap.size() > minHeap.size())
            return maxHeap.peek();
        else return (maxHeap.peek() + minHeap.peek()) /2.0;
        
    }
}

//4 Maximize capital
class Solution4 {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<Pair<Integer,Integer>> minCap = new PriorityQueue<>((a,b) -> (a.getKey() - b.getKey()));
        PriorityQueue<Integer> maxProfit = new PriorityQueue<>(Collections.reverseOrder());

        for(int i =0; i< capital.length; i++){
            minCap.add(new Pair<>(capital[i], i));
        }
        int available = w;
        for(int i=0; i<k; i++){
            while(!minCap.isEmpty() && minCap.peek().getKey() <= available){
                int index = minCap.poll().getValue();
                maxProfit.add(profits[index]);
            }
            if(maxProfit.isEmpty()) break;
            available += maxProfit.poll();
        }
        return available;
    }
}

// 5.1 minimum meeting rooms
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        
        PriorityQueue<Integer> q = new PriorityQueue<Integer>(
                                                intervals.length,
                                                new Comparator<Integer>() {
                                                public int compare(Integer a, Integer b) {
                                                    return a - b;
                                                }
                                                });
        int count = 1;
        if(intervals.length == 0) return 0;

        Arrays.sort(intervals, new Comparator<int[]>(){
            public int compare(int[] a, int[] b){ return a[0] - b[0];}
        });
        q.offer(intervals[0][1]);
        for(int i = 1; i<intervals.length; i++)
        {
            if(intervals[i][0] <= q.peek())
                count++;
            else
                q.poll();
            q.offer(intervals[i][1]);
        }
        return count;
    }
}
    
//6 most booked meeting room
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (m1, m2) -> Integer.compare(m1[0], m2[0]));
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] == b[0]? a[1] - b[1] : a[0] - b[0]);
        int[] result = new int[n]; // keep track of num meetings in ith room
        PriorityQueue<Integer> available = new PriorityQueue<Integer>();
		for (int i = 0; i < n; i++)
			available.add(i);
        for(int[] meeting: meetings){
            while(!minHeap.isEmpty() && minHeap.peek()[0] <= meeting[0]){
                available.add(minHeap.poll()[1]);
            }
            int room = -1;
            int[] heapVal = new int[2];
            if(!available.isEmpty()){
                room = available.poll();
                minHeap.offer(new int[] {meeting[1], room });
            }
            else{
                heapVal = minHeap.poll();
                room = heapVal[1];
                minHeap.offer(new int[] {heapVal[0] + meeting[1] - meeting[0], heapVal[1]});
            }
            result[room] +=1;
        }
        int maxIndex = 0;
        for(int r =0; r<result.length; r++){
            if(result[r] > result[maxIndex])
                maxIndex = r;
        }
        return maxIndex;
    }
}
