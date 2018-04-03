from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")

def index():
    return render_template("index.html")

@app.route('/validate-data', methods=['POST'])
def validate_data():
    username = request.form["username"]
    password = request.form["password"]
    verifypass = request.form["verifypass"]
    email = request.form["email"]   

    username_error=""
    password_error =""
    verifypass_error =""
    email_error=""

    if not username:   
        username_error = "Please enter a username." 
    elif len(username) < 3:
        username_error = "Must be more than 3 characters."       
    elif len(username) > 20:
        username_error = "Username is too long. Must be less than 20 characters."
    else:
        username = username

    if not password:   
        password_error = "Please enter a password."  
        password = ""
    elif len(password) < 3:
        password_error = "Must be more than 3 characters."       
        password = ""
    elif len(password) > 20:
        password_error = "Username is too long. Must be less than 20 characters."
        password = ""
    else:
        password = password
    
    if not verifypass:   
        verifypass_error = "Please enter a verify password." 
        verifypass = ""   
    elif password != verifypass:
        verifypass_error = "Password and verify password must be the same."       
        verifypass = ""
    else:
        verifypass = verifypass
        
    if email.count("@") != 1:
        email_error = "There must be exactly 1 @ sign."
    elif email.count(".") !=1:
        email_error = "There must be exactly 1 . sign."
    elif len(email) < 3:
        email_error = "Must be more than 3 characters."       
    elif len(email) > 20:
        email_error = "Email is too long. Must be less than 20 characters."
    else:
        email = email

    if not username_error and not password_error and not verifypass_error and not email_error:  #this passes if the strings stay empty
        return render_template("welcome.html", username=username)
    else:  #it had an error
        return render_template("index.html", 
            username_error=username_error,
            password_error=password_error,
            verifypass_error=verifypass_error,
            email_error=email_error
            )    

app.run()
