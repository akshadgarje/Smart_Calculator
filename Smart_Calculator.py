import re
from collections import deque

OPERATORS = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}

variables = {}
while True:
    input_ = input()
    if input_ == "":
        pass
    elif input_ == "/exit":
        print("Bye!")
        break
    elif input_ == "/help":
        print("Integer calculator (+-*/^)")
    elif input_[0] == "/":
        print("Unknown command")
    elif "=" in input_:
        if input_.count("=") == 1:
            name, value = input_.replace(" ", "").split("=")
            if value in variables:
                value = str(variables[value])
            if name.isalpha() and value.isnumeric():
                variables[name] = int(value)
            elif not name.isalpha():
                print("Invalid identifier")
            elif value.isalpha():
                print("Unknown variable")
            else:
                print("Invalid assignment")
        else:
            print("Invalid assignment")
    else:
        result = []
        stack = deque()
        num = True
        input_ = input_.replace("(", "( ")
        input_ = input_.replace(")", " )")
        for x in input_.split():
            if re.match(r"[+-]*$", x):
                sgn = (-1) ** x.count("-")
                if sgn == 1:
                    x = "+"
                elif sgn == -1:
                    x = "-"
            if x.isalnum():
                result.append(x)
            elif x in OPERATORS:
                if len(stack) == 0 or stack[-1] == "(" \
                or OPERATORS[x] > OPERATORS[stack[-1]]:
                    stack.append(x)
                else:
                    while len(stack) > 0 \
                    and (stack[-1] != "(" or OPERATORS[x] <= OPERATORS[stack[-1]]):
                        result.append(stack.pop())
                    stack.append(x)
            elif x == "(":
                stack.append(x)
            elif x == ")":
                while stack[-1] != "(":
                    result.append(stack.pop())
                    if not stack:
                        print("Invalid expression")
                        break
                else:
                    stack.pop()
            else:
                print("Invalid expression")
                break
        else:
            while stack:
                if "(" in stack:
                    print("Invalid expression")
                    break
                result.append(stack.pop())

            else:
                for x in result:
                    if x.isnumeric():
                        stack.append(int(x))
                    elif x.isalpha():
                        if x in variables:
                            stack.append(variables[x])
                        else:
                            print("Unknown variable")
                            break
                    elif x in OPERATORS:
                        n1 = stack.pop()
                        n2 = stack.pop()
                        if x == "+":
                            stack.append(n2 + n1)
                        elif x == "-":
                            stack.append(n2 - n1)
                        elif x == "*":
                            stack.append(n2 * n1)
                        elif x == "/":
                            stack.append(n2 // n1)
                        elif x == "^":
                            stack.append(n2 ** n1)
                else:
                    print(stack.pop())
