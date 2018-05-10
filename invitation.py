import time
from model.Chance import Chance
from model.InviteCode import InviteCode
def getInvitationCode(db):
    print(int(time.time()))
    code=InviteCode.query.filter(InviteCode.endtime>int(time.time()),InviteCode.status==1).first()
    return code.code


def hasChance(openid):
    ret = Chance.query.filter_by(openid=openid).count() <= 0
    return ret


def addOpenid(openid, db):
    item = Chance(openid)
    db.session.add(item)
    db.session.commit()
