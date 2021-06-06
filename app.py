from flask import Flask, request
from flask_cors import CORS
import sqlite3
import json

port = 5000
app = Flask(__name__)
CORS(app)

# endpoints that take the user to this point of the directory
@app.route("/", methods=["POST"])
def respond():
    conn = sqlite3.connect("MOCdb.db")
    cursor = conn.cursor()
    sql_command = """INSERT INTO business_info (first, last, birthday, business_name, business_address, contact, email, state, city, zip,
    specialization, experience, ownership, website_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    values = (request.form["first-name"], request.form["last-name"], request.form["birthday"], request.form["BusName"], request.form["address"], request.form["phone-number"], request.form["email"], request.form["state"], request.form["city"], request.form["zip"], request.form["dropdown"], request.form["experience"], request.form["ownership"], request.form["website-link"] )
    print(values)
    cursor.execute(sql_command, values)
    conn.commit()
    conn.close()
    return "Ok"

@app.route("/searchbyname/<business_name>", methods=["GET"])
def search(business_name):
    conn = sqlite3.connect("./MOCdb.db")
    cursor = conn.cursor()
    sql_command = """SELECT * FROM business_info WHERE business_name LIKE ?;"""
    values = (f'%{str(business_name)}%',)

    cursor.execute(sql_command, values)

    row_headers = [x[0] for x in cursor.description] # Get all the column names in the db

    results = cursor.fetchall()

    json_response = []


    for row in results:
        json_response.append(dict(zip(row_headers, row))) # Create dictionaries combining row_headers with real data

    conn.commit()
    conn.close()
    print(f'found {len(json_response)} match{"" if len(json_response) == 1 else "es"} for "{business_name}"')
    return json.dumps(json_response)

if __name__ == "__main__":
    app.run(port=port)

