import Extracter_OF_Feature
import SignalProcesser
import Select_OF_File
import config
import numpy
import pandas
def main():
    #设置属性
    samp_rate=config.Audio.samp_rate
    flen=config.Audio.flen
    hlen=config.Audio.hlen
    DATA_PATH=config.Paths.DATA_PATH

    #获取子文件夹
    train_folders= Select_OF_File.get_subdir(DATA_PATH)
    #print(train_folders)
    #此标志用来控制是否创建了数据表
    flag=False
    labels=[]
    print("正在创建csv文件....")
    for folder in train_folders:
        #得到文件夹中每个音频的样本数组
        sample_arrays= SignalProcesser.get_sample_arrays(DATA_PATH, folder, samp_rate)
        for sample_array in sample_arrays:
            #从样本数组中提取特征
            mfccs= Extracter_OF_Feature.extract_mfccs(sample_array, samp_rate, flen, hlen)
            if not flag:
                dataset_numpy=numpy.array(mfccs)
                flag=True
            elif flag:
                #如果创建了，往文件中添加新的特征
                dataset_numpy=numpy.vstack((dataset_numpy,mfccs))

            #将最终的numpy数组转换成DataFrame
            dataset_pandas=pandas.DataFrame(dataset_numpy)

            #将说话者的名字添加到labels数组中
            for i in range(0,mfccs.shape[0]):
                labels.append(folder)


    #在speaker列下为没一行添加说话者的名字
    dataset_pandas["speaker"]=labels
    #生成csv文件
    dataset_pandas.to_csv("dataset.csv",index=False,encoding="gbk")
    print("数据集已成功生成并且添加到项目目录中！")

if __name__ == "__main__":
    main()