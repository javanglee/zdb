#-*- encoding=utf8 -*-

import threading
import time
class null():
    __instance = None
    __lock = threading.Lock()

    def __getattr__(self, key):
        def not_found(*args, **kwargs):
            return self
        if key in dir(self):
            return getattr(self, key)
        return not_found 

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if null.__instance is None:
                time.sleep(1)
                null.__instance= object.__new__(cls, *args, **kwargs) 
        return null.__instance
    
    def javang(self):
        print("you'd better call me Handsome Father")

    def __repr__(self):
        return '@' 

    def __str__(self):
        return '@' 

    def __add__(self, other):
        return other 
    def __radd__(self, other):
        return other

    def __mul__(self, other):
        return other
    def __rmul__(self, other):
        return other

    def __sub__(self, other):
        return other
    def __rsub__(self, other):
        return other

    def __truediv__(self, other):
        return other
    def __rtruediv__(self, other):
        return other

    def __floordiv__(self, other):
        return other
    def __rfloordiv__(self, other):
        return other

    def __mod__(self, other):
        return other
    def __rmod__(self, other):
        return other

    def __pow__(self, other):
        return other
    def __rpow__(self, other):
        return other
    def __eq__(self, other):
        if id(self)==id(other):
            return True
        if id(self) != id(other):
            return False

    def __del__(self):
        pass

def task(num):
    obj = null()
    print( id(obj) )

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=task, args=(i,))
        t.start()

    a = null()
    b = null()

    print( 'id a is ', id(a) )
    print( 'id b is ', id(b) )

    a.walk()
    a.play()
    a.javang()

    print( a+2 )
    print( a*2 )
    print( a )
    print( a ** 2 )
    print( a*a )
    print( a==3 )
    print( a==a )
    print( 3==a )

