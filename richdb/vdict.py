#-*-encoding=utf8-*-
import os, logging, re, copy, time
from rich.console import Console
from rich.table import Table
from datetime import datetime
from functools import wraps
from .runlog import log
from pathlib import Path
from threading import Thread, Lock
lock = Lock()
v_columns_names = {}

class LineException(Exception):
    pass


class vdict:

    def __init__(self, *args, **kwargs):
        self._vdict__list = []
        self._vdict__iter = 0
        self._vdict__len = 0
        name = kwargs['name'] if 'name' in kwargs else ''
        _list = kwargs['_list'] if '_list' in kwargs else []
        self._vdict__name = str(id(self)) if name == '' or name is None else name
        llen = len(_list)
        if self._vdict__name in v_columns_names:
            for i in range(len(v_columns_names[self._vdict__name])):
                if i < llen:
                    self._vdict__list.insert(i, _list[i])
                else:
                    self._vdict__list.insert(i, None)

        if self._vdict__name not in v_columns_names:
            v_columns_names[self._vdict__name] = []
            for i in range(len(_list)):
                v_columns_names[self._vdict__name].insert(i, str(i))
                if i < llen:
                    self._vdict__list.insert(i, _list[i])
                else:
                    self._vdict__list.insert(i, None)

        self._vdict__len = len(v_columns_names[self._vdict__name])
        columns = v_columns_names[self._vdict__name]
        self._vdict__columns = columns

    @property
    def columns(self):
        return self._vdict__columns

    @property
    def name(self):
        return self._vdict__name

    @property
    def list(self):
        return self._vdict__list

    def add_column(self, name):
        with lock:
            v_columns_names[self._vdict__name].insert(self._vdict__len, name)
            self._vdict__list.insert(self._vdict__len, None)
            self._vdict__len = self._vdict__len + 1

    def insert_column(self, idx, name):
        with lock:
            v_columns_names[self._vdict__name].insert(idx, name)
            self._vdict__list.insert(idx, None)

    def set_column_name(self, i, name):
        with lock:
            nameset = set(v_columns_names[self._vdict__name])
            if name in nameset:
                raise ValueError('the column name conflict!')
            v_columns_names[self._vdict__name][i] = name

    def __next__(self):
        if self._vdict__iter >= self._vdict__len:
            raise StopIteration
        iteritem = self._vdict__list[self._vdict__iter]
        self._vdict__iter += 1
        return iteritem

    def __iter__(self):
        self._vdict__iter = 0
        return self

    def __len__(self):
        print(self._vdict__list)
        return max(len(self._vdict__list), len(v_columns_names[self._vdict__name]))

    def __getattr__(self, name):
        pass

    def __repr__(self):
        return str(self.to_dict())

    def __getitem__(self, key):
        if isinstance(key, str):
            for i in range(len(v_columns_names[self._vdict__name])):
                if v_columns_names[self._vdict__name][i] == key:
                    if i < len(self._vdict__list):
                        if i >= 0:
                            return self._vdict__list[i]

        if isinstance(key, int):
            if key < len(self._vdict__list):
                if key >= 0:
                    return self._vdict__list[key]
            if key < 0:
                return self._vdict__list[(len(self._vdict__list) + key - 1)]

    def __setitem__(self, key, value):
        vlen = len(v_columns_names[self._vdict__name])
        inflag = False
        if isinstance(key, str):
            for i in range(vlen):
                if v_columns_names[self._vdict__name][i] == key:
                    self._vdict__list[i] = value
                    inflag = True

            if inflag == False:
                v_columns_names[self._vdict__name].insert(vlen, key)
                self._vdict__list.insert(vlen, value)
                inflag = True
        elif isinstance(key, int):
            if key >= vlen:
                for i in range(key - vlen + 1):
                    self._vdict__list.insert(vlen + i, None)
                    v_columns_names[self._vdict__name].insert(vlen + i, str(vlen + i))

                self._vdict__list[key] = value
            else:
                self._vdict__list[key] = value

    def __getslice__(self, i, j):
        return self._vdict__list[i:j]

    def __setslice__(self, i, j, value):
        self._vdict__list[i:j] = value

    def __contains__(self, obj):
        if obj in self.list:
            return True
        else:
            return False

    def to_dict(self):
        d = {}
        print(v_columns_names)
        for i in v_columns_names[self._vdict__name]:
            d[i] = self.__getitem__(i)

        return d

    def to_list(self):
        l = []
        for i in v_columns_names[self._vdict__name]:
            l.append({i: self[i]})

        return l

    def print(self):
        table = Table(title=(self._vdict__name))
        for i in v_columns_names[self._vdict__name]:
            table.add_column(('None' if i is None else i), style='cyan', no_wrap=True)

        (table.add_row)(*[str(i) for i in self._vdict__list])
        console = Console()
        console.print(table, justify='center')

    def save(self, file):
        with open(file, 'a', encoding='utf-8') as (f):
            curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            f.write('\n#databeginblock#\n' + self._vdict__name + '\n' + curtime + '\n' + ','.join(['' if i is None else str(i) for i in self._vdict__columns]) + '\n' + ','.join(['' if i is None else str(i) for i in self._vdict__list]) + '\n' + '#dataendblock#')

    def load(self, file):
        i = 0
        enternum = 0
        datastrb = b''
        with open(file, 'rb+') as (f):
            i = 0
            while 1:
                i = i + 1
                f.seek(-i, 2)
                if f.read(1) == b'\n':
                    enternum += 1
                if enternum >= 6:
                    datastrb = f.read()
                    break

        datastr = str(datastrb, encoding='utf-8')
        if '#databeginblock#' not in datastr:
            raise LineException("{'errcode':'000001','errmsg':'datablock is destroyed'}")
        if '#dataendblock#' not in datastr:
            raise LineException("{'errcode':'000001','errmsg':'datablock is destroyed'}")
        datalist = datastr.replace('\r', '').split('\n')
        name = datalist[1] if datalist[1] is not None else str(id(self))
        updatetime = datalist[2]
        title = [None if i == '' else i for i in datalist[3].split(',')]
        data = [None if i == '' else i for i in datalist[4].split(',')]
        self._vdict__list = data
        self._vdict__name = name
        v_columns_names[self._vdict__name] = title
        columns = v_columns_names[self._vdict__name]
        self._vdict__columns = columns


