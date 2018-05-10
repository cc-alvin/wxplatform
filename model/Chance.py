# -*- coding:utf-8 -*-


from ext import db


class Chance(db.Model):
    __tablename__ = 'chance'
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return self.openid

    def __init__(self, openid):
        self.openid = openid;
