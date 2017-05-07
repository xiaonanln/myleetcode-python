import java.util.HashMap;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        HashMap<Integer, Integer> inorderMap = new HashMap<Integer, Integer>(inorder.length);
        for (int i = 0; i < inorder.length; i++) inorderMap.put(inorder[i], i);
        return buildTreeHelper(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1, inorderMap);
    }

    private TreeNode buildTreeHelper(int[] preorder, int pi, int pj, int[] inorder, int ii, int ij, HashMap<Integer, Integer> inorderMap) {
        if (pi > pj) return null;
        int rootval = preorder[pi];
        int m = inorderMap.get(rootval);
        TreeNode root = new TreeNode(rootval);
        root.left = buildTreeHelper(preorder, pi+1, pi+m-ii, inorder, ii, m-1, inorderMap);
        root.right = buildTreeHelper(preorder, pi+m-ii+1, pj, inorder, m+1, ij, inorderMap);
        return root ;
    }
}