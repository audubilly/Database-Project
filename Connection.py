import getpass
import mysql.connector
from mysql.connector import Error
import os

username_str = input("Enter your username: ")
password_str = getpass.win_getpass()
db_name = input("Enter db name: ")

conn = None


def initialize_connection():
    try:
        global conn
        conn = mysql.connector.connect(
            host='localhost',
            user=username_str,
            password=password_str
        )
        print("connection successful")
        if conn.is_connected():
            sql = f'CREATE DATABASE IF NOT EXISTS {db_name}'
            conn.cursor().execute(sql)
            print(f"{db_name} created successfully")
            return conn
    except Error as connection_error:
        print("connection failed due to connection error", connection_error)


def close_connection():
    if conn is not None and conn.is_connected:
        conn.close()
        print("database closed.......")


def create_table():
    queries = [
        '''
        CREATE TABLE IF NOT EXISTS Customer(
        customerId INTEGER not null AUTO_INCREMENT,
        firstName VARCHAR(50) not null,
        LastName VARCHAR(50) not null,
        middleName VARCHAR(50),
        mobileNumber VARCHAR (11) UNIQUE,
        occupation VARCHAR(90),
        date_of_birth DATE,
        constraint  customer_pk PRIMARY KEY(customerId)
        );
        ''',
        '''
            CREATE TABLE IF NOT EXISTS Account(
            accountNumber INTEGER not null AUTO_INCREMENT,
            customerId INTEGER not null,
            accountType VARCHAR (40),
            accountStatus VARCHAR (40),
            accountOpeningDate DATE DEFAULT(CURRENT_DATE ),
            constraint account_pk  PRIMARY KEY(accountNumber),
            constraint account_fk FOREIGN KEY(customerId) references Customer(customerId) on delete cascade 
            );
        ''',
        '''
           CREATE TABLE IF NOT EXISTS Transactions(
           transactionId INTEGER not null AUTO_INCREMENT,
           accountNumber INTEGER not null,
           transactionDate DATE DEFAULT (CURRENT_DATE ),
           transactionType VARCHAR (40) not null,
           transactionAmount INTEGER not null,
           transactionMedium VARCHAR (40) not null,
           constraint transactions_pk PRIMARY KEY (transactionId),
           constraint transaction_fk FOREIGN KEY (accountNumber) references Account(accountNumber) on delete cascade ) 
        ''']
    for query in queries:
        conn.cursor().execute(query)

