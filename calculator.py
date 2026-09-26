memory = None


def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("please enter other number then zero")
            return None
        else:
            return first_number / second_number
    else:
        print("please enter a correct number")
        return None


while True:
    try:
        first_number = input(
            'Please enter the first number or press m if you want to use memory: '
        )

        if first_number.lower() == "m":
            if memory is None:
                print('No memory saved ')
                continue
            first_number = memory
        else:
            first_number = float(first_number)

    except ValueError:
        print("Thats not a valid number")
        continue

    try:
        second_number = float(input('Please enter the second number: '))
    except ValueError:
        print("thats not a valid number")
        continue

    operation = input("which operation would you like to perform ")

    result = calculate(first_number, second_number, operation)

    if result is not None:
        print(result)
        memory = result

    repeat = input("do you want to keep using the calculator?")
    if repeat.lower() == "n":
        break
