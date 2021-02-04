from Connection import *


def initialize_database():
    connection = initialize_connection()
    use_database()
    create_table()
    return connection


def create_new_account():
    firstName = input("enter your firstName")
    lastName = input("enter your lastName")
    mobile_number = input("enter your mobileNumber")
    date_of_birth = input("enter your dateOfBirth in YYYY-MM-DD")

    if firstName == "":
        raise ValueError("firstName must be entered")

    if mobile_number == "":
        raise ValueError("mobileNumber must be entered")

    if lastName == "":
        raise ValueError("lastname must be entered ")

    sql = 'insert into bankProject.Customer(firstName, lastName, mobilenumber, date_of_birth) ' \
          'VALUES (%s, %s, %s, %s)'
    values = [(firstName, lastName, int(mobile_number), date_of_birth)]

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
