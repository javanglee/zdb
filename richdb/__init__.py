"""

richdb is a tiny, timeseries and Javang Matrix type database optimized for your rich :)
Focus on make you rich!!!!!!!

.. codeauthor:: javang.lee <walkbob@sina.com>


Usage example:


>>> from tinydb import TinyDB, where

>>> from tinydb.storages import MemoryStorage

>>> db = TinyDB(storage=MemoryStorage)

>>> db.insert({'data': 5})  # Insert into '_default' table

>>> db.search(where('data') == 5)

[{'data': 5, '_id': 1}]

>>> # Now let's create a new table

>>> tbl = db.table('our_table')

>>> for i in range(10):

...     tbl.insert({'data': i})

...

>>> len(tbl.search(where('data') < 5))

5

"""

from .richdb import rich 
from .vdict import vdict
from .ztime import Time,Timeseries
from .null import null
from .mdict import mdict
from .version import __version__

__all__ = ('rich', 'vdict', 'Time', 'Timeseries',  'null', 'mdict')