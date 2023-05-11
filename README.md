# simple-password-manager
Simple project with python language and MySQL database that allow you to create and management your passwords for different accounts on applications / sites

## Features that password-manager Supported:

  1. Create New Password
  2. Get My Passwords
  4. Delete My Password

## Installing

  First Of All You Need To Install Python3 And MySQL DBMS On Your Device
  Then You Need To git or download This Project
  
  ### git simple-password-manager
  ```
    git clone https://github.com/MahmoudMahfouz21295/simple-password-manager.git
  ```
  
  ### import modules
  ```
    pip3 install mysql
    pip3 install random
  ```
  
## Database creation

  You Need To Create Database On MySQL DBMS That Will Be Used To Save Your Passwords
  ```
    CREATE DATABASE password_manager;
    
    USE password_manager;
    
    CREATE TABLE accounts(
          id INT NOT NULL AUTO_INCREMENT,
          application VARCHAR(255) NOT NULL,
          email VARCHAR(255) NOT NULL,
          password VARCHAR(255) NOT NULL,
          username VARCHAR(255),
          url VARCHAR(255),
          PRIMARY KEY(id)
    );
    
    -- Pseudo Data For Testing --
    INSERT INTO accounts(application,email,password,username,url) VALUES(
            'APP NAME','example@email.com','P0w3rFu1_P@55wrD','optional_username','https://optional.url.com/'
    );
    
    SELECT * FROM accounts;
  ```
  
 

## Usage
  ```
    python3 password_manager.py 
    // Results
    # Select one choice
     - Create New Password (1)
     - Show My Passwords (2)
     - Delete My Password (3)
     - Exit (0)
     ? 
  ```
