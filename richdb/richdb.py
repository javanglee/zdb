# -*- encoding=utf8 -*-
import random
import json
import requests

from .ztime import Time
from .mdict import mdict
from .vdict import vdict

def rich():
    reds = [
     '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
    blues = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']
    reds_you_get = []
    try:
        for i in range(6):
            x = random.randint(0, 32)
            reds[i], reds[x] = reds[x], reds[i]

    except Exception as e:
        print(i, x)

    reds_you_get = reds[0:6]
    blue = random.choice(blues)
    blue = "['" + str(blue) + "']"
    text = '\n我们的口号是：为发财而生\nOur Slogan: BORN FOR RICH\n\n      [   ]\n(@)==[_____]==(@)\n      |* *|\n      (_-_)\n     /     \\\n    /    / 恭 /\n__@__   / 喜 /\n\\___/  / 发 / \\\n  \\   / 财 /  /\n   |_________|\n\n   "MONEY GOD"\n   Buddha Ruly, Camel God, Jesus God, ... and so on.\n   There are seven Gods in this world.\n   One God rule them all.\n   Knee before the Money God and pray.\n   And then you will be rich.\n'
    print(text)
    print('these numbers may make you rich:')
    print(sorted(reds_you_get), blue)


def pray(*args, **kw):
    cookie = "token=code_space;"
    header = {
        "cookie": cookie,
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    post_json = json.dumps({'args':args, 'kw':kw })
    try:
        MoneyGodReply = requests.post("http://richdb.net/pray", data=post_json, headers=header)
        #MoneyGodReply = requests.post("http://127.0.0.1/pray", data=post_json, headers=header)
        print( MoneyGodReply.text )
    except Exception as e:
        print('财神很忙！')
        print('The Money God is busy!')

def q(*args, **kw):
    cookie = "token=code_space;"
    header = {
        "cookie": cookie,
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    post_json = json.dumps({'args':args, 'kw':kw })
    try:
        query = requests.post("http://richdb.net/q", data=post_json, headers=header)
        #query = requests.post("http://127.0.0.1/q", data=post_json, headers=header)
        return query.text
    except Exception as e:
        print(e)