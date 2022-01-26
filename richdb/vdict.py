# -*- coding=utf-8 -*-
import os
import yaml
import logging
import re
import copy
import time

from rich.console import Console
from rich.table import Table

from datetime import datetime
from common import common as c 
from functools import wraps
from runlog import log
from pathlib import Path
from threading import Thread, Lock

lock = Lock()

v_columns_names ={}

class LineException(Exception):
    pass

class vdict:
    def __init__(self, *args, **kwargs):
        name = kwargs['name'] if 'name' in kwargs else ''
        _list = kwargs['_list'] if '_list' in kwargs else [] 
        print('id is :', str(id(self)) )
        self.__name = str(id(self)) if name=='' else name
        print('__name is :', self.__name)
        self.__list = _list
        if self.__name in v_columns_names:
            for i in range( len( v_columns_names[self.__name])):
                self.__list.append(None)

        self.__iter = 0

        if self.__name not in v_columns_names:
            v_columns_names[self.__name] =[]
            for i in range( len(_list)):
                v_columns_names[self.__name].insert(i, None) 
        print( v_columns_names )

        self.__len = len(v_columns_names[self.__name])
        columns = v_columns_names[self.__name]
        self.__columns = columns


    @property
    def columns(self):
        return self.__columns

    @property
    def name(self):
        return self.__name

    @property
    def list(self):
        return self.__list
     
    def add_column(self, name):
        with lock:
            v_columns_names[self.__name].insert(self.__len, name)
            self.__list.insert(self.__len, None)
            self.__len = self.__len+1

    def insert_column(self, idx, name):
        with lock:
            v_columns_names[self.__name].insert(idx, name)
            self.__list.insert(idx, None)

    def set_column_name(self,i, name):
        with lock:
            nameset = set( v_columns_names[self.__name] )
            if name in nameset:
                raise ValueError('the column name conflict!')
            v_columns_names[self.__name][i] = name

    def __next__(self):
        if self.__iter >=self.__len:
            raise StopIteration
        iteritem = self.__list[self.__iter]
        self.__iter += 1
        return iteritem

    def __iter__(self):
        self.__iter = 0
        return self

    def __len__(self):
        return self.__len

    def __getattr__(self, name):
        pass

    def __repr__(self):
        return str(self.to_dict() )

    def __getitem__(self, key):
        if isinstance(key, str):
            for i in range(len(v_columns_names[self.__name])):
                if v_columns_names[self.__name][i] == key:
                    return self.__list[i]
        return self.__list[key]
        
    def __setitem__(self, key, value):
        vlen = len(v_columns_names[self.__name])
        inflag = False
        if isinstance(key, str):
            for i in range(vlen):
                if v_columns_names[self.__name][i] == key:
                    self.__list[i] = value
                    inflag = True
            if inflag == False:
                v_columns_names[self.__name].insert(vlen, key)
                self.__list.insert(vlen,value)
                inflag = True
        elif isinstance(key, int):            
            if key >= vlen:
                for i in range(key-vlen+1):
                    self.__list.insert(vlen+i, None)
                    v_columns_names[self.__name].insert(vlen+i, str(vlen+i))
                self.__list[key] = value
            else:
                self.__list[key] = value

    def __getslice__(self, i, j):
        return self.__list[i:j]

    def __setslice__(self, i,j,value):
        self.__list[i:j] = value

    def __contains__(self, obj):
        return True if obj in self.list else False

    def to_dict(self):
        d = {}
        for i in v_columns_names[self.__name]:
            d[i] = self[i]       
        return d

    def to_list(self):
        l = []
        for i in v_columns_names[self.__name]:
            l.append( { i : self[i] } )
        return l

    def print(self):
        table = Table(title = self.__name)
        for i in v_columns_names[self.__name]:
            table.add_column("None" if i is None else i , style="cyan", no_wrap=True)
        
        table.add_row(*[str(i) for i in self.__list])
        console = Console()
        console.print(table, justify="center")

    def save(self, file):
        with open(file, "a", encoding="utf-8") as f:
            curtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) #this is so ugly
            f.write('\n#databeginblock#\n'\
            +self.__name+'\n'\
            +curtime+'\n'\
            +','.join(['' if i is None else str(i) for i in self.__columns])+'\n'\
            +','.join(['' if i is None else str(i) for i in self.__list])+'\n'\
            +'#dataendblock#')

    def load(self, file):
        #self.save(file)
        i=0
        enternum = 0
        datastrb = b""
        with open(file,'rb+') as f:
            i=0
            while True:
                i = i+1
                f.seek(-i,2)
                if f.read(1) == b'\n' :
                    enternum+=1
                if enternum >= 6:
                    datastrb=f.read()
                    break
        datastr = str(datastrb, encoding='utf-8')
        if '#databeginblock#' not in datastr:
            raise LineException("{'errcode':'000001','errmsg':'datablock is destroyed'}")
        if '#dataendblock#' not in datastr:
            raise LineException("{'errcode':'000001','errmsg':'datablock is destroyed'}")

        datalist = datastr.replace('\r','').split('\n')


        name = datalist[1] if datalist[1] is not None else str(id(self))
        updatetime = datalist[2]
        title = [ None if i == '' else i for i in datalist[3].split(',') ]
        data = [ None if i == '' else i for i in datalist[4].split(',') ] 

        self.__list = data
        self.__name = name
        v_columns_names[self.__name] = title 
        columns = v_columns_names[self.__name]
        self.__columns = columns

