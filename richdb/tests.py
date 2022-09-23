# -*- encoding=utf8 -*-
import sys
from pathlib import Path
sys.path.append( Path( __file__ ).resolve().parent )

from mdict import mdict
from wull import wull, iswull, WULL
import pytest
from ztime import Time
import time

def test_wull():
    a = WULL
    assert iswull(a) == True
    assert not iswull(a) == False

    assert a+1   == 1
    assert a-1   == -1
    assert 1-a   == 1
    assert -1-a  == -1
    assert 1 + a == 1
    assert 1-a   == 1

    assert a*2 == a
    assert a/2 == a
    assert 2/a == a
    assert 2*a == a

    assert 2+a+3-a+4==9
    assert 2-a-4 == -2

    assert abs(a) == a
    assert (1>a) == True
    assert (0>a) == True
    assert (-1>a) == True
    
    assert (a>-1) ==  False
    assert (a>1) ==  False
    assert (a>0) ==  False
    assert str(a) == '@'


def test_mdict():
    #block 1 key in main dict and value in mirror dict and dict[key] == value
    a = mdict()
    a[1]=2
    a[1]=2
    assert a[1] == 2
    assert a[2] == 1 

    #block 2 key not in main dict and value not in mirror dict
    a = mdict()
    a[1] = 2
    a[2] = 3
    assert a[1] == 2 
    assert a[2] != 1 
    assert a[2] == 3 
    assert a[3] == 2 

    #block 3 value in mirror dict and key not in main dict
    a=mdict()
    a[None] = 10
    a[1] = 2
    a[3] = 2 
    a[None] =  None
    assert a[3] == 2
    assert a[2] == 3
    assert a[None] == None


    #block 4 key in main dict and value not in mirror dict
    b = mdict()
    b[1] = 2
    b[3] = 4
    b[4] = 5
    b[4] = 6 
    b[4] = None
    assert b[1] == 2
    assert b[2] ==  1 

    assert b[3] == 4 
    assert b[4] == None 
    assert b[None] == 4 
def test_vdict():

    pass
