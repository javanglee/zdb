#-*- encoding=utf8 -*-
import sys

#from .richdb import rich, pray, Time, mdict, wull, WULL
from .ztime import Time, orange, fmt
from .richdb import rich, pray, q
from .mdict import mdict
from .wull import wull, WULL, iswull
from .vdict import vdict
from .version import __version__
__all__ = ('rich', 'Time', 'wull', 'WULL', 'mdict', 'pray', 'iswull', 'q', 'vdict', 'orange', 'fmt', '__version__')