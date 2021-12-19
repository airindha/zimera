class deposit:
    deposit = 0
    def __init__(self):
        print()
    def setDeposit(d):
        deposit.deposit = d
    
    def getDeposit():
        return deposit

class withdraw :
    withdraw = 0 
    def __init__(self):
        print()  
    def setWithdraw(self, w):
        withdraw.withdraw = w
    
    def getWithdraw():
        return withdraw

class balanceInquiry:
    balanceInquiry = 0
    def __init__(self):
        print()
    def setBalance(self,b):
        balanceInquiry.balance = b
    
    def getBalance(self):
        return balanceInquiry

class ATMMachine(deposit, withdraw, balanceInquiry):

    saldo = 250000
    def checkBalance(self):
        print("\tYour current balance is " + balanceInquiry.getBalance())
   
    def withdrawMoney(self):
        if balanceInquiry.balanceInquiry == 0:
            print("\tYour current balance is zero.")
            print("\tYou cannot withdraw!")
            print("\tYou need to deposit money first.")

        elif balanceInquiry.balanceInquiry <= 500:
            print("\tYou do not have sufficient money to withdraw")
            print("\tChecked your balance to see your money in the bank.")

        elif withdraw.withdraw > balanceInquiry.balance:
            print("\tThe amount you withdraw is greater than to your balance")
            print("\tPlease check the amount you entered.")

        else:
            balanceInquiry.balance = balanceInquiry.balance - withdraw.withdraw
            print("\n\tYou withdraw the amount of Php " + withdraw.withdraw)
    
    def depositMoney():
        print("\tYou deposited the amount of " + deposit.getDeposit())

    def __init__(self):
        select = 0
        choice = 0
        print("====================================================")
        print("\tWelcome to this simple ATM machine")
        print("====================================================")
        print()

        while True:
            try :
                input1 =int(input("Enter 0 to entry the next step :"))        
                if input1 == 0 :
                    print("\tPlease select ATM Transactions")
                    print("\tPress [1] Deposit")
                    print("\tPress [2] Withdraw")
                    print("\tPress [3] Balance Inquiry")
                    print("\tPress [4] Exit")

                    print("\n\tWhat would you like to do? ")
                    
                    select =int(input("Enter number your choice : "))

                    if select == 1:
                        print("\n\tEnter the amount of money to deposit Rp ")
                        deposit.deposit = int(input(""))
                        balanceInquiry.balance = deposit.deposit + balanceInquiry.balance
                        print("Your deposit now is Rp ", balanceInquiry.balance)
                    elif select == 2:
                        print("\n\t To withdraw, make sure that you have sufficient balance in your account.")
                        print()
                        print("\tEnter amount of money to withdraw Rp ")
                        withdraw.withdraw = int(input())
                        ATMMachine.withdrawMoney(self)
                        remaining = ATMMachine.saldo - withdraw.withdraw
                        print("The remaining money Rp ", remaining)
                    elif select == 3:
                        print("Balance money Rp ", ATMMachine.saldo)
                    elif select == 4 :
                        print("\n\ttransaction excited.") 
                    else :
                        print("\n\t please select correct")
                    try:    
                        print("\n\tWould you like to try another transaction?")
                        print("\n\tPress [1] Yes \n\tPress [2] No")
                        print("\tEnter choice: ")
                        choice =int(input("Enter the number of your choice : "))
                        if choice == 1:
                            print("Welcome back!")
                        elif choice == 2:
                            print ("Thank you for using ATM machine")
                            break
                        else : 
                            print("\n\tPlease select correct choice.")
                    except:
                        print("\tError Input! Please enter a number only.")
                        choice =int(input(""))
                        print("\tEnter yout choice:", choice)
            except :
                print("Enter the correct number.")    
        
atm1=ATMMachine()                    

print("\n\tThank you for using this simple ATM Machine.")