import ast

def evaluate_expression(expression):
    try:
        parsed_expr = ast.parse(expression, mode='eval')
        result = eval(compile(parsed_expr, filename='<ast>', mode='eval'))
        return result
    except SyntaxError:
        return "Syntax Error: Invalid expression"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return "Error: " + str(e)

print("Welcome to Ken's Arithmetic Calculator. Type 'quit' to exit.")

while True:
    user_input = input("Enter an arithmetic expression: ")

    if user_input.lower() == "quit":
        break
    else:
        result = evaluate_expression(user_input)
        print("Result:", result)
