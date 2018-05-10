def getSuccessResponse(data):
    res = {}
    res['code'] = 0
    res['msg'] = 'ok'
    res['data'] = data
    return res


def getFailedResponse(data):
    res = {}
    res['code'] = 1
    res['msg'] = 'failed'
    res['data'] = data
    return res