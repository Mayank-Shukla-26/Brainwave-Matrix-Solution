import time

print("Please insert your ATM Card")

time.sleep(5)

pin = int(input("Enter your 4 digit ATM Pin : "))

balance = 1000

if pin == 1234:

    while True:
        print("1 = Check Balance")
        print("2 = Withdraw Money")
        print("3 = Deposit Money")
        print("4 = Exit")
        try:
            option = int(input("Choose any option above : "))
        except:
            print("Please choose the valid option")

        if option == 1:
            print("-----------------------------------")
            print(f"Your current balance is {balance} rs.")

        if option == 2:
            withdraw_money = int(input("Enter your Withdraw Amount : "))
            if withdraw_money < balance:
                print("-----------------------------------")
                balance = balance - withdraw_money
                print(f"{withdraw_money} rs. is debited from your account")
                print(f"Your current balance is {balance} rs.")
            else:
                print("You do not have sufficient balance")

        if option == 3:
            deposit_money = int(input("Enter your Deposit Amount : "))
            balance = balance + deposit_money
            print("-----------------------------------")
            print(f"{deposit_money} rs. is credited to your Account")
            print(f"Your current balance is {balance} rs.")

        if option == 4:
            print("Thank you for visiting our ATM Machine...")
            break
else:
    print("You entered the wrong pin...Try Again")