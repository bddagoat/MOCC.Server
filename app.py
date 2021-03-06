import re
from unicodedata import category
from flask import Flask, request
# from flask import SQLAlchemy
from flask import jsonify
from flask_cors import CORS
import sqlite3
import json
import time

port = 5000
app = Flask(__name__)
CORS(app)

# endpoints that take the user to this point of the directory
# inserts account info into database
@app.route("/create-profile", methods=["POST"])
def respond():
    conn = sqlite3.connect("MOCdb.db")
    cursor = conn.cursor()
    sql_command = """INSERT INTO business_info (first, last, birthday, business_name, business_address, contact, email, state, city, zip,
    specialization, ownership, hire, website_link, mission_statement) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    values = (request.get_json()["first"],
              request.get_json()["last"], 
              request.get_json()["birthday"], 
              request.get_json()["business_name"], 
              request.get_json()["business_address"], 
              request.get_json()["contact"], 
              request.get_json()["email"], 
              request.get_json()["state"], 
              request.get_json()["city"], 
              request.get_json()["zip"], 
              request.get_json()["specialization"], 
              request.get_json()["ownership"], 
              request.get_json()["hire"], 
              request.get_json()["website_link"], 
              request.get_json()["mission_statement"])

    print(values)
    cursor.execute(sql_command, values)
    
    sql_command = """SELECT * FROM business_info WHERE first = ? AND last = ? AND business_name = ?"""
    values1 = (request.get_json()["first"], request.get_json()["last"], request.get_json()["business_name"])
    cursor.execute(sql_command, values1)

    business = cursor.fetchone()
    conn.commit()
    conn.close()
    return json.dumps(business)
    # json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/specalists", methods=["POST"])
def specialists(): 
    conn = sqlite3.connect("MOCdb.db")
    cursor = conn.cursor()
    sql_command = """INSERT INTO prospect_info (first, last, email, education, state, city, bio, contact, password, website_link, specialization, resume) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    values = (request.get_json()["first"],
              request.get_json()["last"],
              request.get_json()["email"], 
              request.get_json()["education"], 
              request.get_json()["state"], 
              request.get_json()["city"],  
              request.get_json()["bio"], 
              request.get_json()["contact"], 
              request.get_json()["password"], 
              request.get_json()["website_link"],
              request.get_json()["specialization"],
              request.get_json()["resume"])
    print(values)
    cursor.execute(sql_command, values)

    sql_command = """SELECT * FROM prospect_info WHERE first = ? AND last = ? AND specialization = ?"""
    values1 = (request.get_json()["first"], request.get_json()["last"], request.get_json["specialization"])
    cursor.execute(sql_command, values1)

    prospect = cursor.fetchone() 
    conn.commit()
    conn.close()
    return json.dumps(prospect)
    # json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route("/artists", methods=["POST"])
def artists(): 
    conn = sqlite3.connect("MOCdb.db")
    cursor = conn.cursor()
    sql_command = """INSERT INTO artist_producer (first, last, email, state, city, contact, password, website_link, genre, profile)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    values = (request.get_json()["first"],
              request.get_json()["last"],
              request.get_json()["email"], 
              request.get_json()["state"], 
              request.get_json()["city"],   
              request.get_json()["contact"], 
              request.get_json()["password"], 
              request.get_json()["website_link"],
              request.get_json()["genre"],
              request.get_json()["profile"])
    print(values)
    cursor.execute(sql_command, values)

    sql_command = """SELECT * FROM artist_producer WHERE first = ? AND last = ? AND genre = ?"""
    values1 = (request.get_json()["first"], request.get_json()["last"], request.get_json["genre"])
    cursor.execute(sql_command, values1)

    artist = cursor.fetchone() 
    conn.commit()
    conn.close()
    return json.dumps(artist)


@app.route("/art", methods=["POST"])
def media():
    conn = sqlite3.connect("MOC.db")
    cursor = conn.cursor()
    sql_command = """INSERT INTO art_media (name, title, email, category, file, monetize, description) VALUES (?, ?, ?, ?, ?, ?, ?);"""

    values = (request.get_json()["name"],
              request.get_json()["title"],
              request.get_json()["email"],
              request.get_json()["category"],
              request.get_json()["file"],
              request.get_json()["montize"],
              request.get_json()["description"])
    print(values)
    cursor.execute(sql_command, values)

    sql_command = """SELECT * FROM art_media WHERE name = ? AND category = ? AND monetize = ?"""
    values1 = (request.get_json()["name"], request.get_json()["category"], request.get_json()["monetize"])
    cursor.execute(sql_command, values1)

    media = cursor.fetchone()
    conn.commit()
    conn.close()
    return json.dumps(media)


# Posts will be received by the post page and inserted into the gallery_art table to create a db of account posts

# @app.route("/post", method=["POST"])
# def art():
#     conn = sqlite3.connect("MOCdb.db")
#     cursor = conn.cursor()
#     sql_command = """INSERT INTO gallery_art (name, title, email, category, monetize, picture, description)
#     VALUES (?, ?, ?, ?, ?, ?, ?)"""
#     values = (request.get_json()["name"],
#               request.get_json()["title"],
#               request.get_json()["email"],
#               request.get_json()["category"],
#               request.get_json()["monetize"],
#               request.get_json()["picture"],
#               request.get_json()["description"])
#     print(values)
#     cursor.execute(sql_command, values)        

