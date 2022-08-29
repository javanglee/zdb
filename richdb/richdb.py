# -*- encoding=utf8 -*-
import random
import sys
from os.path import dirname, abspath
sys.path.append( dirname( abspath( __file__ ) ) )

from ztime import Time
from mdict import mdict
from vdict import vdict

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
    print( args, kw)
