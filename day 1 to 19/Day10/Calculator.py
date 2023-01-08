from art import logo


# calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


print(logo)

# ask for input
num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
symbol = (input("Pick one operation. "))
if symbol not in operations:
    exit("Program exiting because input is Not a valid symbol")
num2 = float(input("What's the second number?: "))

# print operations and get user input
calculation = operations[symbol]
answer = calculation(num1, num2)
output = f"{num1} {symbol} {num2} = {answer}"
print(output)

end_calculation = False
should_continue = str(input(f"you answer is {answer}, Do you want to perform more operations? enter 'Y for Yes and "
                            f"'N' for No   ")).lower()

second_answer = answer  # prevent answer loss incase wrong operation is in input.
# looping it.
if should_continue == "y":
    while not end_calculation:
        num1 = answer
        # pick options
        for symbol in operations:
            print(symbol)
        symbol = (input("Pick one operation. "))
        if symbol not in operations:
            print(f"You final answer is {second_answer}")
            exit("Program exiting because input is Not a valid symbol")
        num2 = float(input("What's the second number?: "))
        calculation = operations[symbol]
        second_answer = answer = calculation(num1, num2)
        output = f"{num1} {symbol} {num2} = {second_answer}"
        print(output)
        should_continue = str(
            input(f"Your final answer is {second_answer}, Do you want to perform more operations? enter 'Y for Yes and "
                  f"'N' for No  ")).lower()
        if should_continue == "y":
            end_calculation = False
        elif should_continue == "solution":
            end_calculation = True
    else:
        end_calculation = True