if __name__ == '__main__':
    c = vdict(1, 2, 3, name='c')
    d = vdict(name='d')
    e = vdict(name='e', _list=[])
    f = vdict(name='f', _list=[])
    l = vdict()
    l.add_column('l0')
    l.add_column('l1')
    l.add_column('l2')
    l.add_column('l3')
    l[0] = 'l0'
    l[1] = None
    l[2] = 'l2'
    l[3] = 'None'
    l.add_column('l5')
    l.insert_column(2, 'l_isnert')
    l[2] = 'insert'
    l.print()
    print(l.to_dict())
    print(l.to_list())
    l.save('t.txt')
    d.add_column('d1')
    d.add_column('d2')
    print('d is :')
    d.print()
    print('global v_columns_names is :', v_columns_names)
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
    print('ee is ok ?')
    ee.save('ee.txt')
    ee.print()
    print('ee.columns is :', ee.columns)
    eee = vdict(name='e')
    eee[0] = 100
    eee[1] = 200
    eee.print()

    class A:

        def __repr__(self):
            return 'A.a00001'


    a = A()
    dd[0] = a
    dd[1] = 2
    print('dd is :')
    dd.print()
    print('d is :')
    d.print()
    d.columns.insert(2, 'd3')
    print('d_list :', d.list)
    print('d_name :', d.name)
    print('d_columns :', d.columns)
    print(d['d1'])
    d['d1'] = a
    d['d2'] = 1232423
    print("the final d['d1']", d['d1'])
    d.save('d.txt')
    e.print()
    f.print()
    e[0] = 1
    e[1] = 2
    f[0] = 3
    f[1] = 4
    e.print()
    f.print()
    loadtest = vdict()
    print('load is ok ?')
    loadtest.load('l.txt')
    print(loadtest.to_list())
    print(loadtest.to_dict())
    print('columns is :', loadtest.columns)
    print('__name is :', loadtest.name)
    print('shuai' if loadtest[0] is None else 'more shuai')
    print('shuai' if loadtest[1] is None else 'more shuai')
    print('shuai' if loadtest[2] is None else 'more shuai')
    print('shuai' if loadtest[3] is None else 'more shuai')
    loadtest.save('l.txt')