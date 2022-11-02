import random

MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

symbol_multiplier = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_for_win(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_lines(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_ct in symbols.items():
        for _ in range(symbol_ct):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_lines(columns):
    for row in range(len(columns[0])):
        line_number = int(row) + 1
        print(f"Line {str(line_number)}", end=": | ", flush=True)
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" | ")

        print()


def deposit():
    while True:
        amount = input("\nEnter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("\nAmount must be greater than 0")
        else:
            print("\nAmount must be a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"\nEnter number of lines (max {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("\nEnter a valid number of lines")
        else:
            print("\nPlease enter a number. ")
    return lines


def get_bet_amount():
    while True:
        bet = input(
            f"\nEnter bet amount (min ${MIN_BET}, max ${MAX_BET}) on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"\nBet must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("\nPlease enter a number. ")
    return bet


def play(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = lines * bet

        if total_bet > balance:
            print(
                f"\nYou do not have enough money to make this bet, your balance is ${balance}")
        else:
            break

    print(f"Your bet: ${bet} on {lines} lines. Total bet is ${total_bet}\n")

    slots = get_lines(ROWS, COLS, symbol_count)
    print_lines(slots)

    winnings, winning_lines = check_for_win(slots, lines, bet, symbol_multiplier)
    print(f"\nYou won ${winnings}")
    print(f"\nYou won on lines:", *winning_lines, sep=" ")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"\nYour balance is ${balance}")
        choice = input("\nPress any to play or q to quit: ")
        if choice == "q":
            break
        balance += play(balance)
        if balance <= 0:
            print("\nYou are out of money. Game over.")
            break

    print(f"\nYour final balance is ${balance}\n")


main()

"""
Player can choose the line number and same bet amount
Player can choose the line number with different bet amounts
Winnings can be diagonal if player chose all 3 lines
Winnings with two symbols
"""
