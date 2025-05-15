import math

def calculator():
    print("Simple calculator")
    while(True):
        try:
            command = input("Two numbers or (-1) to exit: ")
            if command == '-1':
                print("exit()")
                break
            x, y = map(float, command.split())
            add = lambda x, y : x+ y
            sub = lambda x, y : math.fabs(x - y)
            ans = 0
            operation = input("enter operation: +, -, *, / : ")
            def calculate(operation):
                match operation:
                    case '+':
                        ans = add(x, y)
                    case '-':
                        ans = sub(x, y)
                    case '*':
                        ans = x * y
                    case '/':
                        ans = x / y
                return ans
            print("result:", calculate(operation))
        except ValueError:
            print("Invalid input")
        except ZeroDivisionError:
            print("cannot divide by 0")

calculator()