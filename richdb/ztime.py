# -*- encoding=utf8 -*-
import sys
from os.path import dirname, abspath
sys.path.append( dirname( abspath( __file__ ) ) )

import datetime as dt, time, re, calendar, sys
from utils import *
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
'''
class Time
Get current time:
t1 = Time()
t1.fmt('%Y-%m-%d %H:%M:%S') #2022-08-04 10:46:30
t1.fmt('%Y-%m-%d %H:%M:%S.%f') #2022-08-04 10:46:30.100002

Make str to Time(Weak AI Aided Programming WAIAP):

t1 = Time('2022')
t1 = Time('2022-01-02 10:49:22.121233')
t1 = Time('2022-01-01')

#t1 = Time('March 2 1996')
#t1 = Time('March,2,1996')
#t1 = Time('March 2,1996')

#t1 = Time('2 March,1996')
#t1 = Time('2,March,1996')
#t1 = Time('2 March 1996')

#t1 = Time('Mar. 2,1996')
#t1 = Time('Mar 2 1996')
#t1 = Time('Mar. 2 1996')
#t1 = Time('Mar.,2 1996')
#t1 = Time('Mar.,2,1996')

#t1 = Time('Mar2 1996')
#t1 = Time('Mar.2 1996')
#t1 = Time('2Mar. 1996')

#t1 = Time('1989/01/02 12:01:00.10002')
#t1 = Time('1989.01.02 12:01:00.10002')
#t1 = Time('1989 01 02 12:01:00.10002')

Because the USA and England's time different,we have to use US/us or EN/en prefix to help the class.
Maybe all of you think this is not difficult.
But when you design it in the dark road, it is so hard and full of pain.

It is very hard to choose from NLP or RegEx.

#t1 = Time('us01 02 1980 12:00:00.10002')
#t1 = Time('en01 02 1980 12:00:00.10002')

#t1 = Time('en01/02/1980 12:00:00.10002')
#t1 = Time('us01/02/1980 12:00:00.10002')

Get current watch time(Tt is the time from your watch) :
t2 = Time('@') # 19208@02:48:21.6316211
t3 = Time('@-1')# -0@23:59:59.0000000

default 19208 represent the days from utc 1970-01-01 00:00:00.0 to present.

Here is the formula:
Time('@imestamp') = 'D@H:M:S'
H:M:S show the time from pointer of the watch.
Change watch time to seconds.

timestamp = D*86400+(H*60*60+M*60+S)

Time('@-timestamp') = '-D@H:M:S'
timestamp = -D*86400-86400+(H*60*60+M*60+S)

if you use it like this , it is more clear.
Time('@12:23:24.23232')
Time('@-12:23:24.23232')

#Time('-1@12:23:24.23232')
#Time('2@12:23:24.23232')


t1 = Time()
t2 = Time()

Can't make t1+t2, it will raise Exception.


t2-t1 return a watch time Time('@'),Sometimes it is equivalent to timedelta.
But it means the Timer on your Pocket Watch. 
It shows the pointer of the Pocket Watch when press at t1 ,and stop at t2.
It is not very hard to make the logic clear.
Maybe this is ugly, but I can't find a better way.

(t2-t1).timestamp is float
(t2-t1).epoch is wull, if you print it you will see @ in cmd.

but t2.epoch is 1970-01-01 00:00:00.0

Wull is an special class, it is different from None.

t1 = Time()
t2 = Time('@1000')
t1 + t2 == t1 + 1000
t1 + '3D' #add three days to t1
t1 + '3H' #add three hours to t1
t1 + '3min' #add three minutes to t1
t1 + '3S' #add three seconds to t1

'''

