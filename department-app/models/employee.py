from flask import g

db = g.db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    name = db.Column(db.String(50))
    birthdate = db.Column(db.Date)
    salary = db.Column(db.Numeric)
