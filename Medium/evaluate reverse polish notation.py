class Solution(object):
    def evalRPN(self, tokens):
        num1 = 0
        num2 = 0
        sum = 0

        while len(tokens) > 1:
            for i, char in enumerate(tokens):
                if char in "+-*/":
                    num2 = int(tokens[i-1])
                    num1 = int(tokens[i-2])

                    if char == "+":
                        sum = num1 + num2
                    elif char == "-":
                        sum = num1 - num2
                    elif char == "*":
                        sum = num1 * num2
                    else:
                        sum = int(num1 / num2)

           
                    tokens[i-2:i+1] = [str(sum)]
                    break

        return int(tokens[0])