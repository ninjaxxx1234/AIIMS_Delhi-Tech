from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://CaptainNeoNight:Ninja141003@cluster0.wysd8lj.mongodb.net/"
mongo = PyMongo(app)

@app.route("/")
def hello_world():
    mongo.db.sample_mflix.insert_one({ "a": 1 })
    return "<p>Hello World</p>"

app.run(host="0.0.0.0", port=5000, debug=True)