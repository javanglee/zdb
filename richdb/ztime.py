# -*- encoding=utf8 -*-
import sys
sys.path.append('.')

import datetime as dt, time, re, calendar, sys
from utils import get_strdate_format
from wull import wull, iswull, WULL
from datetime import datetime

if sys.version_info.major >=3 and sys.version_info.minor>=8:
    clocktime = time.perf_counter
    process_time = time.process_time
    process_time_ns = time.process_time_ns
else:
    clocktime = time.clock
    process_time = time.clock
    process_time_ns = time.clock

def get_month_firstday_Time(t):
    this_month_firstday = dt.datetime(t.year, t.month, 1)
    return Time(this_month_firstday.strftime('%Y-%m-%d %H:%M:%S'))

def get_month_lastday_Time(t):
    this_month_lastday = calendar.monthrange(t.year, t.month)[1]
    return Time(dt.datetime(t.year, t.month, this_month_lastday).strftime('%Y-%m-%d %H:%M:%S'))

class Time:
    def __init__(self, *args):
        self._Time__timestamp = time.time()
        self.__epoch =0.0
        if len(args) == 0 or args[0]=='':
            return
        if isinstance(args[0], float):
            self._Time__timestamp = args[0]
            return
        if isinstance(args[0], datetime):
            self._Time__timestamp = args[0].timestamp()
            return
        if isinstance(args[0], str):
            if args[0][0] == '@':
                self.__epoch=WULL
            else:
                fmt = get_strdate_format(args[0])
                if '.' in args[0]:
                    gsecond = args[0].split('.')[0]
                    lsecond = args[0].split('.')[1]
                else:
                    gsecond = args[0]
                    lsecond = ''
                if '.%f' in fmt:
                    gfmt = fmt.split('.')[0]
                    lfmt = fmt.split('.')[1]
                else:
                    gfmt = fmt
                    lfmt = ''
                fsecond = float('0.' + lsecond if len(lsecond) > 0 else '0')
                timeArray = time.strptime(gsecond, gfmt)
                dtime = dt.datetime.strptime(gsecond, gfmt)
                epoch = dt.datetime(1970, 1, 1)
                stamp_seconds = (dtime - epoch).total_seconds()
                self._Time__timestamp = stamp_seconds + fsecond
        else:
            raise ValueError("Time(args)'s args can only be float timestamp or str format or datetime.datetime")
    @property
    def epoch(self):
        return self._epoch
    
    @property
    def timestamp(self):
        return self._Time__timestamp

    @property
    def datetime(self):
        return self.fmt('%Y-%m-%d %H:%M:%S.%f')

    @property
    def year(self):
        return dt.datetime.fromtimestamp(self._Time__timestamp).year

    @property
    def month(self):
        return dt.datetime.fromtimestamp(self._Time__timestamp).month

    @property
    def day(self):
        return dt.datetime.fromtimestamp(self._Time__timestamp).day

    @property
    def week(self):
        return dt.datetime.fromtimestamp(self._Time__timestamp).week

    @classmethod
    def clock(cls):
        return clocktime()

    @classmethod
    def process_time(cls):
        return process_time()

    @classmethod
    def process_time_ns(cls):
        return process_time_ns()

    def timezone(self, utc):
        hours = int(utc.replace('UTC', ''))
        return self + hours * 60 * 60

    def fmt(self, fmt):
        dtime = dt.datetime(1970, 1, 1) + dt.timedelta(seconds=(self._Time__timestamp))
        strtimestamp = str(self._Time__timestamp)
        if '.%f' in fmt:
            fmt = fmt.split('.')[0]
            if self._Time__timestamp >= 0:
                lsecond = strtimestamp.split('.')[1]
            else:
                lsecond = str(1.0 - float('0.' + strtimestamp.split('.')[1])).split('.')[1]
            return dtime.strftime(fmt) + '.' + lsecond
        else:
            return dtime.strftime(fmt)

    def monthdiff(self, other):
        return (self.year - other.year) * 12 + (self.month - other.year)

    def yeardiff(self, other):
        return self.year - other.year

    def daydiff(self, other):
        return (self - orther) / 60.0 / 60.0 / 24.0

    def __repr__(self):
        return self.fmt('%Y-%m-%d %H:%M:%S.%f')

    def __str__(self):
        return "{'timestamp':" + str(self._Time__timestamp) + ',' + "'datetime':" + "'" + self.fmt('%Y-%m-%d %H:%M:%S.%f') + "'" + '}'

    def __add__(self, other):
        if isinstance(other, int):
            new_timestamp = self._Time__timestamp + float(other)
        else:
            if isinstance(other, float):
                new_timestamp = self._Time__timestamp + orther
            else:
                if isinstance(other, str):
                    pass
                else:
                    raise TypeError("Time isinstance can't plus the type which is not str or int or float")
        return Time(new_timestamp)

    def __sub__(self, other):
        if isinstance(other, Time):
            timediff = self._Time__timestamp - other._Time__timestamp
            return timediff
        else:
            if isinstance(other, float):
                return Time(self._Time__timestamp - other)
            if isinstance(other, int):
                return Time(self._Time__timestamp - other)
        raise TypeError('Time instance can only sub Time|int|float instance.')

    def __getitem__(self, key):
        if key == 'timestamp':
            return self._Time__timestamp
        else:
            if key == 'datetime':
                return self.fmt('%Y-%m-%d %H:%M:%S')
            return

    def __setitem__(self, key, value):
        if key == 'timestamp':
            self._Time__timestamp = value
        else:
            if key == 'datetime':
                fmt = get_strdate_format(value)
                if fmt is not None:
                    timeArray = time.strptime(value, fmt)
                    self._Time__timestamp = time.mktime(timeArray)
                else:
                    raise TypeError('Time format is not ok!')
            else:
                raise ValueError('Only datetime or timestamp can be accepted!')


