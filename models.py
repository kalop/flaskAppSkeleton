from myapp import db

#Table in the db
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    mail = db.Column(db.String(100))
    random = db.Column(db.Integer)
