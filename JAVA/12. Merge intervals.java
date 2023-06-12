//1. simple merge intervals
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
 class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        LinkedList<int[]> merged = new LinkedList<>();
        for (int[] interval : intervals) {
            // if the list of merged intervals is empty or if the current
            // interval does not overlap with the previous, simply append it.
            if (merged.isEmpty() || merged.getLast()[1] < interval[0]) {
                merged.add(interval);
            }
            // otherwise, there is overlap, so we merge the current and previous
            // intervals.
            else {
                merged.getLast()[1] = Math.max(merged.getLast()[1], interval[1]);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }
}
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
     
        List<Interval> result = new ArrayList<Interval>();
        if(intervals == null|| intervals.size() ==0)
            return result;
        
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval i1, Interval i2){
                if(i1.start != i2.start)
                    return i1.start-i2.start;
                else
                    return i1.end-i2.end;
           } 
        });
        
        Interval prev = intervals.get(0);
        for(int i =0; i<intervals.size(); i++){
            Interval curr = intervals.get(i);
            if(curr.start > prev.end){
                result.add(prev);
                prev = curr;
            }
            else{
                Interval merged = new Interval(prev.start, Math.max(prev.end, curr.end));
                prev = merged;
            }
                
        }
        result.add(prev);
        return result;
    }
}