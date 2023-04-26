from applications import db, app
from applications.models import Shows

def create_database():
    with app.app_context():
        db.create_all()

def delete_database():
    with app.app_context():
        db.drop_all()

def add_entries():
    entry1 = Shows(name="income", genre="500", description="investments")
    entry2 = Shows(rating=5)
    entry3 = Shows(name="sal", description="2000")
    entry4 = Shows(name="bob", rating=2)
    with app.app_context():
        db.session.add(entry1)
        db.session.add(entry2)
        db.session.add(entry3)
        db.session.add(entry4)
        db.session.commit()

def see_db_entries():
    with app.app_context():
        entries = Shows.query.all()
        for entry in entries:
            print(f"{entry.name}, {entry.genre}, {entry.description}, {entry.rating}, {entry.release}")

if __name__ == "__main__":
    delete_database()
    create_database()
    add_entries()
    see_db_entries()