class Timeseries:

    def __init__(self, *args):
        self._Timeseries__end_time = None
        self._Timeseries__level = 0
        self._Timeseries__freq = 86400
        self._Timeseries__list = []
        self._Timeseries__length = 1
        if len(args) == 0:
            self._Timeseries__end_time = Time()
            first_day = get_month_firstday_Time(self._Timeseries__end_time)
            self._Timeseries__length = int((self._Timeseries__end_time - first_day) / 86400)
            for i in range(self._Timeseries__length):
                self._Timeseries__list.append(self._Timeseries__end_time - (self._Timeseries__length - i) * 86400)

            self._Timeseries__list.append(self._Timeseries__end_time)
        else:
            if len(args) == 1:
                self._Timeseries__end_time = Time(args[0])
                first_day = get_month_firstday_Time(self._Timeseries__end_time)
                self._Timeseries__length = int((self._Timeseries__end_time - first_day) / 86400)
                for i in range(self._Timeseries__length):
                    print(self._Timeseries__end_time - i * 86400)
                    self._Timeseries__list.append(self._Timeseries__end_time - (self._Timeseries__length - i) * 86400)

                self._Timeseries__list.append(self._Timeseries__end_time)
            else:
                if len(args) == 2:
                    self._Timeseries__end_time = Time(args[0])
                    self._Timeseries__length = args[1]
                    for i in range(self._Timeseries__length):
                        self._Timeseries__list.append(self._Timeseries__end_time - (self._Timeseries__length - i) * 86400)

                    self._Timeseries__list.append(self._Timeseries__end_time)
                else:
                    if len(args) == 3:
                        self._Timeseries__end_time = Time(args[0])
                        self._Timeseries__length = args[1]
                        self._Timeseries__freq = args[2]
                        for i in range(self._Timeseries__length):
                            self._Timeseries__list.append(self._Timeseries__end_time - (self._Timeseries__length - i) * self._Timeseries__freq)

                        self._Timeseries__list.append(self._Timeseries__end_time)
                    else:
                        raise TypeError('1-3 arguments should be given!')

    def fmt(self, fmt):
        return [x.fmt(fmt) for x in self._Timeseries__list]

    def __repr__(self):
        return "['" + "','".join([x.fmt('%Y-%m-%d %H:%M:%S') for x in self._Timeseries__list]) + "']"

    @property
    def length(self):
        return self._Timeseries__length