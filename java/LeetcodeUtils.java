import static java.lang.Math.max;

/**
 * Created by Administrator on 2017/5/7.
 */
public class LeetcodeUtils {
    public static void printTree(TreeNode root) {
        printTreeHelper(root, 0);
    }

    private static void printTreeHelper(TreeNode root, int indent) {
        if (root != null) printTreeHelper(root.right, indent+1);

        for (int i = 0; i < indent;i++) {
            System.out.print('\t');
        }
        if (root != null) {
            System.out.println(root.val);
        } else {
            System.out.println("nil");
        }

        if (root != null) printTreeHelper(root.left, indent+1);
    }

    public static int treeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + max(treeDepth(root.left), treeDepth(root.right));
    }

}
