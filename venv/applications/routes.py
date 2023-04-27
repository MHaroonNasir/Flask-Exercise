from applications import app, db
from flask import render_template, redirect, url_for, request
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

@app.route('/rating/<int:userid>', methods = ["GET", "POST", "UPDATE"])
def amendRating(userid, operation):
    # show = Shows.query.get_or_404(int(id))
    # entry = Shows(rating = rating)
    # db.session.update(entry)
    # db.session.commit()


    #1st id likely refers to id column in db and 2nd id refers to id parameter passed into function
    print("!1!!!!!!!!!!!!!!!!!!!!!", userid, operation)
    #userrating = request.form
    #print("!1!!!!!!!!!!!!!!!!!!!!!", userrating)
    user = Shows.query.get(int(userid))
    print("!!!!!!!!!!!!!!!!!!!!!!!-------------------", user, user.name, user.rating)
    user.rating = int(user.rating)+1
    db.session.commit()
    #print("show id----->", id, user)
    return redirect(url_for('displayShow', id = user.id))


@app.route('/dashboard')
def dashboard():
    shows = Shows.query.all()
    data = [d.__dict__ for d in shows]
    for show in data:
        show.pop('_sa_instance_state', None)
    return render_template('dashboard.html', data = data)