from util import *

control = 1
while control != -1:
    userChoice_str = input("""welcome to Mansa Bank"
    Enter 1 To Create a new Account: 
    Enter 2 To Check your Account Details:
    Enter 3 To update your Account Details:
    Enter 4 To Make a new Transaction:
    Enter 5 To Delete your Account: 
    Enter 6 To Quit:
    """)

    userChoice_int = int(userChoice_str)

    if userChoice_int == 1:
        create_new_account()

    if userChoice_int == 4:
        make_transaction()

    if userChoice_int == 2:
        get_account_details()

    if userChoice_int == 3:
        update_account()

    if userChoice_int == 5:
        delete_account_details()
    if userChoice_int == 6:
        print("Goodbye ...")
        control = -1
