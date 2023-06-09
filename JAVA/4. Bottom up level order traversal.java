/**
* Definition for a binary tree node.
* public class TreeNode {
*     int val;
*     TreeNode left;
*     TreeNode right;
*     TreeNode() {}
*     TreeNode(int val) { this.val = val; }
*     TreeNode(int val, TreeNode left, TreeNode right) {
*         this.val = val;
*         this.left = left;
*         this.right = right;
*     }
* }
*/
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> levels = new ArrayList<List<Integer>>();
        if(root == null) return levels;
    
        queue.add(root);
        int level = 0;
        while(!queue.isEmpty()){
            int level_size = queue.size();
            List<Integer> curr_level = new ArrayList<Integer>();
            for(int i=0; i<level_size; i++){
                TreeNode node = queue.remove();

                curr_level.add(node.val);
                if(node.left != null) queue.add(node.left);
                if(node.right!=null) queue.add(node.right);
            }
            levels.add(0, curr_level);
            level++;
        }
        return levels;
        
    }
}