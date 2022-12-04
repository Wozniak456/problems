import os.path

from flask import Flask, Response, render_template
from back_rep1_main.db import db_init

app = Flask(__name__)
users, category, currency, record = db_init()
from back_rep1_main import views


@app.route('/')
def hello():  # pragma: no cover
    return render_template('index.html')