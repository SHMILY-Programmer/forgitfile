import python_speech_features
import config
import numpy
import librosa
#从样本数组中提取梅尔频率倒谱系数
def extract_mfccs(sample_array,sampling_rate,flen,hlen):
    #winlen - 分析窗口的长度，按秒计，默认0.025s(25ms)
    #winstep - 连续窗口之间的步长，按秒计，默认0.01s（10ms）
    #numcep - 倒频谱返回的数量，默认13
    #winfunc - 分析窗口应用于每个框架.
    #返回:一个大小为numcep的numpy数组，包含着特征，每一行都包含一个特征数组。
    mfccs=python_speech_features.mfcc(sample_array,sampling_rate,winlen=flen,winstep=hlen,
                                numcep=13,winfunc=config.Windowing.hamming)
    #print(mfccs)
    mfccs=numpy.array(mfccs)
    #print(mfccs)
    mfccs=mfccs[:,1:]
    #print('mfccs.shape[0]', mfccs.shape[0])
    #print(mfccs)

    return mfccs

#此方法用于提取测试音频文件的mfccs
def extract_features(sample_array,sampling_rate,flen,hlen):

    mfccs=extract_mfccs(sample_array,sampling_rate,flen,hlen)
    return mfccs