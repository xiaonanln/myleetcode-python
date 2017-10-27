import collections

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = collections.deque()
        for t in tokens:
            if t == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 + v2)
#                 print("%d %s %d" % (v2, t, v1 ), list(stack))
            elif t == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2-v1)
#                 print("%d %s %d" % (v2, t, v1 ), list(stack))
            elif t == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 * v2)
#                 print("%d %s %d" % (v2, t, v1 ), list(stack))
            elif t == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                positive = (v1 >= 0 and v2 >= 0) or (v1 < 0 and v2 < 0)
                stack.append(abs(v2) / abs(v1) * (1 if positive else -1))
#                 print("%d %s %d" % (v2, t, v1 ), list(stack))
            elif isinstance(t, list):
                t = self.evalRPN(t)
                stack.append(t)
            else:
                t = int(t)
                stack.append(t)

        return stack.pop()

# print Solution().evalRPN( ["2", "1", "+", "3", "*"] )
# print Solution().evalRPN(["4", "13", "5", "/", "+"])
print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])