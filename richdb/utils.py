#-*- encoding=utf8 -*-
import datetime as dt, time, re, calendar
from .wull import wull, iswull, WULL

#Name xxxx-xx-xx xx:xx:xx.xxxxx as standard datetime format, This is very important.
#use for to make code simple won't be better than this,too many return in for is hard to maintain and debug.

MONTH_DICT={'JAN':'01','JANUARY':'01','JAN.':'01','FEB':'02','FEB.':'02','FEBRUARY':'02','MAR.':'03','MAR':'03','MARCH':'03','APR.':'04','APR':'04','APRIL':'04','MAY':'05','JUN.':'06','JUNE':'06','JUN':'06','JUL':'07','JULY':'07','JUL.':'07','AUG':'08','AUG.':'08','AUGUST':'08','SEP.':'09','SEPTEMBER':'09','SEP':'09','OCT.':'10','OCT':'10','OCTOBER':'10','NOV.':'11','NOVEMBER':'11','NOV':'11','DEC':'12','DEC.':'12','DECEMBER':'12'}

# 31-12-2012 12:12:12.1213
UTILS_ENREX0 = re.compile(r'en\D*([0123]?\d)\D+([01]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)',re.I)
# 31-12-2012 12:12:12
UTILS_ENREX1 = re.compile(r'en\D*([0123]?\d)\D+([01]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)',re.I)
# 31-12-2012 12:12
UTILS_ENREX2 = re.compile(r'en\D*([0123]?\d)\D+([01]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)',re.I)
# 31-12-2012 12
UTILS_ENREX3 = re.compile(r'en\D*([0123]?\d)\D+([01]?\d)\D+(\d{4})\D+([012]?\d)',re.I)
# 31-12-2012
UTILS_ENREX4 = re.compile(r'en\D*([0123]?\d)\D+([01]?\d)\D+(\d{4})',re.I)

# 12-31-2012 12:12:12.1213
UTILS_USREX0 = re.compile(r'us\D*([01]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)',re.I)
# 12-31-2012 12:12:12
UTILS_USREX1 = re.compile(r'us\D*([01]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)',re.I)
# 12-31-2012 12:12
UTILS_USREX2 = re.compile(r'us\D*([01]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)',re.I)
# 12-31-2012 12
UTILS_USREX3 = re.compile(r'us\D*([01]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)',re.I)
# 12-31-2012
UTILS_USREX4 = re.compile(r'us\D*([01]?\d)\D+([0123]?\d)\D+(\d{4})',re.I)

#12/2012
UTILS_MONTH_YEAR_REX0 =re.compile(r'^([0123]?\d)[^0123456789eujfmaosndaEUJFMAOSNDA]+(\d{4})',re.I) 

# 12-31-2012 12:12:12.1213
UTILS_EXCEPT_REX0 = re.compile(r'^([0123]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)',re.I)
# 12-31-2012 12:12:12
UTILS_EXCEPT_REX1 = re.compile(r'^([0123]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)',re.I)
# 12-31-2012 12:12
UTILS_EXCEPT_REX2 = re.compile(r'^([0123]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)',re.I)
# 12-31-2012 12
UTILS_EXCEPT_REX3 = re.compile(r'^([0123]?\d)\D+([0123]?\d)\D+(\d{4})\D+([012]?\d)',re.I)
# 12-31-2012
UTILS_EXCEPT_REX4 = re.compile(r'^([0123]?\d)\D+([0123]?\d)\D+(\d{4})',re.I)


#20121212 12:12:12.1212321
UTILS_REX_TIME_WITHOUT_SEPRATOR00=re.compile(r'(\d{8})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)')
#20121212 12:12:12
UTILS_REX_TIME_WITHOUT_SEPRATOR01=re.compile(r'(\d{8})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)')
#20121212 12:12
UTILS_REX_TIME_WITHOUT_SEPRATOR02=re.compile(r'(\d{8})\D+([012]?\d)[:]([0123456]?\d)')
#20121212 12
UTILS_REX_TIME_WITHOUT_SEPRATOR03=re.compile(r'(\d{8})\D+([012]?\d)')
#20121212
UTILS_REX_TIME_WITHOUT_SEPRATOR04=re.compile(r'(\d{8})')

