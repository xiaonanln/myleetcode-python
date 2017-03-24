class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minvals = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.arr:
            self.arr.append(x)
            self.minvals.append(x)
            return

        assert self.minvals
        self.arr.append(x)
        minval = self.minvals[-1]
        if x <= minval:
            self.minvals.append(x)



    def pop(self):
        """
        :rtype: void
        """
        v = self.arr.pop(-1)
        if v == self.minvals[-1]:
            self.minvals.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minvals[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()