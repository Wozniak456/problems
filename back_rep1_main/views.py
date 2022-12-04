import datetime
from flask import jsonify, request, Response, render_template
from flask_smorest import abort
from back_rep1_main import app, users, category, currency, record


@app.route("/categories", methods=['GET'])
def get_categories():
    return jsonify({"categories": category})

@app.route("/category", methods=['POST'])
def create_category():
    request_data = request.get_json()
    category.append(request_data)
    return jsonify(request_data)

@app.route("/users")
def get_users():
    return jsonify({"records": users})

@app.route("/registration")
def register_func():
    return render_template('registration.html')

@app.route("/user", methods=['GET', 'POST'])
def create_user():
    request_data = request.get_json()
    users.append(request_data)
    return jsonify(request_data)

@app.route("/records", methods=['GET'])
def get_records():
    return jsonify({"records": record})

@app.route("/record", methods=['POST'])
def create_record():
    request_data = request.get_json()
    record.append(request_data)
    return jsonify(request_data)