class Time:
    '''
        Time init
    '''
    def __init__(self, *args):
        self._Time__timestamp = time.time()
        self.__epoch =0.0
        if len(args) == 0 or args[0]=='':
            return
        if isinstance(args[0], float) or isinstance(args[0],int):
            self._Time__timestamp = float(args[0])
            return
        if isinstance(args[0], datetime):
            self._Time__timestamp = args[0].timestamp()
            return
        if isinstance(args[0], str):
            if '@' in args[0]:
                self.__epoch=WULL
                daystr = args[0].split('@')[0]
                sign=1 
                if '-' in daystr:
                    sign = -1

                days = abs(float(daystr)) if daystr != '' else 0.0

                clocktimestr = args[0].split('@')[1]
                timearr = clocktimestr.split(':')
                tlen = len( timearr )
                ttimestamp = 0.0


                if ':' in clocktimestr:
                    if clocktimestr[0] == '-':
                        sign = -1
                    for i in range(tlen):
                        c = float(timearr[i])

                        if i == 0 and ( abs(c) >=24 ):
                            raise ValueError('Not right time!')
                        if i == 1 and ( c < 0 or c >=60):
                            raise ValueError('Not right time!')
                        if i == 2 and ( c < 0 or c >=60):
                            raise ValueError('Not right time!')
                        if i == 0 :
                            ttimestamp = ttimestamp + abs(c)*60*60
                        if i == 1 :
                            ttimestamp = ttimestamp + abs(c) * 60
                        if i == 2 :
                            ttimestamp = ttimestamp + abs(c)
                    if sign == 1:
                        self._Time__timestamp = ttimestamp * sign + float(days)*86400
                    else:
                        #timestamp = -D*86400-86400+(H*60*60+M*60+S)
                        self._Time__timestamp = ttimestamp+float(days)*86400*sign-86400

                elif tlen >= 1 and clocktimestr != '' :
                    if '-' in clocktimestr:
                        sign = -1
                    self._Time__timestamp = abs(float(clocktimestr))*sign+abs(float(days))*86400*sign
            else:
                fmt = '%Y-%m-%d %H:%M:%S.%f'
                std_date_str = get_std_datestr(args[0])
                if '.' in std_date_str:
                    gsecond = std_date_str.split('.')[0]
                    lsecond = std_date_str.split('.')[1]
                else:
                    gsecond = std_date_str
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
        return self.__epoch
    
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
        if not iswull(self.__epoch):
            return Time(self._Time__timestamp + hours * 60 * 60)
        else:
            return Time('@'+str( self._Time__timestamp + hours * 60 * 60 ) )

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
        return (self - other) / 60.0 / 60.0 / 24.0

    def __repr__(self):
        if iswull(self.epoch):
            day = ( self._Time__timestamp/86400 )
            daystr = str(int(day))

            hour = ( self._Time__timestamp%86400 )/3600
            hourstr = '{:0>2d}'.format(int(hour))

            minute = ( (self._Time__timestamp%86400)%3600 )/60
            minutestr = '{:0>2d}'.format(int(minute))

            second = round (  ( (self._Time__timestamp%86400)%3600 ) % 60 , 7 )
            secondstr =  '{:0>10.7f}'.format(second)
            if self._Time__timestamp <0 and abs(self._Time__timestamp)<86400:
                return '<Time:' + '-0' +'@'+ hourstr + ':' + minutestr +':' +secondstr+'>'
            return '<Time:' + daystr +'@'+ hourstr + ':' + minutestr +':' +secondstr+'>'
        else:
            return '<Time:' + self.fmt('%Y-%m-%d %H:%M:%S.%f') + '>'

    def __str__(self):
        if iswull(self.epoch):
            day = ( self._Time__timestamp/86400 )
            daystr = str(int(day))

            hour = ( self._Time__timestamp%86400 )/3600
            hourstr = '{:0>2d}'.format(int(hour))

            minute = ( (self._Time__timestamp%86400)%3600 )/60
            minutestr = '{:0>2d}'.format(int(minute))

            second = round (  ( (self._Time__timestamp%86400)%3600 ) % 60 , 7 )
            secondstr =  '{:0>10.7f}'.format(second)

            if self._Time__timestamp <0 and abs(self._Time__timestamp)<86400:
                return '-0' +'@'+ hourstr + ':' + minutestr +':' +secondstr
            return daystr +'@'+ hourstr + ':' + minutestr +':' +secondstr
        else:
            return self.fmt('%Y-%m-%d %H:%M:%S.%f')

    def __add__(self, other):
        if isinstance(other, int):
            new_timestamp = self._Time__timestamp + float(other)
        else:
            if isinstance(other, float) or isinstance(other, int):
                new_timestamp = self._Time__timestamp + float(other)
            else:
                if isinstance(other, str):
                    #to do D H M S 
                    if 'D' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('D') )*24*60*60 )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('D') )*24*60*60))

                    if 'H' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('H') )*60*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('H') )*60*60))

                    if 'min' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('min') )*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('min') )*60))

                    if 'S' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('S') )  )
                        else :
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('S') )))

                if isinstance(other, Time):
                    if not iswull(self.__epoch) and not iswull(other.epoch):
                        raise ValueError('All of the two time epoch is wull')

                    elif iswull(self.__epoch) and not iswull(other.epoch): 
                        new_timestamp = self._Time__timestamp + other.timestamp

                    elif not iswull(self.__epoch) and iswull(other.epoch): 
                        new_timestamp = self._Time__timestamp + other.timestamp

                    elif iswull(self.__epoch) and iswull(other.epoch):
                        new_timestamp = self._Time__timestamp + other.timestamp
                        return Time('@'+str(new_timestamp))
                else:
                    raise TypeError("Time isinstance can't plus the type which is not str or int or float")

        return Time(new_timestamp)

    def __sub__(self, other):
        if isinstance(other, Time):
            timediff = self._Time__timestamp - other._Time__timestamp
            if not iswull(self.__epoch) and not iswull(other.epoch):
                return Time('@'+str(timediff))

            elif iswull(self.__epoch) and not iswull(other.epoch): 
                return Time(timediff)

            elif not iswull(self.__epoch) and iswull(other.epoch): 
                return Time(timediff)

            elif iswull(self.__epoch) and iswull(other.epoch):
                return Time('@'+str(timediff))
        else:
            if isinstance(other, float):
                return Time(self._Time__timestamp - other)
            if isinstance(other, int):
                return Time(self._Time__timestamp - other)
            if isinstance(other, str):
                #to do D H M S 
                if 'D' in other:
                    return Time( self._Time__timestamp- float(other.strip('D') )*24*60*60 )
                if 'H' in other:
                    return Time( self._Time__timestamp- float(other.strip('H') )*60*60  )
                if 'min' in other:
                    return Time( self._Time__timestamp- float(other.strip('min') )*60  )
                if 'S' in other:
                    return Time( self._Time__timestamp- float(other.strip('S') )  )

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
