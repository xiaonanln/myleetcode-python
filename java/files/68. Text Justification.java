import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution {
    class LineInfo {
        int wordCount;
        int totalLength;
        int getMaxStringLengthToAdd(int maxWidth) {
            return maxWidth - (totalLength + wordCount);
        }
    }
    public List<String> fullJustify(String[] words, int maxWidth) {
        Queue<LineInfo> lineInfos = new LinkedList<LineInfo>();
        LineInfo lastLineInfo = null;
        for (String w : words) {
            int sz = w.length();
            if (lastLineInfo == null || lastLineInfo.getMaxStringLengthToAdd(maxWidth) < sz) {
                lastLineInfo = new LineInfo();
                lineInfos.add(lastLineInfo);
            }
            lastLineInfo.wordCount += 1;
            lastLineInfo.totalLength += sz;
        }

        int wi = 0;
        List<String> res = new LinkedList<String>();
        int lii = -1;
        for (LineInfo lineInfo : lineInfos) {
            lii += 1;
            boolean isLastLine = (lii == lineInfos.size() - 1);

            StringBuilder s = new StringBuilder(maxWidth);
            int leftSpaceCount = maxWidth - lineInfo.totalLength;
            int leftSepCount = lineInfo.wordCount - 1;
            assert(leftSpaceCount >= leftSepCount);
            for (int i = 0; i < lineInfo.wordCount; i++) {
                String word = words[wi];

                if (i != 0) {
                    if (!isLastLine) {
                        int spaceCount = leftSpaceCount / leftSepCount;
                        if (leftSpaceCount % leftSepCount != 0) spaceCount += 1;
                        leftSpaceCount -= spaceCount;

                        for (; spaceCount>0; spaceCount -= 1) s.append(' ');

                    } else {
                        s.append(' ');
                        leftSpaceCount -= 1;
                    }
                    leftSepCount -= 1;
                }

                s.append(word);
                wi += 1;
            }
            for (int i = 0; i < leftSpaceCount; i++ ) {
                s.append(' ');
            }
            res.add(s.toString());
        }
        return res;
    }
}