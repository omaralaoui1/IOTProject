import sqlite3
import mysql.connector

# SQLite DB Name
DB_Name =  "IoT.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists DHT22_Temperature_Data ;
create table DHT22_Temperature_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Temperature text
);
drop table if exists DHT22_Humidity_Data ;
create table DHT22_Humidity_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Humidity text
);
drop table if exists Soil_Moisture_Data ;
create table Soil_Moisture_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Soil_Moisture textases
);
"""

#Connect or Create DB File
connection = mysql.connector.connect(host='192.168.1.107',user='python-user',
                                   password='broker123')
print("Connected to :", connection.get_server_info())