def test_Time_init():
    t1 = Time()
    t2 = time.time()

    assert abs(t1.timestamp - t2) <0.000000001 

    t1 = Time(-1.1)
    assert t1.fmt('%Y-%m-%d %H:%M:%S') == '1969-12-31 23:59:58'

    t2 = Time('1969-12-31 23:59:58.9')
    assert t1.timestamp == t2.timestamp

    t3 = Time(-0.1)
    assert t3.timestamp == -0.1

    t4 = Time('1970-01-01')
    assert t4.timestamp == 0.0

    t1 = Time(0.0)
    assert t1.fmt('%Y-%m-%d %H:%M:%S') == '1970-01-01 00:00:00'

    t1=Time('1970-01-01 00:00:00')
    assert t1.timestamp == 0.0

    #t1=Time('1970_01_01 00.00.00')
    #assert t1.timestamp == 0.0

    t1 = Time('@-1')
    assert str(t1)=='-0@23:59:59.000000000'

    t1 = Time('@0')
    assert str(t1)=='0@00:00:00.000000000'
    
    t1=Time('1970-1-1 0:0:0')
    assert t1.timestamp == 0.0

    t1=Time('1970/1/1 0:0:0')
    assert t1.timestamp == 0.0

    t1=Time('1970/01/01 00:00:00')
    assert t1.timestamp == 0.0

    t1=Time('1970年01月01日 00:00:00')
    assert t1.timestamp == 0.0

    t1=Time('1970年1月1日 00:00:00')
    assert t1.timestamp == 0.0

    t1=Time('19700101 00:00:00')
    assert t1.timestamp == 0.0

    t1=Time('197001 00:00:00')
    assert t1.timestamp == 0.0

    t1=Time('1970 00:00:00')
    assert t1.timestamp == 0.0

    t1 = Time('1970')
    assert t1.timestamp == 0.0

    #t1= Time('12:12:12.1212 2021/01/01') is this needed?
    #assert str(t1) == '2021-01-01 12:12:12.1212'

    #t1= Time('12:12:12 2021/01/01')
    #assert str(t1) == '2021-01-01 12:12:12.0'

    t = Time('/12/2012')
    assert str(t) == '2012-12-01 00:00:00.0'
    
    t=Time('us01/12/2012')
    t=Time('12/2012')
    t=Time('12 2012')

    #t=Time('01 12 2012')
    #t=Time('01-12-2012')

    t=Time('us01-12-2012')
    assert( str(t) == '2012-01-12 00:00:00.0')
    t=Time('/2021/01/01/')
    t=Time('2021/01/01')
    t=Time('2012')
    assert str( Time('23:59:59') ) == '0@23:59:59.000000000'
    assert str( Time('19120101') + Time('23:59:59')) == '1912-01-01 23:59:59.0'
    assert str( Time('1970') + Time('@-1') ) == '1969-12-31 23:59:59.0'
    assert str( Time('1970') + Time('@-12:00:00') ) == '1969-12-31 12:00:00.0'
    assert str( Time('19700101') + Time('@-11:00:00') ) == '1969-12-31 11:00:00.0'

    #str(Time('24:00:00')) == '0@23:59.59.0'
    #assert str( Time('2012 01 02 12.12.12.12') ) == '2012-01-02 12:12:12.12'
    assert str( Time('12:12:12.1212') + Time('2021/01/01') ) == str( Time('2021/01/01 12:12:12.1212') )
    assert str( Time('20000228')+'1D' ) == '2000-02-29 00:00:00.0'
    assert str( Time('20010228')+'1D' ) == '2001-03-01 00:00:00.0'
    assert str( Time('20011130')+'1D' ) == '2001-12-01 00:00:00.0'
    assert str( Time('20011129')+'1D' ) == '2001-11-30 00:00:00.0'
    assert str( Time('20011231')+'1D' ) == '2002-01-01 00:00:00.0'
    assert str( Time('2008') ) == '2008-01-01 00:00:00.0'

    #Time('20000228') - Time('20000227')
    assert ( str( Time('2012 11-11 10:10:10.0') ) == '2012-11-11 10:10:10.0' ) 
    assert ( str( Time('2012-11-5 10:10:10.0') ) == '2012-11-05 10:10:10.0' ) 
    assert ( str( Time('2012-11-5 23:39:47.99999') ) == '2012-11-05 23:39:47.99999' ) 
    assert ( str( Time('2012-11-5 23:39:47.99999') ) == '2012-11-05 23:39:47.99999' ) 
    assert ( str( Time('2012/11/5 23:39:47.99999') ) == '2012-11-05 23:39:47.99999' ) 
    assert ( str( Time('2012...11...5 23:39:47.99999') ) == '2012-11-05 23:39:47.99999' ) 
    assert ( str( Time('2012...02...28 23:59:59.99999') ) == '2012-02-28 23:59:59.99999' ) 
    assert ( str( Time('us02-28-2012 23:59:59.99999') ) == '2012-02-28 23:59:59.99999' ) 
    assert ( str( Time('2012年的2月28日 23:59:59.99999') ) == '2012-02-28 23:59:59.99999' ) 
    assert ( str( Time('2012.2.28 23:59:59.99999') ) == '2012-02-28 23:59:59.99999' ) 
    #assert ( str( Time('us02282012 23:59:59.99999') ) == '2012-02-28 23:59:59.99999' ) 
    #assert(  str( Time('02012012 23:59:59.99999') )  )
    assert(  str( Time('19201212 23:59:59.99999') )=='1920-12-12 23:59:59.99999'  )

    Time('1@')
    t=Time('19700101')
    assert t.week == 4
    t=Time('19691231')
    assert t.week == 3
    t=Time('19691102')
    assert t.week == 0
    t=Time('1910 12:12:12.12345678901223')

    #代码可以开源 测试用例不能开源 这才是财富积累啊 但是这个是教科书的一个子集 就没必要了

    #Jan|January|Jan\.
    t = Time('Jan 01 1970')
    assert(str(t) == '1970-01-01 00:00:00.0')

    t = Time('Jan 01 1970 12')
    assert(str(t) == '1970-01-01 12:00:00.0')

    t = Time('Jan 01 1970 12:12')
    assert(str(t) == '1970-01-01 12:12:00.0')

    t = Time('Jan 01 1970 12:12:12')
    assert(str(t) == '1970-01-01 12:12:12.0')

    t = Time('Jan 01 1970 12:12:12.12312312412')
    assert(str(t) == '1970-01-01 12:12:12.12312312412')

    t = Time('01 Jan ,1970')
    assert(str(t) == '1970-01-01 00:00:00.0')

    t = Time('01 JAN 1970')
    assert(str(t) == '1970-01-01 00:00:00.0')

    t = Time('01 jan ,1970')
    #assert(str(t) == '1970-01-01 00:00:00.0')

    t = Time('January 01 1970') 
    assert(str(t) == '1970-01-01 00:00:00.0')

    t = Time('01 January 1970') 
    assert(str(t) == '1970-01-01 00:00:00.0')

    t = Time('1970 January 01') 
    assert(str(t) == '1970-01-01 00:00:00.0')


    t = Time('1970 01 January')
    assert(str(t) == '1970-01-01 00:00:00.0')

    #|Feb|Feb\.|February
    t = Time('1970 01 February')
    assert(str(t) == '1970-02-01 00:00:00.0')
    t = Time('1970 01February')
    assert(str(t) == '1970-02-01 00:00:00.0')
    t = Time('1970February01')
    assert(str(t) == '1970-02-01 00:00:00.0')
    t = Time('February01 1970')
    assert(str(t) == '1970-02-01 00:00:00.0')
    t = Time('1970 01 Feb.')
    assert(str(t) == '1970-02-01 00:00:00.0')
    t = Time('1970 01 Feb')
    assert(str(t) == '1970-02-01 00:00:00.0')

    #|Mar|Mar\.|March
    t = Time('1970 01 March')
    assert(str(t) == '1970-03-01 00:00:00.0')
    t = Time('1970 01 Mar.')
    assert(str(t) == '1970-03-01 00:00:00.0')
    t = Time('1970 01 Mar')
    assert(str(t) == '1970-03-01 00:00:00.0')

    #|Apr|Apr\.|April
    t = Time('1970 01 April')
    assert(str(t) == '1970-04-01 00:00:00.0')
    t = Time('1970 01 Apr.')
    assert(str(t) == '1970-04-01 00:00:00.0')
    t = Time('1970 01 Apr')
    assert(str(t) == '1970-04-01 00:00:00.0')

    #|May
    t = Time('1970 01 May')
    assert(str(t) == '1970-05-01 00:00:00.0')

    #|Jun\.|June|Jun
    t = Time('1970 01 June')
    assert(str(t) == '1970-06-01 00:00:00.0')
    t = Time('1970 01 Jun.')
    assert(str(t) == '1970-06-01 00:00:00.0')
    t = Time('1970 01 Jun')
    assert(str(t) == '1970-06-01 00:00:00.0')

    #|Jul|July|Jul\.
    t = Time('1970 01 Jul')
    assert(str(t) == '1970-07-01 00:00:00.0')
    t = Time('1970 01 July')
    assert(str(t) == '1970-07-01 00:00:00.0')
    t = Time('1970 01 Jul.')
    assert(str(t) == '1970-07-01 00:00:00.0')

    #|Aug|Aug\.|August
    t = Time('1970 01 August')
    assert(str(t) == '1970-08-01 00:00:00.0')
    t = Time('1970 01 Aug.')
    assert(str(t) == '1970-08-01 00:00:00.0')
    t = Time('1970 01 Aug')
    assert(str(t) == '1970-08-01 00:00:00.0')

    #|Sep\.|September|Sep
    t = Time('1970 01 September')
    assert(str(t) == '1970-09-01 00:00:00.0')
    t = Time('1970 01 Sep.')
    assert(str(t) == '1970-09-01 00:00:00.0')
    t = Time('1970 01 Sep')
    assert(str(t) == '1970-09-01 00:00:00.0')

    #|Oct\.|Oct|October
    t = Time('1970 01 October')
    assert(str(t) == '1970-10-01 00:00:00.0')
    t = Time('1970 01 Oct.')
    assert(str(t) == '1970-10-01 00:00:00.0')
    t = Time('1970 01 Oct')
    assert(str(t) == '1970-10-01 00:00:00.0')

    #|Nov\.|November|Nov
    t = Time('1970 01 November')
    assert(str(t) == '1970-11-01 00:00:00.0')
    t = Time('1970 01 Nov.')
    assert(str(t) == '1970-11-01 00:00:00.0')
    t = Time('1970 01 Nov')
    assert(str(t) == '1970-11-01 00:00:00.0')

    #|Dec|Dec\.|December
    t = Time('1970 01 December')
    assert(str(t) == '1970-12-01 00:00:00.0')
    t = Time('1970 01 Dec.')
    assert(str(t) == '1970-12-01 00:00:00.0')
    t = Time('1970 01 Dec')
    assert(str(t) == '1970-12-01 00:00:00.0')

    #t=Time('2012da01 12:12:12.12')
    #assert( str(t) == '2012-01-01 12:12:12.12')
