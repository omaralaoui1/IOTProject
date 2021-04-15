import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "192.168.1.107" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "database"
# this is the user you create
USER = "python-user"
# user password
PASSWORD = "broker123"
# connect to MySQL server
db_connection = mysql.connect(host=HOST, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
# enter your code here!