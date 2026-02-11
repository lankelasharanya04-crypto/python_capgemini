class Bank:
    # Static (class) members
    bank_name = "ABC Bank"
    branch = "Hyderabad"
    timings = "9am-4:30pm"
    ifsc_code = "ABC000123"

    # Constructor
    def __init__(self, name, age, profession, account_type, balance):
        self.name = name
        self.age = age
        self.profession = profession
        self.account_type = account_type
        self.balance = balance
    def with_money(self, amount):
        if amount <= self.balance and self.balance>0:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def deposit(self,amount):
        self.balance+=amount 
        print("deposited",amount)
    def display(self):
        print("Bank:", Bank.bank_name)
        print("Name:", self.name)
        print("age:",self.age)
        print("profession:",self.profession)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
c1 = Bank("Sharanya", 20, "Student", "Savings", 5000)
c2 = Bank("Paddu", 25, "Engineer", "Current", 15000)
c1.with_money(100)
c1.deposit(2000)
c1.display()

