# zdb
这个包的设计是模仿pathlib的，我们管这种设计方式叫基于群论的软件工程设计方法。
this package is designed follow the pathlib's design method
we call this kind design method : software design base on group theory

群的性质越完备越好，则类的设计越好。
将群论引入软件工程有助于量化评估代码质量，我们经常无法解决的问题是什么代码算好的问题，缺乏一个量化的指标。
这是python和C++语言的魅力，未来语言应该怎样设计呢？

时间序列是数据处理中非常重要的领域，数据管理工程中很重要的原则就是一手数据源原则。
this package contains another design method. 
一手数据源原则，避免计算列，所有的日期都是由时间戳获得，这是数据处理中最重要的原则之一。
一手数据源原则，就是A数据集由B数据集计算得来，但是为了避免A数据集计算错误和时间差造成的不一致，通常C计算集都是由A计算得来。
这有个概率公式A->B->C A->B出错的概率为a B->C出错的概率为b, 
C数据集会因为数据错误的概率会因为传递而导致增加( sum(A)*a*(1-b) + sum(B)*b ) /sum(B)。
当我们选择接口或者数据嵌套时，就需要深度评估，尤其加强测试。

install :
python setup.py install

This package is very easy to use:

You can input data parameter with float timestamp or string datetime format to init the Time class instance.

from zdb import Time, Timeseries

t1 = Time(30000)

t2 = Time(1000)

t979 = Time(1)

t989 = Time(0)

t999 = Time(-1)

t3 = Time('2022-01-05 12:12:12.1')

t909 = Time('2022-01-05 12:12:12.000001')

t4 = Time('2022.01.05 12:12:12.000001')

t5 = Time('2022/01/05 12:12:12.000001')

t6 = Time('20220105 12:12:12.000001')

t99 = Time('2022')

t99 = Time('202201')

t7  = Time('20220105')

t8  = Time('20220105 12')

t9  = Time('20220105 12:12')

t10 = Time('20220105 12:12:13')

t22 = Time('2022')

t23 = Time('2022-01')

t11 = Time('2022-01-05')

t12 = Time('2022-01-05 12')

t13 = Time('2022-01-05 12:12')

t14 = Time('2022-01-05 12:12:13')

t25 = Time('2022')

t26 = Time('2022.01')

t15 = Time('2022.01.05')

t16 = Time('2022.01.05 12')

t17 = Time('2022.01.05 12:12')

t17 = Time('2022.01.05 12:12:13')

print( 't17 time format %Y-%m-%d %H:%M:%S ', t17.fmt( '%Y-%m-%d %H:%M:%S' ))


print( t1 )
print( t2 )
print( t1 - t2 )

print( t1.timestamp )

print( t2.timestamp )

print( t1 + 100 )

print( t1 + 20000 )

print( 'day is :', t1.day)

print( 'month is :', t1.month)

print( 'year is :', t1.year)

print( 'week is :', t1.week)

获取截止当前时间所在月的全部日期：
ts1 = Timeseries()

获取截止日期20210101的所在月的全部日期：
ts2 = Timeseries('20210101')

获取截止日期20210131的所在月的全部日期：
ts3 = Timeseries('20210131')

按照%Y-%m-%d格式输出时间序列的list
print( ts1.fmt('%Y-%m-%d') )

按照%Y-%m-%d格式输出时间序列的list
print( ts2.fmt('%Y-%m-%d'))

按照%Y-%m-%d格式输出时间序列的list
print( ts3.fmt('%Y-%m-%d'))
