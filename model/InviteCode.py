# -*- coding:utf-8 -*-


from ext import db


class InviteCode(db.Model):
    __tablename__ = 'pre_common_invite'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    endtime = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __repr__(self):
        return self.code

    def __init__(self, code, endtime, status):
        self.code = code;
        self.endtime = endtime
        self.status = status
