import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page."""

    return render_template('index.html')


@app.route('/home')
def home():
    
    return render_template('bio.html')

@app.route('/projects')
def projects():

    return render_template('projects.html')


@app.route('/education')
def education():

    return render_template('education.html')

if __name__ == "__main__":
    app.run(debug=True)