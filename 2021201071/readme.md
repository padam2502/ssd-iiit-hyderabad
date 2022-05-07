# SSD Assignment 3B

## Instructions for Running the code

- Create virtual env with following command
    >python3 -m venv venv

- Activate the virtual env with following command.
    >source venv/bin/activate

- Install requirements with following command
    >pip3 install -r requirements.txt

- Add database in mysql to create tables

- Modify app.config['SQLALCHEMY_DATABASE_URI'] as follows. 
- Here username and password must be of mysql
    > app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://\<username>:\<password>@localhost/\<database name>'

- Run following commands in order in terminal
    > python3
    
    >from server import db

    >db.create_all()

    >exit()

- Run the Flask project with following command
    >python3 server.py

- On Seperate Terminal Run Client Application
    >python3 client.py

----

## Functions

- Provided '/make-chef/\<username>' api to make any user as chef

- The Flask App runs on 8000 port


