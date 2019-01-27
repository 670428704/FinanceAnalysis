
#根据函数特征查找对应K线形态的位置
#返回该K线形态的所有的时间点，以三维矩阵返回
#  'time', 'open', 'high', 'low', 'close'
import numpy as np
import KLineAnalysis.GetDate as KG


class KLineFeatures:

    #趋势分析，判断整体是下降还是上升
    #KLineArray 为需要分析的部分，不是所有数据
    # 输入的数据顺序为:
    #  'time', 'open', 'high', 'low', 'close'
    def TrendAnalysis(self,KLineArray):
        a=0


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

    df = KG.GetDalyKLin('600776.SH','20180101','20181231')
    df = KG.GetKLineData(df)
    a = np.array([])
    KLineFeatures = KLineFeatures()
    M = KLineFeatures.Cross_stars(df)
    print(M)
