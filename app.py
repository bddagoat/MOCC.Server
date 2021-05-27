from flask import Flask, request
from flask_cors import CORS
import sqlite3

port = 5000
app = Flask(__name__)
CORS(app)

# endpoints that take the user to this point of the directory
@app.route("/", methods=["POST"])
def respond():
    conn = sqlite3.connect("MOCdb.db")
    cursor = conn.cursor()
    sql_command = """INSERT INTO business_info (first, last, birthday, business_name, business_address, contact, email, state, city, zip,
    specialization, experience, website_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    values = (request.form["firstName"], request.form["lastName"], request.form["birthday"],
              request.form["BusName"], request.form["address"], request.form["number"], request.form["email"],
              request.form["state"], request.form["city"], request.form["zip"], request.form["dropdown"],
              request.form["experience"], request.form["weblink"])
    cursor.execute(sql_command, values)
    print(request.form)
    conn.commit()
    conn.close()
    return "ok"

@app.route("/searchbyname/<business_name>", methods=["GET"])
def search(business_name):
    conn = sqlite3.connect("MOCdb.db")
    cursor = conn.cursor()
    sql_command = """SELECT * FROM business_info WHERE business_name = ?;"""
    values = (str(business_name),)
    cursor.execute(sql_command, values)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    print(results)
    return list(results)

if __name__ == "__main__":
    app.run(port=port)

