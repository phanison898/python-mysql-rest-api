import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, Response
import mysql.connector

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB_NAME = os.environ.get("MYSQL_DB_NAME")

conn = mysql.connector.connect(
    host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB_NAME, auth_plugin='mysql_native_password')

if conn.is_connected:
    print("Successfully connected to database")
else:
    print("Unable to connect to database")

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM users")

for i in mycursor:
    for j in i:
        print(j, end="\t")
    print(end="\n")
