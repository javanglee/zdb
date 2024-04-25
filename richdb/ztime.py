# -*- encoding=utf8 -*-
import sys

import datetime as dt, time, re, calendar, sys
from .utils import *
from .wull import wull, iswull, WULL
from datetime import datetime

if sys.version_info.major >=3 and sys.version_info.minor>=8:
    clocktime = time.perf_counter
    process_time = time.process_time
    process_time_ns = time.process_time_ns
else:
    clocktime = time.clock
    process_time = time.clock
    process_time_ns = time.clock

'''
class Time
Get current time:
t1 = Time()
t1.fmt('%Y-%m-%d %H:%M:%S') #2022-08-04 10:46:30
t1.fmt('%Y-%m-%d %H:%M:%S.%f') #2022-08-04 10:46:30.100002

Make str to Time(Weak AI Aided Programming WAIAP):
t = Time('20120103') + Time('12:12:12.003')
t1 = Time('2022')
t1 = Time('2022-01-02 10:49:22.121233')
t1 = Time('2022-01-01')

t1 = Time('March 2 1996')
t1 = Time('March,2,1996')
t1 = Time('March 2,1996')

t1 = Time('2 March,1996')
t1 = Time('2,March,1996')
t1 = Time('2 March 1996')

t1 = Time('Mar. 2,1996')
t1 = Time('Mar 2 1996')
t1 = Time('Mar. 2 1996')
t1 = Time('Mar.,2 1996')
t1 = Time('Mar.,2,1996')

t1 = Time('Mar2 1996')
t1 = Time('Mar.2 1996')
t1 = Time('2Mar. 1996')

t1 = Time('1989/01/02 12:01:00.10002')
t1 = Time('1989.01.02 12:01:00.10002')
t1 = Time('1989 01 02 12:01:00.10002')

Because the USA and England's time different,we have to use US/us or EN/en prefix to help the class.
Maybe all of you think this is not difficult.
But when you design it in the dark road, it is so hard and full of pain.

It is very hard to choose from NLP or RegEx.

t1 = Time('us01 02 1980 12:00:00.10002')
t1 = Time('en01 02 1980 12:00:00.10002')

t1 = Time('en01/02/1980 12:00:00.10002')
t1 = Time('us01/02/1980 12:00:00.10002')

Get current watch time(Tt is the time from your watch) :
t2 = Time('@') # 19208@02:48:21.6316211
t3 = Time('@-1')# -0@23:59:59.0000000

default 19208 represent the days from utc 1970-01-01 00:00:00.0 to present.

Here is the formula:
#this design is very beatiful
Time('@timestamp') = 'D@H:M:S'
H:M:S show the time from pointer of the watch.
Change watch time to seconds.

timestamp = D*86400+(H*60*60+M*60+S)

Time('@-timestamp') = '-D@H:M:S'
timestamp = -D*86400-86400+(H*60*60+M*60+S)

if you use it like this , it is more clear.
Time('@12:23:24.23232')
Time('@-12:23:24.23232')

Time('-1@12:23:24.23232')
Time('2@12:23:24.23232')


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
t1 + '3M' #add three month to t1

'''
EPOCH=0.0

