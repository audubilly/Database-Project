from util import *

userChoice_str = input("""welcome to Mansa Bank"
Enter 1 To Create a new Account: 
Enter 2 To Create your Account Details:
Enter 3 To update your Account Details:
Enter 4 To Make a new Transaction:
Enter 5 To View your Transaction History: 
Enter 6 To Delete your Account: 
Enter 7 To Quit:
""")

userChoice_int = int(userChoice_str)

if userChoice_int == 1:
    create_new_account()

# if userChoice_int == 2:
#     account_number = int(input("Enter account number"))
#     get_account_details(account_number)

# if userChoice_int == 3:
#     account_number = int(input("Enter account number"))
#     get_account_details(account_number)


