accounts = {}

def create_account():
    acc = input("Account No: ")
    name = input("Name: ")
    balance = float(input("Initial Balance: "))
    accounts[acc] = {"name": name, "balance": balance}
    print("Account created")

def deposit():
    acc = input("Account No: ")
    if acc in accounts:
        amt = float(input("Deposit Amount: "))
        accounts[acc]["balance"] += amt
        print("Deposited")
    else:
        print("Account not found")

def withdraw():
    acc = input("Account No: ")
    if acc in accounts:
        amt = float(input("Withdraw Amount: "))
        if accounts[acc]["balance"] >= amt:
            accounts[acc]["balance"] -= amt
            print("Withdrawn")
        else:
            print("Insufficient balance")
    else:
        print("Account not found")

def view_accounts():
    for acc, data in accounts.items():
        print(acc, data["name"], data["balance"])

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.View 5.Exit")
    choice = input("Choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        view_accounts()
    elif choice == "5":
        break
    else:
        print("Invalid choice")