#     # conditional for category

#     sql_command = """SELECT * FROM gallery_info WHERE name = ? AND title = ? AND Category = ?"""
#     values1 = (request.get_json()["name"], request.get_json()["title"], request.get_json["category"])
#     cursor.execute(sql_command, values1)

#     art = cursor.fetchone() 
#     conn.commit()
#     conn.close()
#     return json.dumps(art)


# init SQLAlchemy so we can use it later in our models
# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#     app.config['SECRET_KEY'] = 'secret-key-goes-here'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'MOCdb.db'

#     db.init_app(app)

#     # blueprint for auth routes in our app
#     from flask_auth_app import flask_auth_app as flask_auth_app
#     app.register_blueprint(flask_auth_app_blueprint)

#     # blueprint for non-auth parts of app
#     from .app import app as app_blueprint
#     app.register_blueprint(app_blueprint)

#     return app



# displays the database data to the search engine
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

# Conditional for submit page where posts will be uploaded to home and submit page and categorized

# @app.route("/submit/<post>", method=["GET"])
# def art(post):
#     conn = sqlite3.connect("MOCdb.db")
#     cursor = conn.cursor()
#     sql_command = """SELECT * FROM gallery_art WHERE name LIKE ? AND title LIKE ? AND category LIKE ?;"""
#     values = (f'%{str(post)}%',)
#     cursor.execute(sql_command, values)        

#     conditional for category

#     if category == "art" in gallery_art:

#     row_headers = [x[0] for x in cursor.description] # Get all the column names in the db

#     results = cursor.fetchall()

#     json_response = []

#     for row in results:
#         json_response.append(dict(zip(row_headers, row))) # Create dictionaries combining row_headers with real data

#     conn.commit()
#     conn.close()
#     print(f'found {len(json_response)} match{"" if len(json_response) == 1 else "es"} for "{post}"')
#     return json.dumps(json_response)


  
@app.route("/prospect/<prospect>", methods=["GET"])
def searchProspect(prospect):
    conn = sqlite3.connect("./MOCdb.db")
    cursor = conn.cursor()
    sql_command = """SELECT * FROM prospect_info WHERE prospect LIKE ?;"""
    value = (f'%{str(prospect)}%',)

    cursor.execute(sql_command, value)
    row_headers =  [x[0] for x in cursor.description] 

    results = cursor.fetchall()

    json_response = []

    for row in results:
        json_response.append(dict(zip(row_headers, row))) # Create dictionaries combining row_headers with real data

    conn.commit()
    conn.close()
    print(f'found {len(json_response)} match{"" if len(json_response) == 1 else "es"} for "{prospect}"')
    return json.dumps(json_response)


@app.route("/artist-account/<artist>", methods=["GET"])
def searchArtists(artist):
    conn = sqlite3.connect("./MOCdb.db")
    cursor = conn.cursor()
    sql_command = """SELECT * FROM artist_producer WHERE artist LIKE ?;"""
    value = (f'%{str(artist)}%',)

    cursor.execute(sql_command, value)
    row_headers = [x[0] for x in cursor.description] 

    results = cursor.fetchall()

    json_response = []

    for row in results:
        json_response.append(dict(zip(row_headers, row))) # Create dictionaries combining row_headers with real data

    conn.commit()
    conn.close()
    print(f'found {len(json_response)} match{"" if len(json_response) == 1 else "es"} for "{artist}"')
    return json.dumps(json_response)


if __name__ == "__main__":
    app.run(port=port)


