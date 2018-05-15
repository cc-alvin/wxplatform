# -*- coding: utf-8 -*-
import hashlib

from flask import request
from flask import jsonify
import app_config
from util import receive
from util import reply
import invitation
import robot
from ext import db
import result_util

app = app_config.init()
db.init_app(app)


@app.route('/verify', methods=['POST', 'GET'])
def verify():
    if request.method == 'GET':
        return handleGet(request)
    if request.method == 'POST':
        return handlePost(request)


def handleGet(request):
    signature = request.args.get("signature");
    token = '123456789'
    timestamp = request.args.get("timestamp");
    nonce = request.args.get("nonce");
    echostr = request.args.get("echostr");
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    string=''.join(list)
    sha1.update(string.encode())
    hashcode = sha1.hexdigest()
    print("GET verify: hashcode, signature: ", hashcode, signature)
    if signature == hashcode:
        return echostr
    else:
        return ""


def handlePost(request):
    web_data = request.get_data()
    recMsg = receive.parse_xml(web_data=web_data)
    toUser = recMsg.FromUserName
    fromUser = recMsg.ToUserName
    if isinstance(recMsg, receive.TextMsg) and recMsg.MsgType == 'text':
        message = recMsg.Content
        content = handleMessage(message, toUser)
        result = ''
        print(content)
        if type(content) is list:
            for x in content:
                result += x.__repr__()
        else:
            result += content
        replyMsg = reply.TextMsg(toUser, fromUser, result)
        return replyMsg.send()
    else:
        print("暂且不处理")
        result = '暂时只支持文本查询'
        replyMsg = reply.TextMsg(toUser, fromUser, result)
        return replyMsg.send()


def handleMessage(message, openid):
    # message = message.decode('utf-8')
    if '邀请码' in message:
        has_chance = invitation.hasChance(openid)
        if not has_chance:
            return '不可重复申请邀请码'
        invitation.addOpenid(openid, db)
        return invitation.getInvitationCode(db)
    else:
        return robot.getReply(message,openid)


@app.route('/reply', methods=['POST'])
def inner():
    if request.method == 'POST':
        msg = request.get_json()
        data = msg['msg']
        openid = msg['openid']
        return jsonify(result_util.getSuccessResponse(handleMessage(data, openid)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='19999')
