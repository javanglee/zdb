#-*- encoding=utf8 -*-
import threading
lock = threading.Lock()
 
class mdict():
    def __init__(self):
        self.__dict = {}
        self.__mirror_dict = {}

    def __getitem__(self, key):
        if key in self.__dict:
            return self.__dict[key]
        elif key in self.__mirror_dict:
            return self.__mirror_dict[key]
        return None

    def __setitem__(self, key, value):
        #{1: 2, None: 1}{2: 1, 1: None} a[2]=None

        with lock:
            #block 1 key in main dict and value in mirror dict and dict[key] == value
            if key in self.__dict and value in self.__mirror_dict and self.__dict[key] == value:
                return

            #block 2 key not in main dict and value not mirror dict 
            if key not in self.__dict and value not in self.__mirror_dict:
                self.__dict[key] = value
                self.__mirror_dict[value] = key
                return

            #block 3 value in mirror dict and key not in main dict
            if value in self.__mirror_dict and key not in self.__dict:
                #_dict ={ self.__mirror_dict[value] : self.__dict[ self.__mirror_dict[value] ] } 注释辅助 数据结构 
                #_mirror_dict = { value: self.__mirror_dict[value] }

                del self.__dict[ self.__mirror_dict[value] ]
                del self.__mirror_dict[value]
                self.__dict[key] = value
                self.__mirror_dict[value] = key

            #block 4 key in main dict and value not in mirror dict
            if value not in self.__mirror_dict and key in self.__dict:
                #_dict ={ self.__mirror_dict[value] : self.__dict[ self.__mirror_dict[value] ] } 注释辅助 数据结构 
                #_mirror_dict = { value: self.__mirror_dict[value] }

                del self.__mirror_dict[ self.__dict[key] ]
                del self.__dict[key]
                self.__dict[key] = value
                self.__mirror_dict[value] = key

            #block 5 key in main dict and value not in mirror dict and dict[key] ！= value
            #this feature will be add 
            if key in self.__dict and value in self.__mirror_dict and self.__dict[key] != value:
                raise ValueError('key is in main dict and value is in mirror dict but dict[key] != value')



    def __repr__(self):
        return str( self.__dict ) + str( self.__mirror_dict)

    def __str__(self):
        return str(self.__dict) + str( self.__mirror_dict )

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass
