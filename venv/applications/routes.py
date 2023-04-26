from applications import app
from flask import render_template, redirect, url_for
from applications.models import Shows

@app.route('/')
def index():
    entries = Shows.query.order_by(Shows.release.desc()).all()
    return render_template('index.html', title = "Home Page", entries = entries)

@app.route('/layout')
def layout():
    return render_template('layout.html', title = "layout")


@app.route('/show/<int:id>', methods = ["GET", "POST"])
def displayShow(id):
    entry = Shows.query.get_or_404(int(id))
    #print("show id----->", id)
    return render_template('show.html', title = "Show Page", entry = entry)

@app.route('/add/<int:id>', methods = ["UPDATE"])
def amendRating(id):
    pass
