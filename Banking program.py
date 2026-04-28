#PYTHON BANKING PROGRAM


def show_balance(balance):

    print(f"Your Balance is: ${balance:.2f}")
    print("*******************")


def deposit():
    print("*******************")
    amount = float(input("Enter an amount to deposit: "))


    if amount < 0:
        print("That is not a valid amount")
        return 0

    else:
        return amount


def withdraw(balance):
    print("*******************")
    amount = float(input("Enter an amount to withdraw: "))


    if amount > balance:
        print("Insufficient funds")
        return 0

    elif amount < 0:
        print("Amount must be greater than zero")
        return 0

    else: return amount



def main():

    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("Banking Program")
        print("*******************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")
        print("*******************")
        choice = input("Enter Your choice from (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
          balance -=  withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*******************")
            print("That is not a valid option")
            print("*******************")
    print("*******************")
    print("Thankyou Have a nice day!")
    print("*******************")

if __name__ == '__main__':
    main()
