# uncompyle6 version 3.8.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\scienco\Desktop\paper\zdb\richdb\mdict.py
# Compiled at: 2022-04-30 23:00:11
# Size of source mod 2**32: 3100 bytes
import threading
lock = threading.Lock()

class mdict:

    def __init__(self, *args, **kwargs):
        self._mdict__dict = {}
        self._mdict__mirror_dict = {}
        if len(args) >= 0:
            return

    def __getitem__(self, key):
        if key in self._mdict__dict:
            return self._mdict__dict[key]
        if key in self._mdict__mirror_dict:
            return self._mdict__mirror_dict[key]

    def __setitem__(self, key, value):
        with lock:
            if key in self._mdict__dict:
                if value in self._mdict__mirror_dict:
                    if self._mdict__dict[key] == value:
                        return
                else:
                    if key not in self._mdict__dict:
                        if value not in self._mdict__mirror_dict:
                            self._mdict__dict[key] = value
                            self._mdict__mirror_dict[value] = key
                            return
                    if value in self._mdict__mirror_dict:
                        if key not in self._mdict__dict:
                            del self._mdict__dict[self._mdict__mirror_dict[value]]
                            del self._mdict__mirror_dict[value]
                            self._mdict__dict[key] = value
                            self._mdict__mirror_dict[value] = key
            else:
                if value not in self._mdict__mirror_dict:
                    if key in self._mdict__dict:
                        del self._mdict__mirror_dict[self._mdict__dict[key]]
                        del self._mdict__dict[key]
                        self._mdict__dict[key] = value
                        self._mdict__mirror_dict[value] = key
                if key in self._mdict__dict and value in self._mdict__mirror_dict and self._mdict__dict[key] != value:
                    raise ValueError(f"{key} is in main dict and {value} is in mirror dict but dict[{key}] != {value}")

    def __contains__(self, value):
        if value in self._mdict__dict or value in self._mdict__mirror_dict:
            return True
        else:
            return False

    def __repr__(self):
        return str(self._mdict__dict) + str(self._mdict__mirror_dict)

    def __str__(self):
        return str(self._mdict__dict) + str(self._mdict__mirror_dict)

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass


if __name__ == '__main__':
    m = mdict()
    m['1'] = 100
    m['100'] = 2
    m['110'] = 3
    if 3 in m:
        print('ok')
    if '100' in m:
        print('ok')
    print(m)