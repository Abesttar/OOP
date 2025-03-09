class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited: ${amount}\nNew Balance: ${self.balance}\n")

    def withdraw(self, amount):
        print("\nWithdrawal not allowed for a basic account.\n")
    
    def display_account_details(self):
        print(f"\nAccount Number: {self.account_number}\nBalance: ${self.balance}\n")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 500:
            print("\nWithdrawal limit exceeded. Max $500.\n")
        elif amount > self.balance:
            print("\nInsufficient funds.\n")
        else:
            self.balance -= amount
            print(f"\nWithdrew: ${amount}\nNew Balance: ${self.balance}\n")

class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self, amount):
        if amount > 2000:
            print("\nWithdrawal limit exceeded. Max $2000.\n")
        elif amount > self.balance:
            print("\nInsufficient funds.\n")
        else:
            self.balance -= amount
            print(f"\nWithdrew: ${amount}\nNew Balance: ${self.balance}\n")

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def show_details(self):
        print(f"\n{self.name} | ID: {self.emp_id} | Salary: ${self.calculate_salary()}\n")

class Manager(Employee):
    def calculate_salary(self): return self.salary * 1.2

class Engineer(Employee):
    def calculate_salary(self): return self.salary * 1.1

class Intern(Employee):
    pass

class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days

class Car(Vehicle):
    def open_trunk(self): print("\nTrunk is open.\n")

class Bike(Vehicle):
    def kickstart(self): print("\nBike kickstarted.\n")

class LuxuryFeatures:
    def enable_gps(self): print("\nGPS enabled.\n")
    def enable_heated_seats(self): print("\nHeated seats enabled.\n")

class LuxuryCar(Car, LuxuryFeatures):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + 50 * days

def menu(options, prompt="Choose an option: "):
    print("\n" + "-" * 30)
    for i, option in enumerate(options, 1): print(f"{i}. {option}")
    print("-" * 30)
    return input(f"\n{prompt}")

def bank_menu():
    accounts = {}
    while (choice := menu(["Create Account", "Deposit", "Withdraw", "Show Details", "Exit"])) != "5":
        acc_num = input("\nEnter Account Number: ")
        if choice == "1":
            acc_type = input("\nAccount Type (Savings/Premium): ").lower()
            if acc_type == "savings":
                accounts[acc_num] = SavingsAccount(acc_num)
            elif acc_type == "premium":
                accounts[acc_num] = PremiumSavingsAccount(acc_num)
            else:
                print("\nInvalid account type.\n")
                continue
            print("\nAccount Created Successfully.\n")
        elif acc_num in accounts:
            if choice == "2":
                amount = float(input("\nEnter Amount: "))
                accounts[acc_num].deposit(amount)
            elif choice == "3":
                amount = float(input("\nEnter Amount: "))
                accounts[acc_num].withdraw(amount)
            elif choice == "4":
                accounts[acc_num].display_account_details()
        else:
            print("\nAccount not found.\n")

def employee_menu():
    employees = []
    while (choice := menu(["Add Employee", "Show Employees", "Exit"])) != "3":
        if choice == "1":
            role = input("\nRole (Manager/Engineer/Intern): ").lower()
            cls = {"manager": Manager, "engineer": Engineer, "intern": Intern}.get(role)
            if cls: 
                employees.append(cls(input("\nName: "), input("ID: "), float(input("Salary: "))))
                print("\nEmployee Added Successfully.\n")
        elif choice == "2":
            [e.show_details() for e in employees]

def vehicle_menu():
    vehicles = []
    bike_brands = ["nmax", "pcx", "vario", "beat", "satria", "ninja", "byson", "vixion"]
    while (choice := menu(["Add Vehicle", "Calculate Rental", "Exit"])) != "3":
        if choice == "1":
            vehicle_type = input("\nVehicle Type (Car/Bike): ").lower()
            if vehicle_type == "car":
                car_type = input("\nCar Type (Regular/Luxury): ").lower()
                if car_type == "regular":
                    brand = input("\nBrand (Avanza/Xenia/Sigra/Inova): ").lower()
                    model = input("\nModel: ")
                    rate = {"avanza": 100, "xenia": 110, "sigra": 90, "inova": 150}.get(brand, 100)
                    vehicles.append(Car(brand, model, rate))
                    print("\nRegular Car Added Successfully.\n")
                elif car_type == "luxury":
                    brand = input("\nBrand (BMW/Rolls-Royce/Mercedes): ").lower()
                    model = input("\nModel: ")
                    rate = {"bmw": 300, "rolls-royce": 500, "mercedes": 400}.get(brand, 300)
                    vehicles.append(LuxuryCar(brand, model, rate))
                    print("\nLuxury Car Added Successfully.\n")
                else:
                    print("\nInvalid car type.\n")
            elif vehicle_type == "bike":
                print(f"\nAvailable Bike Brands: {', '.join(bike_brands)}")
                brand = input("\nBrand: ").lower()
                model = input("\nModel: ").lower()
                rate = {"nmax": 50, "pcx": 60, "vario": 40, "beat": 30, "satria": 70, "ninja": 80, "byson": 60, "vixion": 50}.get(brand, 30)
                vehicles.append(Bike(brand, model, rate))
                print("\nBike Added Successfully.\n")
            else:
                print("\nInvalid vehicle type.\n")
        elif choice == "2":
            vehicle_type = input("\nVehicle Type (Car/Bike): ").lower()
            if vehicle_type == "car":
                car_type = input("\nCar Type (Regular/Luxury): ").lower()
                brand = input("\nBrand: ").lower()
                model = input("\nModel: ").lower()
                for v in vehicles:
                    if isinstance(v, Car) and ((car_type == "regular" and not isinstance(v, LuxuryCar)) or (car_type == "luxury" and isinstance(v, LuxuryCar))) and v.brand == brand and v.model == model:
                        days = int(input("\nDays: "))
                        print(f"\nTotal Rental Cost: ${v.calculate_rental(days)}\n")
                        break
                else:
                    print("\nVehicle not found.\n")
            elif vehicle_type == "bike":
                brand = input("\nBrand: ").lower()
                model = input("\nModel: ").lower()
                for v in vehicles:
                    if isinstance(v, Bike) and v.brand == brand and v.model == model:
                        days = int(input("\nDays: "))
                        print(f"\nTotal Rental Cost: ${v.calculate_rental(days)}\n")
                        break
                else:
                    print("\nVehicle not found.\n")
            else:
                print("\nInvalid vehicle type.\n")

def main():
    while (choice := menu(["Bank Management", "Employee Management", "Vehicle Rental", "Exit"])) != "4":
        {"1": bank_menu, "2": employee_menu, "3": vehicle_menu}.get(choice, lambda: print("\nInvalid choice.\n"))()

if __name__ == "__main__":
    main()