#201212 12:12:12.1212321
UTILS_REX_TIME_WITHOUT_SEPRATOR10=re.compile(r'(\d{6})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)')
#201212 12:12:12
UTILS_REX_TIME_WITHOUT_SEPRATOR11=re.compile(r'(\d{6})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)')
#201212 12:12
UTILS_REX_TIME_WITHOUT_SEPRATOR12=re.compile(r'(\d{6})\D+([012]?\d)[:]([0123456]?\d)')
#201212
UTILS_REX_TIME_WITHOUT_SEPRATOR13=re.compile(r'(\d{6})')

#2012 12:12:12.1212321
UTILS_REX_TIME_WITHOUT_SEPRATOR20=re.compile(r'(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)')
#2012 12:12:12
UTILS_REX_TIME_WITHOUT_SEPRATOR21=re.compile(r'(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)')
#2012 12:12
UTILS_REX_TIME_WITHOUT_SEPRATOR22=re.compile(r'(\d{4})\D+([012]?\d)[:]([0123456]?\d)')

# 12:12:12.1212321 12.12.12.122113
UTILS_REX_PURE_TIME0=re.compile(r'^([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)$')
# 12:12:12
UTILS_REX_PURE_TIME1=re.compile(r'^([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)$')
# 12:12
UTILS_REX_PURE_TIME2=re.compile(r'^([012]?\d)[:]([0123456]?\d)$')

#2012-12-31 12:12:12.12213
UTILS_REX_STD_TIME0 = re.compile(r'(\d{4})\D+([01]?\d)\D+([0123]?\d)\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)')
#2012-12-31 12:12:12
UTILS_REX_STD_TIME1 = re.compile(r'(\d{4})\D+([01]?\d)\D+([0123]?\d)\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)')
#2012-12-31 12:12
UTILS_REX_STD_TIME2 = re.compile(r'(\d{4})\D+([01]?\d)\D+([0123]?\d)\D+([012]?\d)[:]([0123456]?\d)')
#2012-12-31 12
UTILS_REX_STD_TIME3 = re.compile(r'(\d{4})\D+([01]?\d)\D+([0123]?\d)\D+([012]?\d)')
#2012-12-31
UTILS_REX_STD_TIME4 = re.compile(r'(\d{4})\D+([01]?\d)\D+([0123]?\d)')
#2012-12
UTILS_REX_STD_TIME5 = re.compile(r'(\d{4})\D+([01]?\d)')
#2012
UTILS_REX_STD_TIME6 = re.compile(r'(\d{4})')

#01 Jan. 2012 12:12:12.1232
UTILS_ENCHRREX0 = re.compile(r'([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)', re.I)
#01 Jan. 2012 12:12:12
UTILS_ENCHRREX1 = re.compile(r'([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)', re.I)
#01 Jan. 2012 12:12
UTILS_ENCHRREX2 = re.compile(r'([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*(\d{4})\D+([012]?\d)[:]([0123456]?\d)', re.I)
#01 Jan. 2012 12
UTILS_ENCHRREX3 = re.compile(r'([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*(\d{4})\D+([012]?\d)', re.I)
#01 Jan. 2012
UTILS_ENCHRREX4 = re.compile(r'([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*(\d{4})', re.I)

#Jan. 01 2012 12:12:12.1232
UTILS_USCHRREX0 = re.compile(r'(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)', re.I)
#Jan. 01 2012 12:12:12
UTILS_USCHRREX1 = re.compile(r'(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)', re.I)
#Jan. 01 2012 12:12
UTILS_USCHRREX2 = re.compile(r'(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+(\d{4})\D+([012]?\d)[:]([0123456]?\d)', re.I)
#Jan. 01 2012 12
UTILS_USCHRREX3 = re.compile(r'(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+(\d{4})\D+([012]?\d)', re.I)
#Jan. 01 2012
UTILS_USCHRREX4 = re.compile(r'(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+(\d{4})', re.I)

