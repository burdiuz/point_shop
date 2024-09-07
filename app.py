from flask import Flask, jsonify, request
from flask import render_template_string
from flask import render_template
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient()
db = client.point_shop

# To run application execute:
# flask run --debug

name = "Vladyslav Olegovych"
address = "Ukraine, Kyiv"
age = 100500

getAddress = lambda: address

# ---- PAGES

@app.route("/")
def hello_world():
    return "<p>Hello, {}!</p>".format(name)


@app.route("/<verb>/<name>")
def verb(verb, name):
    if verb == "hello":
        return "Hello {}.".format(name)
    elif verb == "bye":
        return "Bye {}.".format(name)
    else:
        return "Go away you fat little piece of shit."

@app.route("/contacts")
def page_contacts():
    return render_template("contacts.html", pageTitle="Our Contacts", title="Contact address")

@app.route("/info")
def page_info():
    return render_template("info.html", pageTitle="Random information", title="Some information to be listed")

@app.route("/noinfo")
def page_noinfo():
    return render_template("noinfo.html", pageTitle="Test page", title="Test page")

@app.route("/people")
def page_people():
    return render_template("people.html", pageTitle="Our People", title="People in our organsation")

@app.route("/age")
def page_age():
    return render_template("age.html", age=age, pageTitle="age", title="main developer's age is")

@app.route("/nasa/sbdb")
def page_nasa_sbdb():
    return render_template("nasa/sbdb.html", pageTitle="Nasa SBDB Query", title="Search in Small-Body Database")

# --- API ENDPOINTS

@app.route("/api/people")
def api_people():
    users = db.users
    list = []
    for user in users.find():
        list.append(user['name'])

    return list

@app.route("/api/address")
def api_address():
    return jsonify(getAddress())


@app.route("/api/nasa/sbdb")
def api_nasa_sbdb():
    searchTerm = request.args.get('sstr')
    url = "https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=" + searchTerm
    
    response = requests.get(url)

    return response.json()
