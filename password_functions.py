import random
import connect
from connect import CONNECT



def generate_password(password_length):
    generated_password = ''
    alpha_list = ['abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz'.upper(),'0123456789','!@#$%^&*_+:;<>?']
    while True:
        len1 = random.randint(0,len(alpha_list)) - 1
        len2 = random.randint(0,len(alpha_list[len1])) - 1
        generated_password += alpha_list[len1][len2]
        if len(generated_password) == password_length:
            return str(generated_password)
            break

def check_length(data):
    if len(data) < 1:
        return False
    else:
        return True

def insert_data(application,email,password,username,url):
    
    if not(check_length(application) or check_length(email) or check_length(password)):
        return 1
    else:
        insert_query = """INSERT INTO accounts(application,email,password,username,url) VALUES(
    %s,%s,%s,%s,%s);
        """
        try:
            cursor = CONNECT.cursor()
            cursor.execute(insert_query,[application,email,password,username,url])
            CONNECT.commit()
            return 3
        except:
            return 1
        
def retreve_data():
    query = "SELECT application,email,password,username,url FROM accounts;"
    try:
        cursor = CONNECT.cursor()
        cursor.execute(query)
        fetch = cursor.fetchall()
        return fetch
    except:
        return False

def delete_data(application,email):
    delete_query = "DELETE FROM accounts WHERE application = %s AND email = %s ;"
    try:
        cursor = CONNECT.cursor()
        cursor.execute(delete_query,[application,email])
        CONNECT.commit()
        return True
    except:
        return False
    

