from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import os

load_dotenv()

db_username = os.getenv("databaseUser")
db_password = os.getenv("databasePassword")
db_databaseName = os.getenv("databaseName")

conn = None


def initialize_connection():
    try:
        global conn
        conn = mysql.connector.connect(
            host='localhost',
            user=db_username,
            password=db_password
        )
        print("connection successful")
        if conn.is_connected():
            sql = f'CREATE DATABASE IF NOT EXISTS {db_databaseName}'
            conn.cursor().execute(sql)
            print(f"{db_databaseName} created successfully")
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
        mobileNumber INTEGER(11) UNIQUE,
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
            constraint account_fk FOREIGN KEY(customerId) references Customer(customerId)
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
           constraint transaction_fk FOREIGN KEY (accountNumber) references Account(accountNumber)) 
        ''']
    for query in queries:
        conn.cursor().execute(query)


def use_database():
    sql = f'use {db_databaseName}'
    conn.cursor().execute(sql)
