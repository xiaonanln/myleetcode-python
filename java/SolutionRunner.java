import java.util.List;

/**
 * Created by Administrator on 2017/5/7.
 */
public class SolutionRunner {
    public static void main(String[] args) {
        List<String> result = new Solution().fullJustify(new String[]{"What","must","be","shall","be."}, 12);
        for (String line: result) {
            System.err.printf("\"%s\"\n", line);
        }
    }
}
