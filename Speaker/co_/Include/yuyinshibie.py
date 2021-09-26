import time
import librosa
import config
from sklearn.externals import joblib
import Extracter_OF_Feature
import itertools
import operator
import sys
# from keras.models import load_model
# from keras.preprocessing import sequence
import numpy as np
def findCommon(labels):
    #获得(item,iterable)对的迭代器
    ITEST=sorted((x,i) for i,x in enumerate(labels))
    #print("SL：",SL)
    groups=itertools.groupby(ITEST,key=operator.itemgetter(0))
    #for a ,b in itertools.groupby(SL,key=operator.itemgetter(0)):
       # print("a:",a)
       # print("b:", b)
    #辅助方法用来统计最大的count和最大的min_index
    def _assistfun(g):
        item,iterable=g
        # print("g:",g)
        # print("item:",item)
        #print("iterable:", iterable)
        count=0;
        min_index=len(labels)
        #print("min_index:",min_index)
        #print("进入for循环")
        for _ ,where in iterable:
            #print("_:",_)
           # print("where:",where)
            count += 1
            min_index=min(min_index,where)
            #print("min_index",min_index)
            #print("count:",count)
            #print("------------------------------------------------")
        # print("-min_index:",-min_index)
        # print("count:",count)
        #计算最高计数
        return count,-min_index


    return max(groups,key=_assistfun)[0]



def findthespeaker(samp_array,samp_rate,flen,hlen):
    #从测试音频文件中获取特征
    features_mfccs= Extracter_OF_Feature.extract_features(samp_array, samp_rate, flen, hlen)
    model=joblib.load("C:/file/Speaker/co_/Include/KNC_model.plk")
    #使用模型预测说话人
    predicted_labels=model.predict(features_mfccs)
    # print("predicted_labels",predicted_labels)
    #得到说话人结果
    result=findCommon(predicted_labels)
    return result


def main(audio_path):
    #属性赋值
    samp_rate=config.Audio.samp_rate
    flen=config.Audio.flen
    hlen=config.Audio.hlen

    #获取测试音频文件的样本数组
    samp_array, sr = librosa.load(audio_path,sr=config.Audio.samp_rate,mono=True)
    #获得当前时间
    start_time=time.time()
    #获得音频文件的说话人
    result=findthespeaker(samp_array,samp_rate,flen,hlen)
    #计算时间消耗
    time_consum=time.time()-start_time
    # print("---------------------------------------------------")
    # print("该音频文件的说话人是：",result,"  耗时：",str(time_consum),"秒")
    print(result)
    return result


if __name__ == "__main__":
    main(sys.argv[1])
    #CNN_test()
























