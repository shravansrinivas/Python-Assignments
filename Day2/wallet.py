def wallet1():
    balance=0;
    def deposit():
        amt = float(input("Enter the amount to deposit:"));
        nonlocal balance
        balance+=amt;
        return deposit
    def withdraw():
        amt = float(input("Enter the amount to deposit:"));
        nonlocal balance
        if(amt<=balance):
            balance-=amt;
            print("Amount withdrawn:",amt)
        else:
            print("No sufficient balance to withdraw amount")
        return withdraw
    def viewBalance():
        print("current balance:",balance)
        return viewBalance

    def transfer():
        w=input("Enter wallet: Wallet1 or wallet 2")
        amt = float(input("Enter the amount to Transfer:"));

        nonlocal balance
        if (amt <= balance):
            balance -= amt;
            print("Amount transferred:", amt)
            d1=wallet1()
            w=d1['W']
            d2=wallet2()
            d=d2['D']
        else:
            print("No sufficient balance to transfer amount")

    d1 = {"D": deposit, "B": viewBalance, "W": withdraw}
    return d1
def wallet2():
    balance=0;
    def deposit():
        amt = float(input("Enter the amount to deposit:"));
        nonlocal balance
        balance+=amt;
        return deposit
    def withdraw():
        amt = float(input("Enter the amount to deposit:"));
        nonlocal balance
        if(amt<=balance):
            balance-=amt;
            print("Amount withdrawn:",amt)
        else:
            print("No sufficient balance to withdraw amount")
        return withdraw
    def viewBalance():
        print("current balance:",balance)
        return viewBalance
    d2={"D":deposit,"B":viewBalance,"W":withdraw}
    return d2
    def transfer():
        w=input("Enter wallet: Wallet1 or wallet 2")
        amt = float(input("Enter the amount to Transfer:"));

        nonlocal balance
        if (amt <= balance):
            balance -= amt;
            print("Amount Transferred:", amt)
        else:
            print("No sufficient balance to transfer amount")

d1=wallet1()
dep=d1['D'];
bal=d1['B'];
wi=d1['W'];
d2=wallet2()
dep2=d2['D'];
bal2=d2['B'];
wi2=d2['W'];
process=True
while(process!=False):
    choice=input("What do you want to do:\nD=deposit\nW=withdraw\nB=viewBalance\n")
    if choice=='D':
        dep()


        process=bool(input("Do you want to continue? True or False:"));
    elif choice=='W':
        wi()
        process = bool(input("Do you want to continue? True or False:"));
    elif choice=='B':
        bal()
        process = bool(input("Do you want to continue? True or False:"));
    else:
        print("Invalid choice! Try again")


