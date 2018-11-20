import json


def success(data={}):
    r = {'code': 200, 'data': data if (data != {}) else 'success'}
    return json.dumps(r, ensure_ascii=False)


def fail(message="request fail"):
    r = {'code': 400, 'data':  message}
    return json.dumps(r, ensure_ascii=False)