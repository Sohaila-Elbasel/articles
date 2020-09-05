from blog import app
from flask import render_template

@app.route('/')
def home():
    return "hello world"
