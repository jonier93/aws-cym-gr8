from flask import render_template, request
from server import app
from controller.control import func_register_user, func_consult_user 

@app.route('/')
def home_page():
   return render_template("home.html")
   
@app.route('/register')
def register_page():
    return render_template("register.html")

@app.route("/consult")
def consult_page():
    return render_template("consult.html")
    
@app.route("/register_user", methods=["post"])
def register_user():
    return func_register_user()
    
@app.route("/consult_user", methods=["post"])
def consult_user():
    return func_consult_user()
    
    