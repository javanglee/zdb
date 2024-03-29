<!-- Add banner here -->

<img title="Dmitry Demidko" src="https://images.unsplash.com/photo-1550565118-3a14e8d0386f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=Mnw5MDg0MHwwfDF8c2VhcmNofDIzfHxtb25leXxlbnwwfHx8fDE2NDMyNzg0NTA&ixlib=rb-1.2.1&q=80&w=1080" alt="three round gold-colored coins on 100 US dollar banknotes" width="659">

# Richdb (Born For Rich为发财而生)

<!-- Add buttons here -->

<img title="Jan Antonin Kolar" src="https://images.unsplash.com/photo-1544383835-bda2bc66a55d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=Mnw5MDg0MHwwfDF8c2VhcmNofDI3fHxEQnxlbnwwfHx8fDE2NDMyNzg3MzQ&ixlib=rb-1.2.1&q=80&w=1080" alt="brown wooden drawer" width="475">



我们可以这样开始使用这个包

We can start it like this.

```
pip install richdb
>>> from richdb import rich
>>> rich()

我们的口号是：为发财而生
Our Slogan: BORN FOR RICH

      [   ]
(@)==[_____]==(@)
      |* *|
      (_-_)
     /     \
    /    / 恭 /
__@__   / 喜 /
\___/  / 发 / \
  \   / 财 /  /
   |_________|

   "MONEY GOD"
   Buddha Ruly, Camel God, Jesus God, ... and so on.
   There are seven Gods in this world.
   One God rule them all.
   Knee before the Money God and pray.
   And then you will be rich.

these numbers may make you rich:
['08', '10', '12', '15', '24', '30'] ['14']
>>>
```



当你使用python官方标准时间库时，可能会经常绕晕自己。datetime,calendar,time这些包能很好帮助我们处理时间的问题，但是缺少一点便捷。pathlib的出现给了我们一些启发，时间处理是否可以像pathlib一样方便。此类设计可能会带来性能的影响，但是又不一定，因为好的设计往往带来不只是局部性能的提升而是全局性能的提升，这在DirectX的C#项目与C++项目中得到了印证。

When we use the official standard time package, it always make us confused.datetime,calendar,time these packages can help us to solve the timeseries problem,but it is not so convenient.The pathlib enlightened us , can we make the time package to be like the pathlib.These kind of design may bring some performance problem,or may not.Good design always bring the whole system's better performance rather than local optimization.DirectX c# projects are always playing better than the C++.

软件工程时常要平衡性能和代码可维护性的关系，这个平衡是一个优秀的架构师和程序员管理者的基本功。但是评价这个能力和基本功的量化指标是缺乏的，全世界的程序员们也只能凭主观感受来评价代码，这带来了巨大的管理麻烦，使得世界各地的IT项目良莠不齐，甲乙双方难以达成合适的协议，甲方不知道为哪类代码增加更多的经费（得加钱）。

 Software engineering always need to balance the performance and the maintainability.A good Software Architect can make this balance awesome.But we lack the index or kpi like to estimate  the design work. All of these is based on subjective evaluation on appearance of the code.This make the IT project The corps and the weeds mix together.Party A and Party B can't reach a reasonable agreement.The Party A doesn't know how to make supplementary budget for expenditures for better codes.


在研究pathlib的特征时，我们发现，pathlib的设计理念很类似数学群论。它首先定义了一个文件路径的集合A和字符串的集合B，然后定义了文件路径集合的加法运算/，A中的元素与B中的元素通过运算符/以及其他运算符，在A B两个集合形成了一个很好的闭合。

pathlib's design method seems like it's based on the group theory of math.It define two collections, one is file path collection A, the other is collection B,and define the group addition /.

例如：

eg:

```
>>> from pathlib import Path
>>> Path('/home/data/')/'hello'
WindowsPath('/home/data/hello
>>> Path('/home/data/')/'hello'/'data'/'data'
WindowsPath('/home/data/hello/data/data')
```

正因为集合A中的元素a=Path('/home/data/')，带有根路径的绝对路径构成的结合A与字符串构成的结合B中的元素b1='hello' , b2='data' 等做/运算时，a/b1/b2,a/b2/b1 得到结果元素均属于集合A，这种具有一定闭合性质的运算。

Element a= Path('/home/data/') in collection A ,the root path / the string element in collection B, the result is still in the collection A. This make code elegant.

这使得目录的处理更加方便灵活，避免了大量嵌套判断等等。这很优雅，也很方便，这样的代码除了对它说得加钱，你想不到更好的语言来形容它。据此对时间的类进行了类似的封装与设计，这是一个借鉴，程序员的事怎么能叫抄呢，这叫借鉴。当然也涉及了另一个重要因素就是**一手数据源原则(First Hand Data Principle FH)**。

