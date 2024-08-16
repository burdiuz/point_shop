from flask import Flask
from flask import render_template_string
from flask import render_template

app = Flask(__name__)

# To run application execute:
# flash run --debug

name = "Vladyslav Olegovych"
address = "Ukraine, Kyiv"
people = ["oleg", "vladik", "davyd"]
age = 100500


getPeople = lambda: people

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
    return render_template("contacts.html", address=address, pageTitle="Our Contacts", title="Contact address")

@app.route("/info")
def page_info():
    return render_template("info.html", pageTitle="Random information", title="Some information to be listed")

@app.route("/noinfo")
def page_noinfo():
    return render_template("noinfo.html")

@app.route("/people")
def page_people():
    return render_template("people.html", pageTitle="Our People", title="People in our organsation")

@app.route("/age")
def page_age():
    return render_template("age.html", age=age, pageTitle="age", title="main developer's age is")

# --- API ENDPOINTS

@app.route("/api/people")
def api_people():
    return getPeople()