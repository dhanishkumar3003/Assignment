class BankAccount:
    ROI = 7
    
    def __init__(self):
        self.Name = ""
        self.Amount =0.0
    
    def GetUserInfo(self):
        self.Name = input("Enter account holder's name: ")
        self.Amount = float(input("Enter initial amount: "))
    
    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print(f"{deposit_amount} has been deposited.")
    
    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print(f"{withdraw_amount} has been withdrawn Successfully.")
        else:
            print("Insufficient balance!")
    
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on the current amount ({self.Amount}) at ROI {BankAccount.ROI}% is: {interest}")
    
    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Amount: {self.Amount}")

account1 = BankAccount()
account1.GetUserInfo()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()

account2 = BankAccount()
account2.GetUserInfo()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()
account2.Display()
