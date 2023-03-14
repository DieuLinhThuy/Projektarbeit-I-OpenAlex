import os

from flask import Flask, render_template
from neo4j import Graphdatabase
from flask import Blueprint, jsonify, redirect, render_template, request
from basicauth import basic_auth
from dotenv import load_dotenv

load_dotenv()

password = os.environ.get("DATABASE_PASSWORD")
username = os.environ.get("DATABASE_USERNAME")
url = os.getenv("DATABASE_URL")

app = Flask(__name__, static_folder="static/")
driver = Graphdatabase.driver(url, auth=basic_auth(username, password))
@app.route("/")
def index():
    return render_template("index.html")

