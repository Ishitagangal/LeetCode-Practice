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

    public boolean isValidSequenceHelper(TreeNode node, int[] arr, int len, int index){
        if(index == len || node == null) return false;

        if(node.left == null && node.right==null){
            if(index == len -1 && node.val == arr[index]) return true;
            return false;
        }
        return index < len && arr[index] == node.val && (isValidSequenceHelper(node.left, arr, len, index + 1) || isValidSequenceHelper(node.right, arr, len, index+1)); 
    }
    public boolean isValidSequence(TreeNode root, int[] arr) {
        if(root == null) return false;

        return isValidSequenceHelper(root, arr, arr.length, 0);
    }
}

class Solution {
    int root_to_leaf = 0;

    public void preorder(TreeNode node, int curr){
        if(node != null){
            curr = curr*10 + node.val;
            if(node.left == null && node.right == null) root_to_leaf += curr;

            preorder(node.left, curr);
            preorder(node.right, curr);
        }
    }
    public int sumNumbers(TreeNode root) {
        preorder(root, 0);
        return root_to_leaf;
    }
}