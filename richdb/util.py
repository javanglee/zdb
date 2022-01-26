#-*- encoding=utf8 -*-

import datetime as dt
import time
import re
import calendar

def get_strdate_format(date):

    fmt=None
    #xxxx-xx-xx format time str 

    mat = re.match(r"\d{4}", date)
    if mat is not None:
        fmt='%Y'

    mat = re.match(r"\d{4}-\d{2}", date)
    if mat is not None:
        fmt='%Y-%m'

    mat = re.match(r"\d{4}-\d{2}-\d{2}", date)
    if mat is not None:
        fmt='%Y-%m-%d'

    mat= re.match(r"\d{4}-\d{2}-\d{2}\s+\d{2}", date)
    if mat is not None:
        fmt='%Y-%m-%d %H'

    mat= re.match(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y-%m-%d %H:%M'

    mat= re.match(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y-%m-%d %H:%M:%S'

    mat = re.match(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d+", date)
    if mat is not None:
        fmt='%Y-%m-%d %H:%M:%S.%f'

    #xxxx.xx.xx format time str 

    mat = re.match(r"\d{4}\.\d{2}", date)
    if mat is not None:
        fmt='%Y.%m'

    mat = re.match(r"\d{4}\.\d{2}\.\d{2}", date)
    if mat is not None:
        fmt='%Y.%m.%d'

    mat = re.match(r"\d{4}\.\d{2}\.\d{2}\s+\d{2}", date)
    if mat is not None:
        fmt='%Y.%m.%d %H'

    mat = re.match(r"\d{4}\.\d{2}\.\d{2}\s+\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y.%m.%d %H:%M'

    mat = re.match(r"\d{4}\.\d{2}\.\d{2}\s+\d{2}:\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y.%m.%d %H:%M:%S'

    mat = re.match(r"\d{4}\.\d{2}\.\d{2}\s+\d{2}:\d{2}:\d{2}\.\d+", date)
    if mat is not None:
        fmt='%Y.%m.%d %H:%M:%S.%f'

    #xxxx/xx/xx format time str 

    mat = re.match(r"\d{4}/\d{2}", date)
    if mat is not None:
        fmt='%Y/%m'

    mat = re.match(r"\d{4}/\d{2}/\d{2}", date)
    if mat is not None:
        fmt='%Y/%m/%d'

    mat = re.match(r"\d{4}/\d{2}/\d{2}\s+\d{2}", date)
    if mat is not None:
        fmt='%Y/%m/%d %H'

    mat = re.match(r"\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y/%m/%d %H:%M'

    mat = re.match(r"\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y/%m/%d %H:%M:%S'

    mat = re.match(r"\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}\.\d+", date)
    if mat is not None:
        fmt='%Y/%m/%d %H:%M:%S.%f'

    #xxxxxxxx format time str 

    mat = re.match(r"\d{4}\d{2}", date)
    if mat is not None:
        fmt='%Y%m'

    mat = re.match(r"\d{4}\d{2}\d{2}", date)
    if mat is not None:
        fmt='%Y%m%d'

    mat = re.match(r"\d{4}\d{2}\d{2}\s\d{2}", date)
    if mat is not None:
        fmt='%Y%m%d %H'

    mat = re.match(r"\d{4}\d{2}\d{2}\s\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y%m%d %H:%M'

    mat = re.match(r"\d{4}\d{2}\d{2}\s\d{2}:\d{2}:\d{2}", date)
    if mat is not None:
        fmt='%Y%m%d %H:%M:%S'

    mat = re.match(r"\d{4}\d{2}\d{2}\s\d{2}:\d{2}:\d{2}\.\d+", date)
    if mat is not None:
        fmt='%Y%m%d %H:%M:%S.%f'

    return fmt