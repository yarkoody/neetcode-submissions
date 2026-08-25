class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {"+", "-", "*", "/"}
        stack = []
        
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            elif tok == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif tok == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif tok == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
        return stack.pop()