if __name__=='__main__':
    c = vdict(1,2,3,name='c')
    d = vdict(name='d')
    e = vdict(name="e", _list=[])
    f = vdict(name="f", _list=[])
    l = vdict()

    l.add_column('l0')
    l.add_column('l1')
    l.add_column('l2')
    l.add_column('l3')
    #l.add_column(None)
    l[0] = 'l0'
    l[1] = None
    l[2] = 'l2'
    l[3] = 'None'

    l.add_column('l5')
    l.insert_column(2, 'l_isnert')
    l[2] = 'insert'
    #l.columns.insert(2,'l_insert')
    l.print()
    print( l.to_dict() )
    print( l.to_list() ) 
    l.save( 't.txt' ) 

    d.add_column('d1')
    d.add_column('d2')
    print( 'd is :')
    d.print()
    print('global v_columns_names is :', v_columns_names )
    dd = vdict(name='d')

    c.add_column('c1')
    c.add_column('c2')
    e.add_column('e1')
    e.add_column('e2')
    f.add_column('f1')
    f.add_column('f2')

    ee = vdict(name='e')
    ee[0] = None
    ee[1] = None
    print( 'ee is ok ?')
    ee.save('ee.txt')

    ee.print()
    print( 'ee.columns is :' , ee.columns )

    eee = vdict(name='e')
    eee[0] = 100
    eee[1] = 200

    eee.print()

    class A:
        def __repr__(self):
            return 'A.'+'a00001'
        pass

    a = A()
    dd[0] = a
    dd[1] = 2
    print( "dd is :" )
    dd.print()
    print( "d is :" )
    d.print()
    d.columns.insert(2,'d3')

    print( 'd_list :', d.list)
    print( 'd_name :', d.name)
    print( 'd_columns :', d.columns)
    print( d['d1'])

    d['d1'] = a
    d['d2'] = 1232423

    print("the final d['d1']",  d['d1'] )
    d.save('d.txt')
    e.print()
    f.print()

    e[0] = 1
    e[1] = 2

    f[0] = 3
    f[1] = 4

    e.print()
    f.print()
    #print( v_columns_names[] )

    loadtest = vdict()
    print( 'load is ok ?')

    loadtest.load('l.txt')
    print( loadtest.to_list() )
    print( loadtest.to_dict() )
    print('columns is :', loadtest.columns )
    print('__name is :', loadtest.name )
    print('shuai' if loadtest[0] is None else 'more shuai' )
    print('shuai' if loadtest[1] is None else 'more shuai' )
    print('shuai' if loadtest[2] is None else 'more shuai' )
    print('shuai' if loadtest[3] is None else 'more shuai' )
    loadtest.save('l.txt')