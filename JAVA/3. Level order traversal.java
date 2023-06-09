//Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> levels = new ArrayList<List<Integer>>();
        if(root == null) return levels;
    
        queue.add(root);
        int level = 0;
        while(!queue.isEmpty()){
            levels.add(new ArrayList<Integer>());
            int level_size = queue.size();
            for(int i=0; i<level_size; i++){
                TreeNode node = queue.remove();

                levels.get(level).add(node.val);
                if(node.left != null) queue.add(node.left);
                if(node.right!=null) queue.add(node.right);
            }
            level++;
        }
        return levels;

        
    }
}

// Zig zag level order traversal
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        List<List<Integer>> res = new ArrayList<>();
        if(root == null)
            return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        
        boolean flag = false;
        while(!q.isEmpty())
        {
            List<Integer> level = new ArrayList<>();
            int size = q.size();
            
            for(int i= 0; i<size; i++)
            {
                TreeNode node = q.poll();
                if(flag)
                    level.add(0, node.val);
                else
                    level.add(node.val);
                if(node.left!=null)
                    q.add(node.left);
                if(node.right!=null)
                    q.add(node.right);
            }
            res.add(level);
            flag = !flag;
        }
        return res;
    }
}