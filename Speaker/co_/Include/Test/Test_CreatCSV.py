import Extracter_OF_Feature
import SignalProcesser
import config
import numpy
import pandas
import sys
sys.setrecursionlimit(1000000)

def main():
    samp_rate = config.Audio.samp_rate
    flen = config.Audio.flen
    hlen = config.Audio.hlen
    DATA_PATH = config.Paths.DATA_PATH
    # 获取子文件夹
    #train_folders = FileFinder.get_subdir(DATA_PATH)
    flag = False
    labels = []
    print("正在创建csv文件....")

    sample_arrays = SignalProcesser.get_sample_arrays(DATA_PATH, "天使", samp_rate)
    print("样本数组总和:",sample_arrays)
    for sample_array in sample_arrays:
            # 从样本数组中提取特征
        print("每一个音频文件的样本数组:",sample_array)
        print(sample_array.size)
        mfccs = Extracter_OF_Feature.extract_mfccs(sample_array, samp_rate, flen, hlen)
        print("mfccs:",mfccs)
        print("mfccs的大小",mfccs.size)
        print(mfccs.shape)
        print(mfccs.shape[0])
        if not flag:
            dataset_numpy = numpy.array(mfccs)
            print("dataset_numpy:",dataset_numpy)
            flag = True
        elif flag:
            dataset_numpy = numpy.vstack((dataset_numpy, mfccs))
            print("dataset_numpy2:",dataset_numpy)
        for i in range(0, mfccs.shape[0]):
            labels.append("天使")

        dataset_pandas = pandas.DataFrame(dataset_numpy)
        print("dataset_pandas:",dataset_pandas)
        print("--------------------------------------------------------------------------------------------------")
        dataset_pandas["speaker"]=labels




    #dataset_pandas["speaker"] = labels
    dataset_pandas.to_csv("dataset.csv", index=False, encoding="gbk")
    print("数据集已成功生成并且添加到项目目录中！")


if __name__ == "__main__":
    main()