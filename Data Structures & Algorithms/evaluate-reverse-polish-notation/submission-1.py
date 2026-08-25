class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {"+", "-", "*", "/"}
        stack = []
        
        for tok in tokens:
            if tok not in operators:
                stack.append(tok)
            elif tok == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif tok == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif tok == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a/b)
        return int(stack.pop())