# -*- coding=utf-8 -*-


import random
from .vdict import vdict 
from .ztime import Time, Timeseries 

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
def rich():
    reds = ["01","02","03","04","05", "06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33"]
    blues =["01","02","03","04","05", "06","07","08","09","10","11","12","13","14","15","16"]
    reds_you_get = []
    try:
        for i in range(6):
            x = random.randint(0,32)
            reds[i],reds[x]=reds[x], reds[i]
    except Exception as e:
        print( i, x)


    reds_you_get=reds[0:6]
    blue = random.choice(blues)
    blue = "['" +str(blue) +"']"
    text='''
我们的口号是：为发财而生
Our Slogan: BORN FOR RICH

      [   ]
(@)==[_____]==(@)
      |* *|
      (_-_)
     /     \\
    /    / 恭 /
__@__   / 喜 /
\\___/  / 发 / \\
  \\   / 财 /  /
   |_________|

   "MONEY GOD"
   Buddha Ruly, Camel God, Jesus God, ... and so on.
   There are seven Gods in this world.
   One God rule them all.
   Knee before the Money God and pray.
   And then you will be rich.
'''
    print( text )
    print("these numbers may make you rich:")
    print( sorted(reds_you_get), blue )


    

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
    ts4 = Timeseries('20200901')
    ts5 = Timeseries('20200430')
    ts6 = Timeseries('20200228')
    ts7 = Timeseries('20200228', 10)
    ts8 = Timeseries('20200228', 10, 60)

    print( 'ts1:', ts1.fmt('%Y-%m-%d') )
    print( 'ts2:', ts2.fmt('%Y-%m-%d') )
    print( 'ts3:', ts3.fmt('%Y-%m-%d') )
    print( 'ts4:', ts4.fmt('%Y-%m-%d') )
    print( 'ts5:', ts5.fmt('%Y-%m-%d') )
    print( 'ts6:', ts6.fmt('%Y-%m-%d') )
    print( 'ts7:', ts7 )
    print( 'ts7:', ts7.fmt('%Y-%m-%d') )
    print( 'ts8:', ts8.fmt('%Y-%m-%d %H:%M:%S'))

    #print( ts )
    rich()