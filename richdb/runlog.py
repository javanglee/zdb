#-*- encoding=utf8 -*-
import os, sys
import threading, time, logging
from functools import wraps
import traceback
from .ztime import Time
log_begin_time = Time().fmt('_%Y_%m_%d_%H_%M_%S')
logging.basicConfig(filename=f"log{log_begin_time}.txt", level=(logging.DEBUG), format='%(asctime)s-%(levelname)s-%(message)s')

def log(func):
    """
        日志装饰器，简单记录函数的日志
    """

    @wraps(func)
    def inner(*args, **kwargs):
        pid = os.getpid()
        tid = threading.currentThread().ident
        funcid = (f"{func.__name__}") + str(int(time.time()))
        funcinfo = f"pid:{pid}:tid:{tid}:funcid:{funcid}:func:{func.__name__} {args}"
        logging.debug(f"{funcinfo} begin ")
        res = None
        try:
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                logging.debug(f"{funcinfo} exception: {e} happended")
                traceback.print_exc()
            else:
                logging.debug(f"{funcinfo} -> {res} successed")
                return res
        finally:
            return

        logging.debug(f"{funcinfo} -> {res} finished")
        return res

    return inner


if __name__ == '__main__':

    @log
    def pluser(a, b):
        """ add two ele togethor"""
        raise NameError('pluser exception')
        return a + b


    print(pluser.__doc__)
    print(pluser.__name__)

    def plus(a, b):
        raise NameError('plus exception')


    a = 1
    b = 2
    while True:
        pluser(a, b)