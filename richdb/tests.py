from .mdict import mdict
import pytest

def test_mdict():
    #block 1 key in main dict and value in mirror dict and dict[key] == value
    a = mdict()
    a[1]=2
    print( a )
    a[1]=2
    print( a )
    assert a[1] == 2
    assert a[2] == 1 

    #block 2 key not in main dict and value not in mirror dict
    a = mdict()
    a[1] = 2
    print( a )
    a[2] = 3
    assert a[1] == 2 
    assert a[2] == 3 
    assert a[3] == 2 

    #block 3 value in mirror dict and key not in main dict
    a=mdict()
    a[None] = 10
    a[1] = 2
    print( a )
    a[3] = 2 
    print( a )
    a[None] =  None
    print( a )
    assert a[1] == None 
    assert a[3] == 2
    assert a[2] == 3

    #block 4 key in main dict and value not in mirror dict
    b = mdict()
    b[1] = 2
    b[3] = 4
    b[4] = 5
    print( b)
    b[4] = 6 
    b[4] = None
    print( b )
    assert b[1] == None
    assert b[3] == 4 
    assert b[4] == 3 

    assert b[4] == 5 
    assert b[5] == 4 

    assert b[5] == 2 
    assert b[2] == 5 







