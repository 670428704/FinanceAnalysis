
#这个库里的文件，为了获取股票期货等的信息，例如上市时间，退市时间，价格信息等

import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import mpl_finance as mpf
from matplotlib.pylab import date2num
import datetime
from matplotlib.ticker import Formatter



#获取所有股票的代码和名字
def GetAllShareCode():
    # a = np.array( ts.get_today_all() )
    # code = a[:,0]
    # name = a[:,1]
    pro = ts.pro_api('87018450f256d5d07ff80f6084787c59ad2c3d9be41fd7b269ffab9e')
    data = np.array( pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date') )
    #返回的code包括交易所信息
    code = data[:,0]
    name = data[:,2]
    ListedTime = data[:,5]
    return code,name,ListedTime


#获取某支股票的日k线
def GetDalyKLin(code,stareTime,endTime):
    pro = ts.pro_api('87018450f256d5d07ff80f6084787c59ad2c3d9be41fd7b269ffab9e')
    df = pro.query('daily', ts_code=code, start_date=stareTime, end_date=endTime)
    return df


#将股票的原始日K线数据转化为用于显示K线的数据
def GetKLineData(DataArray):
    DataArray = np.array(DataArray)
    KLineDataArray=np.delete(DataArray,[0,6,7,8,9,10],axis=1)
    return KLineDataArray



#将时间字符串转为candlestick_ockl可读的格式
#  'time', 'open', 'high', 'low', 'close'
def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y%m%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time


#输入数据矩阵，显示K线图
def PlotKLine(dfcvs):
    dfcvs = pd.DataFrame(dfcvs)
    dfcvs.columns = ['time', 'open', 'high', 'low', 'close']
    dfcvs['time'] = pd.to_datetime(dfcvs['time'], format="%Y%m%d")

    # matplotlib的date2num将日期转换为浮点数，整数部分区分日期，小数区分小时和分钟
    # 因为小数太小了，需要将小时和分钟变成整数，需要乘以24（小时）×60（分钟）=1440，这样小时和分钟也能成为整数
    # 这样就可以一分钟就占一个位置

    dfcvs['time'] = dfcvs['time'].apply(lambda x: dates.date2num(x))
    data_mat = dfcvs.as_matrix()

    fig, ax = plt.subplots(figsize=(1200 / 72, 480 / 72))

    fig.subplots_adjust(bottom=0.1)
    mpf.candlestick_ohlc(ax, data_mat, colordown='g', colorup='r', width=0.7, alpha=1)

    # 将x轴的浮点数格式化成日期小时分钟
    # 默认的x轴格式化是日期被dates.date2num之后的浮点数，因为在上面乘以了1440，所以默认是错误的
    # 只能自己将浮点数格式化为日期时间分钟
    # 参考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
    class MyFormatter(Formatter):
        def __init__(self, dates, fmt='%Y/%m/%d'):
            self.dates = dates
            self.fmt = fmt

        def __call__(self, x, pos=0):
            'Return the label for time x at position pos'
            ind = int(np.round(x))
            # ind就是x轴的刻度数值，不是日期的下标

            return dates.num2date(ind).strftime(self.fmt)

    formatter = MyFormatter(data_mat[:, 0])
    ax.xaxis.set_major_formatter(formatter)

    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_horizontalalignment('right')

    plt.show()


if __name__ == "__main__":
    df = GetDalyKLin('002495.SZ','20180101','20181231')
    print( df.axes )
    df = GetKLineData(df)
    print(df)
    PlotKLine(df)
    # dateTest = ['20181228','20181227']

    # PlotKLineIden(df,dateTest)


    # code, name,ListedTime=GetAllShareCode()
    # print(code,name,ListedTime)