def test_Time_property():

    t=Time('19010101')
    t=t+'3M'
    assert str(t) == '1901-04-01 00:00:00.0'

    t=Time('20000229')
    t=t+'12M'
    assert str(t) == '2001-02-28 00:00:00.0'

    t=Time('20000229')
    t=t+'12M'
    assert str(t) == '2001-02-28 00:00:00.0'
    
    t=Time('20001231')
    t=t+'12M'
    assert str(t) == '2001-12-31 00:00:00.0'

    t=Time('20001231')
    t=t+'2M'
    assert str(t) == '2001-02-28 00:00:00.0'
    
    t=Time('19991231')
    t=t+'2M'
    assert str(t) == '2000-02-29 00:00:00.0'

    t=Time('20000229')
    t=t-'12M'
    assert str(t) == '1999-02-28 00:00:00.0'

    t=Time('20000101')
    t=t-'1M'
    assert str(t) == '1999-12-01 00:00:00.0'

    t=Time('20001231')
    t=t-'1M'
    assert str(t) == '2000-11-30 00:00:00.0'

    t=Time('20000531')
    t=t+'1M'
    assert str(t) == '2000-06-30 00:00:00.0'

def test_Time_sleep():

    start = time.time()
    time.sleep(1)
    end = time.time()
    e1 = end - start 

    start=Time()
    Time.sleep(1)
    end = Time()
    e2 = (end - start).timestamp

    assert abs(e2-e1) <= 0.01
