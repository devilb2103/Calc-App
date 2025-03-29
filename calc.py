import operator
# test
def calculator():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /) or 'q' to quit: ")
            if op.lower() == 'q':
                print("Exiting calculator.")
                break
            if op not in ops:
                print("Invalid operation. Try again.")
                continue
            num2 = float(input("Enter second number: "))
            result = ops[op](num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
