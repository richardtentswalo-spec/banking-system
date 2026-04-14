# Basic banking system

def display_menu():
    print('\n-----Menu------')
    print('1. Deposit money')
    print('2. Withdraw money')
    print('3. Check balance')
    print('4. Exit')


def deposit(balance, amount):
    balance += amount
    return balance


def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f'You have withdrawn R{amount}')
    else:
        print('INSUFFICIENT FUNDS')
    return balance


def main():
    balance = 0
    choice = 0

    while choice != 4:
        display_menu()
        choice = int(input('Choose your transaction: '))

        if choice == 1:
            amount = float(input('Deposit: '))
            balance = deposit(balance, amount)
            print(f'You have deposited R{amount}')
            print(f'Your balance is R{balance}')

        elif choice == 2:
            amount = float(input('Withdraw: '))
            balance = withdraw(balance, amount)
            print(f'Your balance is R{balance}')

        elif choice == 3:
            print(f'Your balance is R{balance}')

        elif choice == 4:
            print('Exiting the program')

        else:
            print('Invalid choice entered. Choose 1-4')


main()
