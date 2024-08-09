from flask import Flask
from flask import render_template_string
from flask import render_template

app = Flask(__name__)

# To run application execute:
# flash run --debug

name = "Vladyslav Olegovych"
address = "Ukraine, Kyiv"
people = ["oleg", "vladik", "davyd"]


getPeople = lambda: people

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
def api_contacts():
    return render_template("contacts.html", address=address, pageTitle="Our Contacts", title="Contact address")

@app.route("/info")
def api_info():
    return render_template("info.html", pageTitle="Random information", title="Some information to be listed")

@app.route("/noinfo")
def api_noinfo():
    return render_template("noinfo.html")

@app.route("/people")
def api_people():
    return render_template("people.html", people=getPeople, pageTitle="Our People", title=render_template_string("People in our organsation ({{people()|length}})", people=getPeople))


