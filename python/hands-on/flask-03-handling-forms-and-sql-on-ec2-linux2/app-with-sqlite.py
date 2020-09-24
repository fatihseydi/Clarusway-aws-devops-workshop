# Import Flask modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# Create an object named app
app = Flask(__name__)
# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
# Execute the code below only once.
# Write sql code for initializing users table..
drop_table= """
DROP TABLE IF EXISTS users;
"""
users_table = """    
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""
data = """
INSERT INTO users
VALUES
    ("Levent Akyuz", "levent.akyuz@gmail.com"),
    ("Mustafa Kanat", "mustafa.kanat@yahoo.com"),
    ("Hakan Sule", "hakan.sule@clarusway.com");
"""
db.session.execute(drop_table)
db.session.execute(users_table)
db.session.execute(data)
db.session.commit()
# Write a function named `find_emails` which find emails using keyword from the user table in the db,
# and returns result as tuples `(name, email)`.
def find_emails(keyword):
    query=f"""
    SELECT * FROM users WHERE username like '%{keyword}%'
    """
    result = db.session.execute(query)
    db.session.commit()
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [('Not Found', 'Not Found')]
    return user_emails

# Write a function named `insert_email` which adds new email to users table the db.


# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
#using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')


#Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')


# Add a statement to run the Flask application which can be reached from any host on port 80.


    #app.run(host='0.0.0.0', port=80)