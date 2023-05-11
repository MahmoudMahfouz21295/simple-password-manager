from mysql import connector
from mysql.connector import Error

try:
    CONNECT = connector.Connect(host='localhost',database='password_manager',username='root',password='')
except Error as e:
    ERROR = e