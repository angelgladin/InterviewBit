class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        parenthe_stack = []
        brackets_stack = []
        curlybra_stack = []
        for x in A:
            if x == '(':
                parenthe_stack.append(x)
            elif x == ')':
                if parenthe_stack:
                    parenthe_stack.pop()
            elif x == '[':
                brackets_stack.append(x)
            elif x == ']':
                if brackets_stack:
                    brackets_stack.pop()
            elif x == '{':
                curlybra_stack.append(x)
            elif x == '}':
                if curlybra_stack:
                    curlybra_stack.pop()
        if parenthe_stack or brackets_stack or curlybra_stack:
            return 0
        else:
            return 1
