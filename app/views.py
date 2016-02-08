from flask import render_template
from app import app


@app.route('/')
def api():
    return render_template('index.html')
