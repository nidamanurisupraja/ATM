import random
 
class Account:
    def __init__(self, name, pin,balance, annualInterestRate):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.annualInterestRate = annualInterestRate
 
    def getId(self):
        return self.name
   
    def getPin(self):
        return self.pin
 
    def getBalance(self):
        return self.balance
 
    def getAnnualInterestRate(self):
        return self.annualInterestRate
 
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
 
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
   
def main():
    accounts = []
    acc1 = Account(0,0,0,3.4)
    while True:
        print("\n------->> USE ATM  <<-------\n1 - Make Transactions \t 2 - Create an Account \t 3 - Terminate ")
        cond = int(input("\nEnter your selection: "))
        if cond==1:
            acc=int(input("Enter Your Account number: "))
            flag = 0
            acc1 = Account(0,0,0,3.4)
            while True:
                if flag==-1:
                    acc=int(input("Invalid Account number.. Re-enter: "))
                flag = -1
                for i in accounts:
                    if i.getId()==acc:
                        flag = 1
                        acc1 = i
                        break
                if flag!=-1:
                    break
           
            pin = int(input("\nEnter account pin: "))
            while pin < 1000 or pin > 9999 or pin!=acc1.getPin():
                pin = int(input("\nInvalid Pin.. Re-enter: "))
               
            if pin==acc1.getPin():
                accountObj = acc1
               
               
        elif cond==2:
            acc=int(input("Enter Your Account number: "))
            flag = 0
            while True:
                if flag==1:
                    acc=int(input("Invalid Account number.. Re-enter: "))
                flag = -1
                for i in accounts:
                    if i.getId()==acc:
                        #print(i.getId())
                        flag = 1
                        break
                if flag==-1:
                    break
            pin = int(input("\nEnter account pin: "))


            accountObj = Account(acc,pin,0,3.4)
            accounts.append(accountObj)
        elif cond==3:
            #  write Exit
            print("\nATM System is Terminated!!!!!!!!!!")
            #exit()
            break
        else:
               print("That's an invalid choice.")
           
        while True:
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
            selection = int(input("\nEnter your selection: "))
           
            if selection == 1:
                print(accountObj.getBalance())
            elif selection == 2:
                amt = float(input("\nEnter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
 
                if ver_withdraw == "Yes":
                    print("Verify withdraw")
                else:
                    break
 
                if amt < accountObj.getBalance():
                   accountObj.withdraw(amt)
                   print("\nUpdated Balance: " + str(accountObj.getBalance()) + " ")
                else:
                     print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " ")
                     print("\nPlease make a deposit.");
            elif selection == 3:
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
 
                if ver_deposit == "Yes":
                   accountObj.deposit(amt);
                   print("\nUpdated Balance: " + str(accountObj.getBalance()) + " ")
                else:
                    break
 
            elif selection == 4:
                print("nTransaction is now complete.")
                print("Transaction number: ", random.randint(10000, 1000000))
                print("Current Interest Rate: ", accountObj.annualInterestRate)
                print("Monthly Interest Rate: ", accountObj.annualInterestRate / 12)
                print("Thanks for choosing us as your bank")
                break
 
            else:
                print("That's an invalid choice.")
           
main()