this package contains another design method.Except the group theory , Fisrt Hand Data Principle is also brought in.

```
>>> from richdb import Time
>>> t=Time()
>>> t
<Time:2022-10-19 07:22:28.2295296>
>>> t.timestamp
1643296466.0483491
>>> t.fmt('%Y-%m-%d %H:%M:%S')
<Time:2022-10-19 07:22:28.2295296>
```

```
>>> t2 = Time('2021-01-02')
>>> t2
<Time:2021-01-02 00:00:00.0>
#相差的时间是以秒为单位
>>> t2-t
>>> t2-t
<Time:-655@16:37:31.770470381>
>>> t2-t
<Time:-655@16:37:31.770470381>
#两个时间相差天数
>>> (t2-t).day
-655
>>> (t2-t)+'655D'
<Time:-0@16:37:31.770470381>
>>>
>>> ((t2-t)+'655D').timestamp
-26548.229529619217
#这个时间戳在手表上显示的时间刚好是 16:37:31.770470381

Here is the formula:
#this design is very beatiful
Time('@timestamp') = 'D@H:M:S'
H:M:S show the time from pointer of the watch.
Change watch time to seconds.

timestamp = D*86400+(H*60*60+M*60+S)

Time('@-timestamp') = '-D@H:M:S'
timestamp = -D*86400-86400+(H*60*60+M*60+S)

if you use it like this , it is more clear.
Time('@12:23:24.23232')
Time('@-12:23:24.23232')

Time('-1@12:23:24.23232')
Time('2@12:23:24.23232')

#我们经常需要处理一个时间列表,当然对于任何一个object只要实现了 __add__ 和 defaultstep 两个函数,均可以使用orange
#时间类Time的defaultstep 是 '1D', 也可以使用'3M'，如果一个类实现了加法，但是没有实现defaultstep函数，那么默认增量是1

>>> from richdb import orange
>>> start = Time('20000101')
>>> end = Time('20000107')
>>> for i in orange(start, end):
...     print( i )
...
2000-01-01 00:00:00.0
2000-01-02 00:00:00.0
2000-01-03 00:00:00.0
2000-01-04 00:00:00.0
2000-01-05 00:00:00.0
2000-01-06 00:00:00.0

#orange 在整型变量里是同range效果一样的。
>>> for i in orange(1,10):
...     print( i )
...
1
2
3
4
5
6
7
8
9
>>> list( range(1,10) )
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#求当月的日期列表
>>> t=Time()
>>> start = t.monthfirstday()
>>> end = t.monthlastday()

#tl is short for time list
>>> tl = list( orange( start, end) )
>>> tl
[<Time:2022-10-01 10:34:45.3590262>, <Time:2022-10-02 10:34:45.3590262>, <Time:2022-10-03 10:34:45.3590262>, <Time:2022-10-04 10:34:45.3590262>, <Time:2022-10-05 10:34:45.3590262>, <Time:2022-10-06 10:34:45.3590262>, <Time:2022-10-07 10:34:45.3590262>, <Time:2022-10-08 10:34:45.3590262>, <Time:2022-10-09 10:34:45.3590262>, <Time:2022-10-10 10:34:45.3590262>, <Time:2022-10-11 10:34:45.3590262>, <Time:2022-10-12 10:34:45.3590262>, <Time:2022-10-13 10:34:45.3590262>, <Time:2022-10-14 10:34:45.3590262>, <Time:2022-10-15 10:34:45.3590262>, <Time:2022-10-16 10:34:45.3590262>, <Time:2022-10-17 10:34:45.3590262>, <Time:2022-10-18 10:34:45.3590262>, <Time:2022-10-19 10:34:45.3590262>, <Time:2022-10-20 10:34:45.3590262>, <Time:2022-10-21 10:34:45.3590262>, <Time:2022-10-22 10:34:45.3590262>, <Time:2022-10-23 10:34:45.3590262>, <Time:2022-10-24 10:34:45.3590262>, <Time:2022-10-25 10:34:45.3590262>, <Time:2022-10-26 10:34:45.3590262>, <Time:2022-10-27 10:34:45.3590262>, <Time:2022-10-28 10:34:45.3590262>, <Time:2022-10-29 10:34:45.3590262>, <Time:2022-10-30 10:34:45.3590262>]

>>> from richdb import fmt
>>> fmt( tl, '%Y-%m-%d')
<generator object fmt at 0x000001F1CA89D310>
>>> strtl = list( fmt( tl, '%Y-%m-%d') )
>>> strtl
['2022-10-01', '2022-10-02', '2022-10-03', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09', '2022-10-10', '2022-10-11', '2022-10-12', '2022-10-13', '2022-10-14', '2022-10-15', '2022-10-16', '2022-10-17', '2022-10-18', '2022-10-19', '2022-10-20', '2022-10-21', '2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25', '2022-10-26', '2022-10-27', '2022-10-28', '2022-10-29', '2022-10-30']
>>>

```

