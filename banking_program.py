def show_balance(balance):
    print(f"Your current balance is: {balance}")


def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        return amount
    else:
        print("Deposit amount must be positive!")
        return 0


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        return amount
    else:
        print("Insufficient balance or invalid amount!")
        return 0


def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************************")
        print("********Banking Program********")
        print("1. Show Balance")
        print("2. Make a Deposit")
        print("3. Make a Withdrawal")
        print("4. Exit the program")
        print("*******************************")

        try:
            choice = int(input("Enter your choice (1 - 4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Invalid choice, please choose a number between 1 and 4.")

    print("Thanks for banking with us. Good day 🥰")


if __name__ == "__main__":
    main()
