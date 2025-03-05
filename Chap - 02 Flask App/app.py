# Run $pip install flask in terminal
from flask import Flask,render_template,request,url_for
import sqlite3

connection = sqlite3.connect("pets.db", check_same_thread=False)

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def get_index():
    return("Example flask server")