import datetime as dt
import time
import re
import calendar

'''
这个包的设计是模仿pathlib的，我们管这种设计方式叫基于群论的软件工程设计方法。
this package is designed follow the pathlib's design method
we call this kind design method : software design base on group theory

群的性质越完备越好，则类的设计越好。
将群论引入软件工程有助于量化评估代码质量，我们经常无法解决的问题是什么代码算好的问题，缺乏一个量化的指标。
这是python和C++语言的魅力，未来语言应该怎样设计呢？

时间序列是数据处理中非常重要的领域，数据管理工程中很重要的原则就是一手数据源原则。
this package contains another design method. 
一手数据源原则，避免计算列，所有的日期都是由时间戳获得，这是数据处理中最重要的原则之一。
一手数据源原则，就是A数据集由B数据集计算得来，但是为了避免A数据集计算错误和时间差造成的不一致，通常C计算集都是由A计算得来。
这有个概率公式A->B->C A->B出错的概率为a B->C出错的概率为b, 
C数据集会因为数据错误的概率会因为传递而导致增加( sum(A)*a*(1-b) + sum(B)*b ) /sum(B)。
当我们选择接口或者数据嵌套时，就需要深度评估，尤其加强测试。
'''



'''
argument support 
Time(float|date) =
timestamp:
    float:
        1212323123.12010
date:
    str:
        '20210102'
        '2021-01-02'
        '2021/01/02'

        '20210102 12'
        '2021-01-02 12'
        '2021/01/02 12'

        '20210102 12:12'
        '2021-01-02 12:12'
        '2021/01/02 12:12'

        '20210102 12:12:12'
        '2021-01-02 12:12:12'
        '2021/01/02 12:12:12'

        '20210102 12:12:12.100000'      
        '2021-01-02 12:12:12.1000000'   
        '2021/01/02 12:12:12.1000290'   
'''

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

class Time():
    def __init__(self, *args):
        fmt = ""
        if len(args)>1 :
            raise ValueError('Only one or zero argument is needed!')

        elif len(args) == 0:
            self.__timestamp = time.time()
            return

        elif isinstance( args[0] , float):
            self.__timestamp = args[0]
            print( args[0] )
            return 

        elif isinstance( args[0], str):
            fmt = get_strdate_format(args[0])
            if fmt is not None:
                timeArray = time.strptime( args[0], fmt)
                self.__timestamp = time.mktime( timeArray)
        else:
            self.__timestamp = time.time()


    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def year(self):
        return dt.datetime.fromtimestamp(self.__timestamp).year

    @property
    def month(self):
        return dt.datetime.fromtimestamp(self.__timestamp).month

    @property
    def day(self):
        return dt.datetime.fromtimestamp(self.__timestamp).day
    
    @property
    def week(self):
        return dt.datetime.fromtimestamp(self.__timestamp).week

    def fmt(self, fmt):
        return time.strftime( fmt , time.localtime(self.__timestamp) )
    
    
    def __repr__(self):
        return str( self.__timestamp )

    def __add__(self,other):
        if isinstance(other,int):
            new_timestamp = self.__timestamp + float(other)
        elif isinstance(other,float):
            new_timestamp = self.__timestamp + orther
        elif isinstance(other, str):
           pass
        else:
            raise TypeError("Time isinstance can't plus the type which is not str or int or float") 
        return Time(new_timestamp) 
 
    def __sub__(self,other):
        print( self, other )
        if isinstance(other, Time):
            timediff = self.__timestamp - other.__timestamp
            return timediff
        elif isinstance(other, float):
            return Time(self.__timestamp - other) 
        elif isinstance(other, int):
            return Time(self.__timestamp - other) 
        else:
           raise TypeError("Time isinstance can only sub Time|int|float isinstance") 

'''
util time static method class

'''
def get_month_firstday_Time(t):
    this_month_firstday = dt.datetime(t.year,t.month, 1)
    return Time(this_month_firstday.strftime('%Y-%m-%d %H:%M:%S'))

'''
util time static method class

'''
def get_month_lastday_Time(t):
    this_month_lastday = calendar.monthrange(t.year, t.month)[1]
    return Time( dt.datetime(t.year, t.month, this_month_lastday).strftime('%Y-%m-%d %H:%M:%S') )



'''
argument Timeseries(end,length,freq)

start  : Time() -> time series start time
length : int    -> time series length
freq   : float  -> time unit (default 86400 second), you can input any second value for example 10.1 second

Timeseries()                      -> current month day series
Timeseries( end_time )                 -> end day to the first day of the month of the end
Timeseries( end_time, length )         -> end day backtrace the length days
Timeseries( end_time, length, freq )   -> end day backtrace the length with freqs 
'''

