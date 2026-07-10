class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        # foreach char
        for char in s:
            #if char is a cloisng bracket
            if char in pairs:
                #lets check if we saw an opening bracket before
                #its supposed to be in the stack
                #if the stack is empty now opening bracket was seend so it not valid

                if not stack or stack[-1] != pairs[char]:
                    #if the closing brackets doesnt match the opening onees return false
                        return False
                #its a match so we remove it from the stack
                stack.pop()
            else:
                #its an opening bracket add it to the stack
                stack.append(char)

        return not stack




        