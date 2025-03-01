import random

accounts = {}

def register():
    print("=== Register ===")
    username = input("Set your username: ")
    if username in accounts:
        print("\nUsername already exists. Try again.")
        return
    
    password = input("Set your password: ")
    
    account_number = input("Enter your account number (10 digits): ")
    while not account_number.isdigit() or len(account_number) != 10:
        print("Invalid account number. It must be a 10-digit number.")
        account_number = input("Enter your account number: ")

    accounts[username] = {'password': password, 'balance': 0.0, 'account_number': account_number}
    print("\nRegistration successful.")

def login():
    print("\n=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts and accounts[username]['password'] == password:
        print("\nLogin successful.")
        return username
    else:
        print("\nInvalid username or password.")
        return None

def logout():
    print("\nYou have been logged out.")
    return None

def display_accounts():
    print("\n+----------------------+------------+----------------------+")
    print("| Username            | Balance    | Account Number       |")
    print("+----------------------+------------+----------------------+")
    for user, info in accounts.items():
        print(f"| {user:<20} | ${info['balance']:>10.2f} | {info['account_number']:<20} |")
    print("+----------------------+------------+----------------------+")

def display_menu():
    print("\n=== Bank Menu ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Logout")

def display_table(title, amount):
    print("\n+----------------------+------------+")
    print(f"| {title:<20} | ${amount:>10.2f} |")
    print("+----------------------+------------+")

def check_balance(username):
    balance = accounts[username]['balance']
    display_table("Current Balance", balance)

def deposit_money(username):
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("\nInvalid amount. Must be greater than zero.")
            return
        accounts[username]['balance'] += amount
        display_table("Deposited", amount)
    except ValueError:
        print("\nInvalid input. Please enter a numeric value.")

def withdraw_money(username):
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("\nInvalid amount. Must be greater than zero.")
            return
        if amount > accounts[username]['balance']:
            print("\nInsufficient funds.")
        else:
            accounts[username]['balance'] -= amount
            display_table("Withdrawn", amount)
    except ValueError:
        print("\nInvalid input. Please enter a numeric value.")

def main():
    while True:
        print("\n=== Account Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Show Registered Accounts")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    display_menu()
                    choice = input("\nEnter your choice: ")
                    
                    if choice == '1':
                        check_balance(username)
                    elif choice == '2':
                        deposit_money(username)
                    elif choice == '3':
                        withdraw_money(username)
                    elif choice == '4':
                        logout()
                        break
                    else:
                        print("\nInvalid choice. Please try again.")
        elif choice == '3':
            display_accounts()
        elif choice == '4':
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
