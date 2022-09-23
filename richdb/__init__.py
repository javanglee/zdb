#-*- encoding=utf8 -*-
import sys

#from .richdb import rich, pray, Time, mdict, wull, WULL
from .ztime import Time
from .richdb import rich, pray, q
from .mdict import mdict
from .wull import wull, WULL, iswull
__all__ = ('rich', 'Time', 'wull', 'WULL', 'mdict', 'pray', 'iswull', 'q')