#2012 01 Jan. 12:12:12.1232
UTILS_CHRREX0 = re.compile(r'(\d{4})\D+([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)', re.I)
#2012 01 Jan. 12:12:12
UTILS_CHRREX1 = re.compile(r'(\d{4})\D+([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)', re.I)
#2012 01 Jan. 12:12
UTILS_CHRREX2 = re.compile(r'(\d{4})\D+([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([012]?\d)[:]([0123456]?\d)', re.I)
#2012 01 Jan. 12
UTILS_CHRREX3 = re.compile(r'(\d{4})\D+([0123]?\d)\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([012]?\d)', re.I)
#2012 01 Jan. 
UTILS_CHRREX4 = re.compile(r'(\d{4})\D+([0123]?\d)\D*(January|Jan\.|Jan|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)', re.I)

#2012 Jan. 01  12:12:12.1232
UTILS_REX0 = re.compile(r'(\d{4})\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)\.(\d+)', re.I)
#2012 Jan. 01 12:12:12
UTILS_REX1 = re.compile(r'(\d{4})\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+([012]?\d)[:]([0123456]?\d)[:]([0123456]?\d)', re.I)
#2012 Jan. 01 12:12
UTILS_REX2 = re.compile(r'(\d{4})\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+([012]?\d)[:]([0123456]?\d)', re.I)
#2012 Jan. 01 12
UTILS_REX3 = re.compile(r'(\d{4})\D*(Jan|January|Jan\.|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)\D+([012]?\d)', re.I)
#2012 Jan. 01  
UTILS_REX4 = re.compile(r'(\d{4})\D*(January|Jan\.|Jan|Feb|Feb\.|February|Mar|Mar\.|March|Apr|Apr\.|April|May|Jun\.|June|Jun|Jul|July|Jul\.|Aug|Aug\.|August|Sep\.|September|Sep|Oct\.|Oct|October|Nov\.|November|Nov|Dec|Dec\.|December)\D*([0123]?\d)', re.I)


UTILS_AM_REX=re.compile(r'a[.]m',re.I)
UTILS_PM_REX=re.compile(r'p[.]m',re.I)

def leapyear(year):
    if year %400 == 0:
        return True
    if year %100 !=0 and year %4 == 0:
        return True
    return False
    
def restrip(text, param=' '):
    mo = re.compile(r'^([' + str(param) + r']*)(.*?)([' + str(param) + ']*)$')
    result = mo.search(text)
    if (result != None):
        return result.group(2)
    else:
        return WULL