class Time:
    '''
        Time init
    '''
    def __init__(self, *args, fmt=WULL):
        self._Time__timestamp = time.time()
        self.__epoch = EPOCH
        if len(args) == 0 or args[0]=='':
            return
        if isinstance(args[0], float) or isinstance(args[0],int):
            self._Time__timestamp = round( float(args[0]), 6)
            return
        if isinstance(args[0], datetime):
            self._Time__timestamp = args[0].timestamp()
            return
        if isinstance(args[0], str):
            if not iswull(fmt):
                fsecond = float( '0.'+args[0].split('.')[-1] )
                datestr = '.'.join(args[0].split('.')[0:-1])
                fmt_without_f = '.'.join(fmt.split('.')[0:-1])
                dtime = dt.datetime.strptime( datestr, fmt_without_f)
                epoch = dt.datetime(1970, 1, 1)
                stamp_seconds = (dtime - epoch).total_seconds()
                if '.%f' in fmt:
                    self._Time__timestamp = round(stamp_seconds+fsecond,6)
                else:
                    self._Time__timestamp = stamp_seconds
                return

            if '@' in args[0]:
                self.__epoch=WULL

                #Time('@')
                if args[0].strip() == '@' :
                    return

                daystr = args[0].split('@')[0]
                secstr = args[0].split('@')[1]


                #Time('1@'), Time('-1@') 
                if secstr == '' and daystr != '':
                    self._Time__timestamp = float(daystr)*86400
                    return

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
                std_date_str, self.__epoch = get_std_datestr(args[0])
                if iswull(std_date_str):
                    raise ValueError('The date str {0} format is not supported !'.format(args[0]) )
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
                self._Time__timestamp = round( stamp_seconds + fsecond , 6)
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
        if iswull(self.__epoch):
            return WULL
        return int( self.fmt('%Y') )

    @property
    def month(self):
        if iswull(self.__epoch):
            return WULL
        return  int( self.fmt('%m') )

    @property
    def day(self):
        if iswull(self.__epoch):
            return int( self.__str__().split('@')[0])
        else:
            return int( self.fmt('%d') )

    @property
    def week(self):
        if iswull(self.__epoch):
            return WULL
        return int(self._Time__timestamp/86400 + 4 ) %7

    @classmethod
    def clock(cls):
        return clocktime()

    @classmethod
    def process_time(cls):
        return process_time()

    @classmethod
    def process_time_ns(cls):
        return process_time_ns()
        
    @classmethod
    def sleep(cls, second):
        time.sleep(second)

    @classmethod
    def local(cls):
        return time.ctime()

    def isleapyear(self):
        if iswull(self.__epoch):
            return WULL

        if self.year %400 == 0:
            return True
        if self.year %100 !=0 and self.year %4 == 0:
            return True
        return False

    def add_n_month(self, n):
        year = self.year
        month = self.month
        day = self.day
        DAY = day
        isleap = self.isleapyear()

        for i in range(n):
            if month == 12:
                month = 1
                year = year + 1
            else:
                month = month + 1

            if month == 1 or month == 3 or month == 7 or month == 8 or month == 10 or month ==12 :
                day = DAY
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if DAY == 31:
                    day = 30
            if month == 2:
                if leapyear(year):
                    if DAY >=29:
                        day = 29

                elif DAY >= 29:
                    day = 28
        return Time( str(year).rjust(4,'0')+'-'+str(month).rjust(2,'0') + '-' + str(day).rjust(2,'0') +' ' + self.fmt('%H:%M:%S.%f') )

    def sub_n_month(self, n):
        year = self.year
        month = self.month
        day = self.day
        DAY = day
        isleap = self.isleapyear()

        for i in range(n):
            if month == 1:
                month = 12 
                year = year - 1
            else:
                month = month - 1

            if month == 1 or month == 3 or month == 7 or month == 8 or month == 10 or month == 12:
                day = DAY
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if DAY == 31:
                    day = 30
            if month == 2:
                if leapyear(year):
                    if DAY >=29:
                        day = 29 
                elif DAY >= 29:
                    day = 28
        return Time( str(year).rjust(4,'0')+'-'+str(month).rjust(2,'0') + '-' + str(day).rjust(2,'0') +' ' + self.fmt('%H:%M:%S.%f') )

    def monthlastday(self):
        year = self.year
        month = self.month
        day = self.day
        isleap = self.isleapyear()

        if month == 1 or month == 3 or month == 7 or month == 8 or month == 10 or month == 12:
            day = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day = 30
        if month ==2 :
            if isleap:
                day = 29
            else:
                day = 28

        return Time( str(year).rjust(4,'0')+'-'+str(month).rjust(2,'0') + '-' + str(day).rjust(2,'0') +' ' + self.fmt('%H:%M:%S.%f') )

    def monthfirstday(self):
        year = self.year
        month = self.month
        day = 1
        isleap = self.isleapyear()
        return Time( str(year).rjust(4,'0')+'-'+str(month).rjust(2,'0') + '-' + str(day).rjust(2,'0') +' ' + self.fmt('%H:%M:%S.%f') )

    def daystartsecond(self):
        return Time(self.fmt('%Y-%m-%d'))

    def dayendsecond(self):
        return Time( (self+'1D').fmt('%Y-%m-%d') )+Time('@-1')

    def timezone(self, utc):
        utc=utc.upper()
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

    def __repr__(self):
        if iswull(self.epoch):
            day = ( self._Time__timestamp/86400 )
            daystr = str(int(day))

            hour = ( self._Time__timestamp%86400 )/3600
            hourstr = '{:0>2d}'.format(int(hour))

            minute = ( (self._Time__timestamp%86400)%3600 )/60
            minutestr = '{:0>2d}'.format(int(minute))

            second = ( (self._Time__timestamp%86400)%3600 ) % 60 

            secondstr =  '{:0>12.9f}'.format(second)

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

            second =  ( (self._Time__timestamp%86400)%3600 ) % 60 
            
            secondstr =  '{:0>12.9f}'.format(second)

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

                    if 'Q' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('Q') )*15*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('Q') )*15*60))

                    if 'dong' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('dong') )*2*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('dong') )*2*60))

                    if 'lei' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('lei') )*12  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('lei') )*12))


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

                    if 'M' in other:
                        if not iswull( self.__epoch ):
                            month = int( other.strip('M') )
                            monthfloat = float( other.strip('M') )
                            if monthfloat - month > 0:
                                raise ValueError('add or sub Month should use int type')
                            return self.add_n_month( month )
                        else:
                            raise ValueError("Time('@') is can't add month.")

                    if '秒' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('秒') )  )
                        else :
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('秒') )))

                    if '分' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('分') )*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('分') )*60))

                    if '时' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('时') )*60*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('时') )*60*60))

                    if '刻' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('刻') )*15*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('刻') )*15*60))

                    if '东' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('东') )*2*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('东') )*2*60))

                    if '雷' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('雷') )*12  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('雷') )*12))

                    if '时辰' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('时辰') )*2*60*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('时辰') )*2*60*60))

                    if '天' in other:
                        if not iswull( self.__epoch ):
                            return Time( self._Time__timestamp+ float(other.strip('天') )*24*60*60  )
                        else:
                            return Time('@'+str(self._Time__timestamp+ float(other.strip('天') )*24*60*60))

                    if '月' in other:
                        if not iswull( self.__epoch ):
                            month = int( other.strip('月') )
                            monthfloat = float( other.strip('月') )
                            if monthfloat - month > 0:
                                raise ValueError('add or sub Month should use int type')
                            return self.add_n_month( month )
                        else:
                            raise ValueError("Time('@') is can't add month.")

                if isinstance(other, Time):
                    if not iswull(self.__epoch) and not iswull(other.epoch):
                        raise ValueError('None of the two time epoch is wull')

                    elif iswull(self.__epoch) and not iswull(other.epoch): 
                        new_timestamp = self._Time__timestamp + other.timestamp

                    elif not iswull(self.__epoch) and iswull(other.epoch): 
                        new_timestamp = self._Time__timestamp + other.timestamp

                    elif iswull(self.__epoch) and iswull(other.epoch):
                        new_timestamp = self._Time__timestamp + other.timestamp
                        return Time('@'+str(new_timestamp))
                else:
                    raise TypeError("Time isinstance can't plus the type which is not str|int|float|Time")

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
                if 'Q' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('Q') )*15*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('Q') )*15*60))
                if 'dong' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('dong') )*2*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('dong') )*2*60))

                if 'lei' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp- float(other.strip('lei') )*12  )
                    else:
                        return Time('@'+str(self._Time__timestamp- float(other.strip('lei') )*12))

                if 'min' in other:
                    return Time( self._Time__timestamp- float(other.strip('min') )*60  )
                if 'S' in other:
                    return Time( self._Time__timestamp- float(other.strip('S') )  )

                if 'M' in other:
                    if not iswull( self.__epoch ):
                        month = int( other.strip('M') )
                        monthfloat = float( other.strip('M') )

                        if monthfloat - month > 0:
                            raise ValueError('add or sub Month should use int type')
                        return self.sub_n_month( month )
                    else:
                        raise ValueError("Time('@') is can't sub month.")

                if '秒' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('秒') )  )
                    else :
                        return Time('@'+str(self._Time__timestamp - float(other.strip('秒') )))

                if '分' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('分') )*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('分') )*60))

                if '时' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('时') )*60*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('时') )*60*60))

                if '刻' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('刻') )*15*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('刻') )*15*60))

                if '东' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('东') )*2*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('东') )*2*60))

                if '雷' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp- float(other.strip('雷') )*12  )
                    else:
                        return Time('@'+str(self._Time__timestamp- float(other.strip('雷') )*12))


                if '时辰' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('时辰') )*2*60*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('时辰') )*2*60*60))

                if '天' in other:
                    if not iswull( self.__epoch ):
                        return Time( self._Time__timestamp - float(other.strip('天') )*24*60*60  )
                    else:
                        return Time('@'+str(self._Time__timestamp - float(other.strip('天') )*24*60*60))

                if '月' in other:
                    if not iswull( self.__epoch ):
                        month = int( other.strip('月') )
                        monthfloat = float( other.strip('月') )
                        if monthfloat - month > 0:
                            raise ValueError('add or sub Month should use int type')
                        return self.sub_n_month( month )
                    else:
                        raise ValueError("Time('@') is can't add month.")

        raise TypeError('Time instance can only sub Time|int|float|str instance.')

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

    def __eq__(self, other):
        if isinstance(other, float):
            if self.timestamp == other:
                return True
        if isinstance(other, int):
            if self.timestamp == float(other):
                return True
        if isinstance(other, str):
            if self.timestamp == Time(other).timestamp:
                return True
        if isinstance(other, Time):
            if self.timestamp == other.timestamp and other.epoch == self.epoch:
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, float):
            if self.timestamp != other:
                return True
        if isinstance(other, int):
            if self.timestamp != float(other):
                return True
        if isinstance(other, str):
            if self.timestamp != Time(other).timestamp:
                return True
        if isinstance(other, Time):
            if self.timestamp != other.timestamp and other.epoch == self.epoch:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, float):
            if self.timestamp < other:
                return True
        if isinstance(other, int):
            if self.timestamp < float(other):
                return True
        if isinstance(other, str):
            if self.timestamp < Time(other).timestamp:
                return True
        if isinstance(other, Time):
            if self.timestamp < other.timestamp and other.epoch == self.epoch:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, float):
            if self.timestamp > other:
                return True
        if isinstance(other, int):
            if self.timestamp > float(other):
                return True
        if isinstance(other, str):
            if self.timestamp > Time(other).timestamp:
                return True
        if isinstance(other, Time):
            if self.timestamp > other.timestamp and other.epoch == self.epoch:
                return True
        return False

    def __le__(self, other):
        if isinstance(other, float):
            if self.timestamp <= other:
                return True
        if isinstance(other, int):
            if self.timestamp <= float(other):
                return True
        if isinstance(other, str):
            if self.timestamp <= Time(other).timestamp:
                return True
        if isinstance(other, Time):
            if self.timestamp <= other.timestamp and other.epoch == self.epoch:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, float):
            if self.timestamp >= other:
                return True
        if isinstance(other, int):
            if self.timestamp >= float(other):
                return True
        if isinstance(other, str):
            if self.timestamp >= Time(other).timestamp:
                return True
        if isinstance(other, Time):
            if self.timestamp >= other.timestamp and other.epoch == self.epoch:
                return True
        return False

    def __hash__(self):
        return hash(id(self))

    def __bool__(self):
        return True

    #orange step standard    
    @property
    def defaultstep(self):
        return '1D'

def orange(start, end, step=None):
    defaultstep = 1 if not hasattr(start, 'defaultstep') else start.defaultstep
    step = step if step is not None else defaultstep
    
    while( start < end ):
        yield start
        start = start + step

def fmt(l, fmt='%Y-%m-%d %H:%M:%S'):
    for i in l:
        yield i.fmt(fmt)

class Timeslice():
    pass

class Times:
    '''
        Times 
    '''
    @classmethod
    def timelist(cls, starttime, endtime, interval=None, freq='1D'):
        pass
