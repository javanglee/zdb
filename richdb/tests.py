# -*- encoding=utf8 -*-
import sys
from os.path import dirname, abspath
sys.path.append( dirname( abspath( __file__ ) ) )

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

def test_Time():
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

    t1 = Time('@-1')
    assert t1=='-0@23:59:59.0000000'

    t1 = Time('@-1')
    assert t1=='0@00:00:00.0000000'
    
    t1=Time('1970-1-1 0:0:0')
    assert t1.timestamp == 0.0

    t1=Time('1970/1/1 0:0:0')
    assert t1.timestamp == 0.0

    t1=Time('1970/01/01 00:00:00')
    assert t1.timestamp == 0.0

    t1 = Time('1970')
    assert t1.timestamp == 0.0

