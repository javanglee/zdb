#-*- encoding=utf8 -*-
import datetime as dt, time, re, calendar

def get_strdate_format(date):
    fmt = None
    mat = re.match('\\d{4}', date)
    if mat is not None:
        fmt = '%Y'
    mat = re.match('\\d{4}-\\d{2}', date)
    if mat is not None:
        fmt = '%Y-%m'
    mat = re.match('\\d{4}-\\d{2}-\\d{2}', date)
    if mat is not None:
        fmt = '%Y-%m-%d'
    mat = re.match('\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}', date)
    if mat is not None:
        fmt = '%Y-%m-%d %H'
    mat = re.match('\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}', date)
    if mat is not None:
        fmt = '%Y-%m-%d %H:%M'
    mat = re.match('\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}', date)
    if mat is not None:
        fmt = '%Y-%m-%d %H:%M:%S'
    mat = re.match('\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}\\.\\d+', date)
    if mat is not None:
        fmt = '%Y-%m-%d %H:%M:%S.%f'

    mat = re.match('\\d{4}/\\d{2}', date)
    if mat is not None:
        fmt = '%Y/%m'
    mat = re.match('\\d{4}/\\d{2}/\\d{2}', date)
    if mat is not None:
        fmt = '%Y/%m/%d'
    mat = re.match('\\d{4}/\\d{2}/\\d{2}\\s+\\d{2}', date)
    if mat is not None:
        fmt = '%Y/%m/%d %H'
    mat = re.match('\\d{4}/\\d{2}/\\d{2}\\s+\\d{2}:\\d{2}', date)
    if mat is not None:
        fmt = '%Y/%m/%d %H:%M'
    mat = re.match('\\d{4}/\\d{2}/\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}', date)
    if mat is not None:
        fmt = '%Y/%m/%d %H:%M:%S'
    mat = re.match('\\d{4}/\\d{2}/\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}\\.\\d+', date)
    if mat is not None:
        fmt = '%Y/%m/%d %H:%M:%S.%f'
        
    mat = re.match('\\d{4}\\d{2}', date)
    if mat is not None:
        fmt = '%Y%m'
    mat = re.match('\\d{4}\\d{2}\\d{2}', date)
    if mat is not None:
        fmt = '%Y%m%d'
    mat = re.match('\\d{4}\\d{2}\\d{2}\\s\\d{2}', date)
    if mat is not None:
        fmt = '%Y%m%d %H'
    mat = re.match('\\d{4}\\d{2}\\d{2}\\s\\d{2}:\\d{2}', date)
    if mat is not None:
        fmt = '%Y%m%d %H:%M'
    mat = re.match('\\d{4}\\d{2}\\d{2}\\s\\d{2}:\\d{2}:\\d{2}', date)
    if mat is not None:
        fmt = '%Y%m%d %H:%M:%S'
    mat = re.match('\\d{4}\\d{2}\\d{2}\\s\\d{2}:\\d{2}:\\d{2}\\.\\d+', date)
    if mat is not None:
        fmt = '%Y%m%d %H:%M:%S.%f'
    return fmt