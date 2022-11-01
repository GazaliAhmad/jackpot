MAX_LINES = 3


def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines (max {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number. ")
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(f"Balance: ${balance}, Lines: {lines}")


main()

"""
https://youtu.be/th4OBktqK1I?t=760
"""