class Timeseries():
    def __init__(self, *args):

        self.__end_time=None
        self.__level = 0
        self.__freq  = 86400
        self.__list  = [] 
        self.__length = 1 

        if len(args) == 0:
            self.__end_time = Time()

            first_day = get_month_firstday_Time(self.__end_time)
            self.__length =int( (self.__end_time - first_day)/86400 )
            print( 'self.__length is ', self.__length)

            for i in range(self.__length):
                print( self.__end_time - i*86400 )
                self.__list.append( self.__end_time -(self.__length- i)*86400 )
            self.__list.append(self.__end_time)
            print( self.__list )

        if len(args) >= 1:
            self.__end_time = Time(args[0])
            first_day = get_month_firstday_Time(self.__end_time)
            self.__length = int( (self.__end_time - first_day)/86400 )

            for i in range(self.__length):
                print( self.__end_time - i*86400 )
                self.__list.append( self.__end_time - (self.__length - i)*86400 )
            self.__list.append(self.__end_time)

        if len(args) >= 2:
            self.__end_time =Time(args[0])
            self.__length = args[1] # default freq is day=24*60*60=86400 
            for i in range(self.__length):
                self.__list.append( self.__end_time -(self.__length - i)*86400 )
            self.__list.append(self.__end_time)

        if len(args) >= 3: # 
            self.__end_time = args[0]
            self.__length = args[1]
            self.__freq = args[2]
            for i in range(self.__length):
                self.__list.append( self.__end_time - (self.__length - i )*self.__freq )
            self.__list.append(self.__end_time)

    def fmt(self, fmt):
        return [x.fmt(fmt) for x in self.__list]

    @property
    def length(self):
        return self.__length
    

if __name__=='__main__':
    #t1 = Time(30000)
    #t2 = Time(1000)
    #t979 = Time(1)
    #t989 = Time(0)
    #t999 = Time(-1)

    #t3 = Time('2022-01-05 12:12:12.1')
    #t909 = Time('2022-01-05 12:12:12.000001')
    #t4 = Time('2022.01.05 12:12:12.000001')
    #t5 = Time('2022/01/05 12:12:12.000001')
    #t6 = Time('20220105 12:12:12.000001')

    #t99 = Time('2022')
    #t99 = Time('202201')
    #t7  = Time('20220105')
    #t8  = Time('20220105 12')
    #t9  = Time('20220105 12:12')
    #t10 = Time('20220105 12:12:13')

    #t22 = Time('2022')
    #t23 = Time('2022-01')
    #t11 = Time('2022-01-05')
    #t12 = Time('2022-01-05 12')
    #t13 = Time('2022-01-05 12:12')
    #t14 = Time('2022-01-05 12:12:13')

    #t25 = Time('2022')
    #t26 = Time('2022.01')
    #t15 = Time('2022.01.05')
    #t16 = Time('2022.01.05 12')
    #t17 = Time('2022.01.05 12:12')
    #t17 = Time('2022.01.05 12:12:13')
    #print( 't17 time format %Y-%m-%d %H:%M:%S ', t17.fmt( '%Y-%m-%d %H:%M:%S' ))

    print( ' t18 is created ! ')
    t18 = Time()
    print( ' t18 init end ')

    print( ' the lastday  begin ')
    print( 't18 the lastday of 2022.01.12 is : ', get_month_lastday_Time(t18).fmt('%Y-%m-%d %H:%M:%S') )
    print( 'the lastday end')

    print( 'the first day begin')
    print( 't18 the first day of 2022.01.12 is :', get_month_firstday_Time(t18).fmt('%Y-%m-%d %H:%M:%S') )
    print( 'the first day end')

    #print( t1 )
    #print( t2 )
    #print( t1 - t2 )
    #print( t1.timestamp )
    #print( t2.timestamp )
    #print( t1 + 100 )
    #print( t1 + 20000 )

    #print( 'day is :', t1.day)
    #print( 'month is :', t1.month)
    #print( 'year is :', t1.year)
    #print( 'week is :', t1.week)

    ts1 = Timeseries()
    ts2 = Timeseries('20210101')
    ts3 = Timeseries('20210131')
    print( ts1.fmt('%Y-%m-%d') )
    print( ts2.fmt('%Y-%m-%d'))
    print( ts3.fmt('%Y-%m-%d'))

    #print( ts )
