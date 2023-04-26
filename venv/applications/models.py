from applications import db
from datetime import datetime

class Shows(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), default = 'python', nullable = False)
    genre = db.Column(db.String(30), default = 'horror', nullable = False)
    description = db.Column(db.String(30), default = 'spooky', nullable = False)
    rating = db.Column(db.Integer, default = 3, nullable = False)
    release = db.Column(db.DateTime, default = datetime.utcnow, nullable = False)

    def __str__(self):
        return self.id
