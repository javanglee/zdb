#-*- encoding=utf8 -*-

import threading, time

class wull:
    '''
    a + @ = a
    @ + a = a
    @ - a =-a
    a - @ = a
    -@    = @

    a * @ = @
    @ * a = @
    a / @ = @
    @ / a = @

    a ^ @ = @
    @ ^ a = @

    ln(@) = @ #not easy to realize with python so you can import ln from richdb
    |@|   = @ 
    -1 > @
    0  > @
    1  > @

    空元的乘除法不变性

    '''
    _wull__instance = None
    _wull__lock = threading.Lock()

    def __getattr__(self, key):

        def not_found(*args, **kwargs):
            return self

        if key in dir(self):
            return getattr(self, key)
        else:
            return not_found

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        with cls._wull__lock:
            if wull._wull__instance is None:
                wull._wull__instance = (object.__new__)(cls, *args, **kwargs)
        return wull._wull__instance

    def javang(self):
        print("You'd better call me Handsome Father.\n你甚至都不愿意叫我一声帅父。")

    def __repr__(self):
        return '@'

    def __str__(self):
        return '@'

    def __add__(self, other):
        return other 

    def __radd__(self, other):
        return other

    def __mul__(self, other):
        return self

    def __rmul__(self, other):
        return self

    def __sub__(self, other):
        return -other 

    def __rsub__(self, other):
        return other 

    def __truediv__(self, other):
        return self

    def __rtruediv__(self, other):
        return self

    def __floordiv__(self, other):
        return self

    def __rfloordiv__(self, other):
        return self

    def __mod__(self, other):
        return self

    def __rmod__(self, other):
        return self

    def __pow__(self, other):
        return self

    def __rpow__(self, other):
        return self

    def __neg__(self):
        return self

    def __pos__(self):
        return self

    def __abs__(self):
        return self

    def __iadd__(self):
        return self

    def __isub__(self):
        return self

    def __imul__(self):
        return self

    def __itruediv__(self):
        return self

    def __ifloordiv__(self):
        return self

    def __imod__(self):
        return self

    def __ipow__(self):
        return self

    def __invert__(self):
        return self

    def __lshift__(self, other):
        return self

    def __rshift__(self, other):
        return self

    def __and__(self, other):
        return self

    def __or__(self, other):
        return self

    def __xor__(self, other):
        return self

    def __rlshift__(self, other):
        return self

    def __rrshift__(self, other):
        return self

    def __rand__(self, other):
        return self

    def __rxor__(self, other):
        return self

    def __ror__(self, other):
        return self

    def __ilshift__(self, other):
        return self

    def __irshift__(self, other):
        return self

    def __iand__(self, other):
        return self

    def __ixor__(self, other):
        return self

    def __ior__(self, other):
        return self

    def __eq__(self, other):
        if id(self) == id(other):
            return True
        if id(self) != id(other):
            return False

    def __lt__(self, other):
        if id(self) == id(other):
            return False
        else:
            return True

    def __lt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __ne__(self, other):
        if id(self) == id(other):
            return False
        else:
            return True

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        if id(self) == id(other):
            return True
        else:
            return False

    def __del__(self):
        pass

def iswull(element):
    if isinstance(element, wull):
        return True
    return False
WULL = wull()

if __name__ == '__main__':

    def task(num):
        obj = wull()
        print(id(obj))


    for i in range(3):
        t = threading.Thread(target=task, args=(i,))
        t.start()

    a = wull()
    b = wull()
    a.javang()
    print('id a is ', id(a))
    print('id b is ', id(b))
    a.walk()
    a.play()
    a.javang()
    print(a + 2)
    print(a * 2)
    print(a)
    print(a ** 2)
    print(a * a)
    print(a == 3)
    print(a == a)
    print(3 == a)

    a = wull()
    print( iswull(a) )
    print( iswull(1) )