def get_std_datestr(datestr):
    stddatestr = WULL
    year       = WULL
    month      = WULL
    day        = WULL
    hour       = WULL
    minute     = WULL
    second     = WULL
    msecond    = WULL
    srcdatestr = datestr
    datestr = restrip( datestr, '^0123456789faelrbihdvmsugpjncyotFAELRBIHDVMSUGPJNCYOT' )
    datestr_len = len(datestr)

    #0-------------------I know this is very ugly but useful.-------------------
    #12-31-2012 12:12:12.1213
    groups = UTILS_EXCEPT_REX0.search(datestr)
    if groups:
        raise ValueError('you should add en or us before the date str {0}'.format(datestr))

    groups = UTILS_EXCEPT_REX1.search(datestr)
    if groups:
        raise ValueError('you should add en or us before the date str {0}'.format(datestr))

    groups = UTILS_EXCEPT_REX2.search(datestr)
    if groups:
        raise ValueError('you should add en or us before the date str {0}'.format(datestr))

    groups = UTILS_EXCEPT_REX3.search(datestr)
    if groups:
        raise ValueError('you should add en or us before the date str {0}'.format(datestr))

    groups = UTILS_EXCEPT_REX4.search(datestr)
    if groups:
        raise ValueError('you should add en or us before the date str {0}'.format(datestr))
    #01/2012
    groups = UTILS_MONTH_YEAR_REX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = '01'
            month = groups.group(1)
            year = groups.group(2)
            hour = '00'
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #201201 12:12:12.12312
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR10.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = '01'
            hour = groups.group(2)
            minute = groups.group(3)
            second = groups.group(4)
            msecond = groups.group(5)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #201201 12:12:12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR11.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = '01'
            hour = groups.group(2)
            minute = groups.group(3)
            second = groups.group(4)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #201201 12:12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR12.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = '01'
            hour = groups.group(2)
            minute = groups.group(3)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #201201
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR13.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = '01'
            hour = '00'
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #2012 12:12:12.12312
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR20.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = '01'
            day = '01'
            hour = groups.group(2)
            minute = groups.group(3) 
            second =  groups.group(4)
            msecond = groups.group(5)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #2012 12:12:12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR21.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = '01'
            day = '01'
            hour = groups.group(2)
            minute = groups.group(3) 
            second =  groups.group(4)
            msecond = '0' 
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #2012 12:12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR22.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = '01'
            day = '01'
            hour = groups.group(2)
            minute = groups.group(3) 
            second =  '00'
            msecond = '0' 
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #20120102 12:12:12.12312
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR00.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = year_month_day[6:8]
            hour = groups.group(2)
            minute = groups.group(3)
            second = groups.group(4)
            msecond = groups.group(5)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #20120102 12:12:12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR01.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = year_month_day[6:8]
            hour = groups.group(2)
            minute = groups.group(3)
            second = groups.group(4)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #20120102 12:12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR02.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = year_month_day[6:8]
            hour = groups.group(2)
            minute = groups.group(3)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #20120102 12
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR03.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = year_month_day[6:8]
            hour = groups.group(2)
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #20120102
    groups = UTILS_REX_TIME_WITHOUT_SEPRATOR04.search(datestr)       
    if groups:
        year_month_day = groups.group(1)
        if len(groups.group(0)) == datestr_len:
            year = year_month_day[:4]
            month = year_month_day[4:6]
            day = year_month_day[6:8]
            hour = '00'
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #2012 Jan. 01 12:12:12.123123
    groups = UTILS_REX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(3)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 01 Jan. 2012 12:12:12.123123
    groups = UTILS_ENCHRREX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0
        
    # Feb.02 2012 12:12:12.123231
    groups = UTILS_USCHRREX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(1).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012 02 Feb. 12:12:12.123231
    groups = UTILS_CHRREX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(3).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012-02-01 12:12:12.12312312
    groups = UTILS_REX_STD_TIME0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            year = groups.group(1)
            month = groups.group(2)
            day = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # en01-02-2012 12:12:12.12231
    groups = UTILS_ENREX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = groups.group(2)
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #us01-02-2012 12:12:12.1231231 
    groups = UTILS_USREX0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = groups.group(1)
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = groups.group(7)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #1-------------------I know this is very ugly but useful.-------------------
    # 2012 Jan. 01 12:12:12
    groups = UTILS_REX1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(3)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 01 Jan. 2012 12:12:12
    groups = UTILS_ENCHRREX1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0
        
    # Feb.02 2012 12:12:12
    groups = UTILS_USCHRREX1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(1).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012 02 Feb. 12:12:12
    groups = UTILS_CHRREX1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(3).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012-02-01 12:12:12
    groups = UTILS_REX_STD_TIME1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            year = groups.group(1)
            month = groups.group(2)
            day = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # en01-02-2012 12:12:12
    groups = UTILS_ENREX1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = groups.group(2)
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #us 01-02-2012 12:12:12
    groups = UTILS_USREX1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = groups.group(1)
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = groups.group(6)
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #2-------------------I know this is very ugly but useful.-------------------
    # 2012 Jan. 01 12:12
    groups = UTILS_REX2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(3)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = groups.group(5)
            second ='00' 
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 01 Jan. 2012 12:12
    groups = UTILS_ENCHRREX2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second ='00' 
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0
        
    # Feb.02 2012 12:12
    groups = UTILS_USCHRREX2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(1).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #2012 02 Feb. 12:12
    groups = UTILS_CHRREX2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(3).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = groups.group(5)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012-02-01 12:12
    groups = UTILS_REX_STD_TIME2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            year = groups.group(1)
            month = groups.group(2)
            day = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #en01-02-2012 12:12
    groups = UTILS_ENREX2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = groups.group(2)
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #us 01-02-2012 12:12
    groups = UTILS_USREX2.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = groups.group(1)
            year = groups.group(3)
            hour = groups.group(4)
            minute = groups.group(5)
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #3-------------------I know this is very ugly but useful.-------------------
    #2012 Jan. 01 12
    groups = UTILS_REX3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(3)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute = '00'
            second ='00' 
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 01 Jan. 2012 12
    groups = UTILS_ENCHRREX3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute = '00'
            second ='00' 
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0
        
    # Feb.02 2012 12
    groups = UTILS_USCHRREX3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(1).upper()] 
            year = groups.group(3)
            hour = groups.group(4)
            minute ='00' 
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012 12 Feb.  12
    groups = UTILS_CHRREX3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(3).upper()] 
            year = groups.group(1)
            hour = groups.group(4)
            minute ='00' 
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012-02-01 12
    groups = UTILS_REX_STD_TIME3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            year = groups.group(1)
            month = groups.group(2)
            day = groups.group(3)
            hour = groups.group(4)
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # en01-02-2012 12
    groups = UTILS_ENREX3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = groups.group(2)
            year = groups.group(3)
            hour = groups.group(4)
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0
        
    #us 01-02-2012 12
    groups = UTILS_USREX3.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = groups.group(1)
            year = groups.group(3)
            hour = groups.group(4)
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #4-------------------I know this is very ugly but useful.-------------------

    # 2012 Jan. 01 
    groups = UTILS_REX4.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(3)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(1)
            hour ='00' 
            minute = '00'
            second ='00' 
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 01 Jan. 2012 
    groups = UTILS_ENCHRREX4.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = MONTH_DICT[groups.group(2).upper()] 
            year = groups.group(3)
            hour ='00' 
            minute = '00'
            second ='00' 
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0
        
    # Feb.02 2012
    groups = UTILS_USCHRREX4.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = MONTH_DICT[groups.group(1).upper()] 
            year = groups.group(3)
            hour = '00'
            minute ='00' 
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # 2012 02 Feb.
    groups = UTILS_CHRREX4.search(srcdatestr)
    if groups:
        day = groups.group(2)
        month = MONTH_DICT[groups.group(3).upper()] 
        year = groups.group(1)
        hour = '00'
        minute ='00' 
        second = '00'
        msecond = '0'
        stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
        return stddatestr, 0.0

    # 2012-02-01
    groups = UTILS_REX_STD_TIME4.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            year = groups.group(1)
            month = groups.group(2)
            day = groups.group(3)
            hour = '00'
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    # en01-02-2012
    groups = UTILS_ENREX4.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(1)
            month = groups.group(2)
            year = groups.group(3)
            hour = '00'
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #us 01-02-2012 
    groups = UTILS_USREX4.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = groups.group(2)
            month = groups.group(1)
            year = groups.group(3)
            hour = '00'
            minute = '00'
            second = '00'
            msecond = '0'
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0

    #5----UTILS_REX_PURE_TIME0----
    #12:12:12.123212
    groups = UTILS_REX_PURE_TIME0.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            if '-' in srcdatestr:
                raise ValueError('Negative Time(@-{0}) or Time(-0@{0}) should be used.'.format(datestr))
            day = '01'
            month = '01'
            year = '1970'
            hour = groups.group(1)
            minute = groups.group(2)
            second = groups.group(3)
            msecond = groups.group(4)
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, WULL
    #12:12:12
    groups = UTILS_REX_PURE_TIME1.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            if '-' in srcdatestr:
                raise ValueError('Negative Time(@-{0}) or Time(-0@{0}) should be used.'.format(datestr))
            day = '01'
            month = '01'
            year = '1970'
            hour = groups.group(1)
            minute = groups.group(2)
            second = groups.group(3)
            msecond ='0' 
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, WULL
    #12:12
    groups = UTILS_REX_PURE_TIME2.search(datestr)
    if groups:
        raise ValueError('It means 00:{0} or {0}:00.0?'.format(datestr))

    #1920-01
    groups = UTILS_REX_STD_TIME5.search(datestr)
    if groups:
        if len( groups.group(0)) == datestr_len:
            day = '01'
            month = groups.group(2)
            year = groups.group(1)
            hour = '00'
            minute = '00'
            second = '00' 
            msecond ='0' 
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0 
    #1920
    groups = UTILS_REX_STD_TIME6.search(datestr)
    if groups:
        if len( groups.group(0) ) == datestr_len:
            day = '01'
            month = '01'
            year = groups.group(1)
            hour = '00'
            minute = '00'
            second = '00' 
            msecond ='0' 
            stddatestr = year + '-' + month.rjust(2,'0') +'-'+ day.rjust(2,'0') + ' '+ hour.rjust(2,'0') + ':' + minute.rjust(2,'0') + ':' + second.rjust(2,'0') + '.' + msecond
            return stddatestr, 0.0 

    return stddatestr, 0.0

