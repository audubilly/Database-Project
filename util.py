from Connection import *


def initialize_database():
    connection = initialize_connection()
    create_table()
    return connection


def create_new_account():
    firstName = input("enter your firstName: ")
    lastName = input("enter your lastName: ")
    mobile_number = input("enter your mobileNumber: ")
    date_of_birth = input("enter your dateOfBirth in YYYY-MM-DD: ")

    if firstName == "":
        raise ValueError("firstName must be entered")

    if mobile_number == "":
        raise ValueError("mobileNumber must be entered")

    if lastName == "":
        raise ValueError("lastname must be entered ")

    sql = 'insert into bankProject.Customer(firstName, lastName, mobilenumber, date_of_birth) ' \
          'VALUES (%s, %s, %s, %s)'
    values = [(firstName, lastName, mobile_number, date_of_birth)]

    connection = initialize_database()
    connection.cursor().executemany(sql, values)
    connection.commit()
    query = f'select customerId from bankProject.customer where mobilenumber = {mobile_number}'
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    customer_Id = result[0]

    query = 'insert into bankProject.account(customerId, accountType, accountStatus) ' \
            'values (%s,%s,%s)'

    accountType = int(input("Enter 1 for savings account , 2 for a current account "))
    if accountType == 1:
        accountType = 'savings'
    else:
        accountType = 'current'

    values2 = [(customer_Id, accountType, 'active')]

    cursor.executemany(query, values2)
    connection.commit()

    close_connection()


def make_transaction():
    accountNumber = int(input("Enter your acct number: "))
    transaction_type = int(input("For transaction_type press 1 for Credit and 2 for Debit: "))
    if transaction_type == 1:
        transaction_type == 'credit'
    else:
        transaction_type == 'debit'

    transaction_amount = int(input("Enter transaction_amount: "))

    transaction_medium = input("For medium of transaction press 1 for ATM and 2 for CashWithdrawal: ")
    if transaction_medium == 1:
        transaction_medium == 'ATM'
    else:
        transaction_medium == 'Cash Withdrawal'

    sql = 'insert into bankProject.transactions(accountNumber, transactionType, transactionAmount, \
          transactionMedium) ' \
          'VALUES (%s, %s, %s,%s)'

    values = (accountNumber, transaction_type, transaction_amount, transaction_medium)
    connection = initialize_connection()
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()
    connection.close()


def get_account_details():
    accountNumber = int(input("Enter your acct number: "))
    sql = f'''  select * from customer join account
                on account.customerId = customer.customerId
                where accountNumber = {accountNumber}'''

    connection = initialize_database()
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    connection.close()
    print(result)


def update_account():
    accountNumber = int(input("Enter account Number: "))
    user_choice = int(input("Enter 1 to update firstName, and 2 to update LastName: "))
    column_name = ''
    new_value = ''
    if user_choice == 1:
        column_name = 'firstName'
        new_value = input("Enter firstName: ")
    else:
        column_name = 'lastName'
        new_value = input("Enter lastName: ")

    customer_id_query = f'select customerId from account where accountNumber = {accountNumber}'
    connection = initialize_database()
    cursor = connection.cursor()
    cursor.execute(customer_id_query)
    result = cursor.fetchone()
    customer_Id = result[0]
    sql = f'update customer set {column_name} = %s where customerId = {customer_Id}'
    value = (new_value,)
    cursor.execute(sql, value)
    connection.commit()
    connection.close()


def delete_account_details():
    accountNumber = int(input("Enter account Number: "))
    customer_id_query = f'select customerId from account where accountNumber = {accountNumber}'
    connection = initialize_database()
    cursor = connection.cursor()
    cursor.execute(customer_id_query)
    result = cursor.fetchone()
    customer_Id = result[0]
    delete_account_query = 'Delete from account where accountNumber = %s'
    delete_customer_query = 'Delete from customer where customerId = %s'
    cursor.execute(delete_account_query, (accountNumber,))
    cursor.execute(delete_customer_query, (customer_Id,))
    connection.commit()
    connection.close()
