from flask import render_template, request, jsonify
from server import app
from database.db import connectionSQL, insert_records, consult_records

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
    data_user = request.form
    id, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"] 
    insert_records(id, name, lastname, birthday)
    return render_template("register.html")
    
@app.route("/consult_user", methods=["post"])
def consult_user():
    data_id = request.get_json()
    result = consult_records(data_id["id"])
    if result != None and len(result) != 0:
        name = result[0][1]
        lastname = result[0][2]
        birthday = "1999-01-01"
        resp_data = {
            "status":"ok",
            "name": name,
            "lastname": lastname,
            "birthday": birthday
        }
    else:
        resp_data = {"status":"error"}
    return jsonify(resp_data)
    
    