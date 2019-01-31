
#根据函数特征查找对应K线形态的位置
#返回该K线形态的所有的时间点，以三维矩阵返回
#  'time', 'open', 'high', 'low', 'close'
import numpy as np
import KLineAnalysis.GetDate as KG
from matplotlib.ticker import Formatter
import matplotlib.dates as dates
import matplotlib.pylab as plt
import time
import warnings
warnings.filterwarnings("ignore")


#K线趋势的数据预测
#1基于规则理论进行的数据预测
#2获取深度学习需要的规范数据
#3获取K线的各种经典形态，并分析多方和空方的实力对比
class KLineFeatures:

    



    #趋势分析，判断整体是下降还是上升
    #KLineArray：为需要分析的部分，不是所有数据
    # 输入的数据KLineArray顺序为:
    #  'time', 'open', 'high', 'low', 'close'
    # FunPower：拟合函数的阶数，可作为趋势分析的精度
    #返回一个类
    def TrendAnalysis(self,KLineArray,FunPower):
        KLineArray = np.array(KLineArray)
        Ktime  = KLineArray[:,0]
        timeArray = []
        for i in range(0,len(Ktime) ):
            s = time.strptime(Ktime[i],"%Y%m%d")
            s = time.mktime(s)
            timeArray.append( s )
        timeArray = np.array(timeArray)
        #开盘价数据***
        z1 = np.polyfit(timeArray, KLineArray[:,1], FunPower)
        p1 = np.poly1d(z1)
        #最高价数据***
        z2 = np.polyfit(timeArray, KLineArray[:,2], FunPower)
        p2 = np.poly1d(z2)
        #最低价数据***
        z3 = np.polyfit(timeArray, KLineArray[:, 3], FunPower)
        p3 = np.poly1d(z3)
        #收盘价数据***
        z4 = np.polyfit(timeArray, KLineArray[:, 4], FunPower)
        p4 = np.poly1d(z4)

        # plt.plot(timeArray, KLineArray[:, 1])
        # plt.plot(timeArray, KLineArray[:, 2])
        # plt.plot(timeArray, KLineArray[:, 3])
        # plt.plot(timeArray, KLineArray[:, 4])
        #
        # plt.plot(timeArray,p1(timeArray) )
        # plt.plot(timeArray, p2(timeArray))
        # plt.plot(timeArray, p3(timeArray))
        # plt.plot(timeArray, p4(timeArray))
        # plt.show()
        return p1,p2,p3,p4


    # 寻找十字星
    # 输入的数据顺序为:
    #  'time', 'open', 'high', 'low', 'close'
    def Cross_stars(self,KLineArray):
        Rt = []
        print(KLineArray)
        KLineArray = np.array(KLineArray)
        for i in range(0,len(KLineArray) ):
            K1 = KLineArray[i]
            Ktime = K1[0]
            Kopen = K1[1]
            Khigh = K1[2]
            Klow  = K1[3]
            Kclose= K1[4]
            if np.abs(Khigh - Klow)>8*(np.abs(Kclose-Kopen) ):
                Rt.append(Ktime)
        return np.array(Rt)








if __name__ == "__main__":

    df = KG.GetDalyKLin('002495.SZ','20181101','20181231')
    df = KG.GetKLineData(df)
    a = np.array([])
    KLineFeatures = KLineFeatures()
    p1, p2, p3, p4 = KLineFeatures.TrendAnalysis(df,4)
    print(p1)
    print(p2)
    print(p3)
    print(p4)


