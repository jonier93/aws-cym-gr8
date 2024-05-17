from flask import render_template, request, jsonify
from database.db import connectionSQL, insert_records, consult_records
from controller.s3_control import connection_s3, upload_file_s3, save_file, get_file_s3

def func_register_user():
    data_user = request.form
    photo = request.files["photo"]
    id, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"] 
    confirm = insert_records(id, name, lastname, birthday)
    if confirm: 
        s3_connection = connection_s3()
        photo_path = save_file(id, photo)
        upload_file_s3(s3_connection, photo_path)
        return "<h1> User added </h1>"
    else:
        return"<h1> Error creating the user </h1>"
    
def func_consult_user():
    data_id = request.get_json()
    result = consult_records(data_id["id"])
    if result != None and len(result) != 0:
        s3_connection = connection_s3()
        name_file = get_file_s3(s3_connection, data_id["id"])
        print(name_file)
        name = result[0][1]
        lastname = result[0][2]
        birthday = "1999-01-01"
        resp_data = {
            "status":"ok",
            "name": name,
            "lastname": lastname,
            "birthday": birthday,
            "photo" : name_file
        }
    else:
        resp_data = {"status":"error"}
    return jsonify(resp_data)