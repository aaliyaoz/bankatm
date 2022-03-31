from os import access


class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def check_balance(self):
        print("your balance is 10,000")
    def withdrawl(self,amount):
        new_amount=10,000-amount
        print("you have withdrawn"+str(amount)+"your remaning balance is"+str(new_amount))
def main():
    card_number=input("insert your card number")
    pin_number=input("insert your pin number")
    new_user=Atm(card_number, pin_number)
    print("choose your activity")
    print("1.balance enquiry 2.withdrawl")
    activity=int(input("enter activity number"))
    if activity==1:
        new_user.check_balance()
    elif activity==2:
        amount=int(input("enter the amount"))
        new_user.withdrawl(amount)
    else:print("enter a value number")
if __name__=="__main__":
    main()