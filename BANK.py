#TASK 04 = BASIC BANKING SYSTEM

Balance = 0
name = input("Enter your name = ")

while(True):

    print("----- WELCOME TO VINAY BANK ----- ")
    print("Available services are = ")
    print("1.Deposit \n2.Balance check \n3.Withdraw \n4.Exit")

    
    choice=int(input("Enter the service which you want (1,2,3,4) = "))

    if choice ==1:
        amount=float(input("Enter the amount = ")) 
        Balance+=amount
        print("You have deposited",amount,"into your account and the available balance is = ",Balance)

    elif choice ==2:
        print("Your Available balance is = ",Balance)

    elif choice ==3:
        amount=float(input("Enter the amount to be withdraw = "))
        if amount<=Balance:
            Balance-=amount
            print("You have withdrawen",amount,"from your account and the balance is = ",Balance)
        else:
            print("Insufficient balance")

    elif choice ==4:
        print("--- THANK YOU FOR USING OUR SERVICE,",name,"---")
            

    else:
        print("PLEASE ENTER VALID SERVICE NUMBER WHICH YOU WANT ")
    