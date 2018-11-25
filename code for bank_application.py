import sys
class Customer:
    "' Customer class with bank related application'"
    bank_name='CITY BANK'

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print('After deposit the balance:',self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficient Funds___cannot perform Operation')
            sys.exit()
        self.balance=self.balance-amt
        print('After withdraw the balance:',self.balance)

    def balance_enquiry(self):
        print('Your balance is:',self.balance)

print('Welcome to',Customer.bank_name)
name=input('Enter your Name:')
c=Customer(name)
while True:
   print('d-Deposit\n w-Withdrawt\n be-balance_enquiry\n e-Exi')
   option=input('choose your option:')
   if option.lower()=='d':
       amt=float(input('Enter the amount to deposit:'))
       c.deposit(amt)
   elif  option.lower()=='w':
       amt=float(input('Enter the amount to withdraw:'))
       c.withdraw(amt)
   elif  option.lower()=='be':
       c.balance_enquiry()
   elif option.lower()=='e':
       print('Thanks for Banking')
       sys.exit()
   else:
       print('Choose valid option')