if __name__ == '__main__':
    #很多都可以实现但没什么必要，也增加了混乱
    s='2012'
    s='en1月2日2012 12:12:12.1200000'
    s='02 Jan. 2012 12:12:12.1231223'
    s='02 March 2012 12:12:12.1231223'
    s='02Feb. 2012 12:12:12.1231223'
    s='Feb02 2012, 12.12.12.1231223'
    s='Feb02 2012, 12.12.12.1231223 '
    s='Feb02 2012, 1.12.12.1231223  '
    s='en   1.2....2012-2.1:3.1999 '
    s='en1月2日2012 12:12:12.1200000 '
    s='02 Jan. 2012 12:12:12.1231223 '
    s='02 Jan. 2012 1:12:12.1231223 '
    s='en1月2日2012 12:12:12.1200000'
    s='en1月2日2012 12:12:12.1200000'
    s='2012'
    #s='en   -2.1:3'
    #s='us   1.2....2012-2:1:3.1999'
    #s='us   1.2....2012-2:1:3'
    #s='Feb02 2012 12:12:12'
    #s='en1月2日2012 12:12:12'
    #s='2012年1月2日 12:12:12'
    #s='2012年1月2日'
    #s='12:12:12.001'
    #s='12:12:12'
    #s='12:12'

    s='2012.01.01 12.12.12.12123'
    s='2012.01.01 12.12.12.12123'
    s='12:12'
    s='12.12.12.12123 2012.01.01'
    s='/2021/02/01/'
    s='2012'
    s='1940'
    s='en12321321312n'
    s='en/2021/02/01/'
    s='2012-02-01 12:12:12'
    s='/02-01-2021/'
    s='us01/01/1940 10:10:10.0'
    s='1901/01/19 10:10:10.0'
    s='us1940/01/01 10:10:10.0'
    s='1940年1月2日 12:12:12'
    #s = 'us01/12/2012'
    #s = 'us01/12/2012'
    #s='en/2021/02/01/'
    #s='19691231'
    #s='1940'
    #s='2012'
    #s='2012'
    #s='2012'
    #s='2012'
    print(s)
    print( get_std_datestr(s) )