时间序列是数据处理中非常重要的领域，数据管理工程中很重要的原则就是一手数据源原则。

Timeseries is very important part of the Data Manage Engineering(this area is something different from software engineering).

**一手数据源原则**，避免计算列，所有的日期都是由时间戳获得，这是数据处理中最重要的原则之一。


First Hand Data Principle ：Avoid computing the field base on the computed fields.
In Time class instance only store the timestamp.

一手数据源原则，就是B数据集由A数据集计算得来，但是为了避免A数据集计算错误和时间差造成的不一致，通常C计算集都是由A计算得来。
这有个概率公式A->B->C  A->B出错的概率为a，B->C出错的概率为b, 
C数据集会因为数据错误的概率会因为传递而导致增加$( sum(A)*a*(1-b) + sum(B)*b*(1-a))/sum(B)$。相比于直接通过A计算出C，A->C 发生数据错误的概率更低。 


B is computed from A. C can be computed from A and also can be computed from B.

If you follow the First Hand Data Principle ,you should compute C directly from A rather than compute C from B. 

A->B error probability is a, B->C error probability is b.

C error probability is :$( sum(A)*a*(1-b) + sum(B)*b*(1-a))/sum(B)$

当我们选择接口或者数据嵌套时，就需要深度评估，尤其加强测试，对于有嵌套行为的接口测试的工作量通常要远多于没有数据嵌套的。

So when we choose api ,we'd better not nest api for data transformation. If you have to do this, you must add more test than before and add more maintenance cost.

```
>>> a=[1,2,3]
>>> a[4]=10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>>
```

python原有的list不是很方便，因为经常会因为越界而爆出异常，另外dict类型往往消耗内存较多。所以在这个包中混合了vector list和dict的特点，做了一个vdict类，用起来很方便。

Standard lib list is not enough for some circumstance. And dict type data waste more memory. So this vdict combines the benefits of  vector and list.

```
>>> from richdb import vdict
>>> v=vdict()
>>> v[3]=100
>>> v
{'0': None, '1': None, '2': None, '3': 100}
>>> v.set_column_name(0,'v0')
>>> v['v0']
>>> v
{'v0': None, '1': None, '2': None, '3': 100}
>>> v['v0']=100
>>> v
{'v0': 100, '1': None, '2': None, '3': 100}
>>> v[0]
100
>>> v['v0']
100
>>>dir(vdict) #try and explore more it is easy to use. 
```

Sometime we need mirror dict to record some data contains code and name, 
we need a[code] to get name and we want to use a[name] to get code.
```

>>> from richdb import mdict
>>> a=mdict()
>>> a[10000]='bob'
>>> a[10001]='scott'
>>> a
{10000: 'bob', 10001: 'scott'}{'bob': 10000, 'scott': 10001}
>>> a['bob']
10000
>>> a['scott']
10001
>>> a[10000]
'bob'
>>> a[10001]
'scott'
>>>
```
When we use None ,we can't use None.f(),but sometimes we need this function.
So create another class WULL
```
>>> from richdb import WULL
>>> a=[]
>>> a.append(WULL)
>>> a
[@]
>>> a.append(WULL)
>>> a
[@, @]
>>> a.append(WULL)
>>> a
[@, @, @]
>>> a[0].f()
@
>>> a[0]+100
100
>>>
```
# More for Richdb

It is easy to use and easy to learn and easy to modify. You can add more features or fix the bugs.

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [contribute](#contribute)
- [License](#license)
- [Footer](#footer)

# Installation

[(Back to top)](#table-of-contents)

```
pip install richdb
```

# Usage

[(Back to top)](#table-of-contents)

```
from richdb import Time,Timeseries,vdict
```

# Development

[(Back to top)](#table-of-contents)

<div>
https://github.com/javanglee/zdb.git
</div>

# Contribute

[(Back to top)](#table-of-contents)

Do anything in the src you like!

# License

[(Back to top)](#table-of-contents)

MIT

# Footer

[(Back to top)](#table-of-contents)

Thank Python!

**Life is short,life must be very happy for it is not a man!**
***[python]***
