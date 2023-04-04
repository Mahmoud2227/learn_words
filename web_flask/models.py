from web_flask import db


class List(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    words_list = db.Column(db.ARRAY(db.String), nullable=False)

    def __repr__(self):
        return f'List {self.name}'