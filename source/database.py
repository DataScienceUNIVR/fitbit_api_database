import csv
from csv import reader
import datetime
import mysqlx
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
import credentials
from credentials import getCredentials

#path to the csv file of the sleep score
#path = "C:\\Users\\aless\\OneDrive\\Desktop\\Tesi_fitbit\\MyFitbitData\\Massimo\\Sleep\\sleep_score.csv"
path_to_csv = input("insert th path to the sleep score csv : ")
print(path_to_csv)


if path_to_csv != "" :
    #open the csv 
    path_to_csv = path_to_csv.replace('"', '')
    path_to_csv = path_to_csv.replace("\\", "\\\\")
    with open(path_to_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)