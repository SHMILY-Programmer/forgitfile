import librosa
import numpy
import librosa.display
from matplotlib import pyplot as plt
#在个人音频训练文件夹中得到每一个音频的样本数组
def get_sample_arrays(train_dir,folder_name,samp_rate):
    #得到路径
    path_audios=librosa.util.find_files(train_dir+"/"+folder_name)
    #定义一个列表来存储每个音频文件的样本数组
    audios=[]
    for audio in path_audios:
        x, sr = librosa.load(audio, sr=16000, mono=True)
        audios.append(x)
        #画出所有音频文件的波形图
        # plt.show()
        librosa.display.waveplot(x,sr)
        plt.rcParams['axes.unicode_minus']=False
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.title("波形图")
        #plt.show()

    #画出所有音频文件的频谱图
    for audio2 in path_audios:
         x, sr = librosa.load(audio2, sr=samp_rate, mono=True)
         melspec=librosa.feature.melspectrogram(x,sr)
         logmelspec=librosa.power_to_db(melspec)
         plt.rcParams['axes.unicode_minus'] = False
         plt.rcParams['font.sans-serif'] = ['SimHei']
         plt.figure()
         librosa.display.specshow(logmelspec,sr=samp_rate,x_axis='time',y_axis='mel')
         plt.colorbar(format='%+2.0f dB')
         plt.title("频谱图")
         # plt.show()


    #print(audios)
    audios_numpy=numpy.array(audios)
    #print(len(audios_numpy))
    #print(audios_numpy)
    return audios_numpy






