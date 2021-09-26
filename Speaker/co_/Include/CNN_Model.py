import numpy as np
import pandas as pd
import time
import librosa
import config
from keras.models import load_model
from TrainTestProcesser import split_dnumpy_train_test
from TrainTestProcesser import apply_SKfold
from keras.utils import to_categorical
import Extracter_OF_Feature
from sklearn.model_selection import train_test_split, StratifiedKFold
from keras.layers import *
from keras.callbacks import *
from keras.models import Sequential
from keras import optimizers
from keras.preprocessing import sequence
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.externals import joblib


#从Keras导入线性模型类。这是一个简单的线性神经网络层，
# 它非常适合用在我们正在构建的前馈CNN中。
from keras.models import Sequential
#从Keras导入核心层，这些层几乎所有的神经网络都会用到
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import TrainTestProcesser
import itertools
import operator


def main():
    Cnn_Modify()
    # 属性赋值
    #samp_rate = config.Audio.samp_rate
    #flen = config.Audio.flen
    #hlen = config.Audio.hlen
    # 获取测试音频文件的样本数组
    # result = findthespeaker(samp_array, samp_rate, flen, hlen)
    #return result

def findthespeaker(samp_array,samp_rate,flen,hlen):
    #从测试音频文件中获取特征
    features_mfccs= Extracter_OF_Feature.extract_features(samp_array, samp_rate, flen, hlen)
    #model=joblib.load("CNN_model.plk")
    model=load_model('CNN_model.h5')
    #使用模型预测说话人
    predicted_msg=model.predict(features_mfccs)
    #print("predicted_labels",predicted_labels)
    #得到说话人结果
    result=predicted_msg

    #result = findCommon(predicted_msg)
    #result1 = encoder.inverse_transform()
    print(type(predicted_msg))

    #print(predicted_msg)
    #test_liss=model.evaluate(features_mfccs)
    print(result)
    return result


def Cnn_Modify():
    data_set = pd.read_csv("dataset.csv", index_col=False, encoding='gbk')
    print("数据集的shape：", data_set.shape)
    # 将数据集分为特征x和标签y
    Feature_x, tag_y = TrainTestProcesser.split_dframe_x_y(data_set)
    #Feature_x=pad_sequences(Feature_x)
    Feature_x=np.asarray(Feature_x)
    tag_y=np.asarray(tag_y)

    Feature_x = np.reshape(Feature_x, (Feature_x.shape[0], Feature_x.shape[1],Feature_x.shape[1], 1))
    print("reshape后的Feature_x:",Feature_x)
    print("Feature_x.shape:",Feature_x.shape)
    cross_val_train(Feature_x, tag_y)
    #create_model(Feature_x)


    #recognizer = Sequential()
    #构建卷积层：
    #filters：过滤器数量  2.指定卷积窗口的高和宽3.卷积如何处理边缘4.激活函数
   # recognizer.add(Conv2D(32, 3, activation ='relu', input_shape = (15437,12)))
    #recognizer.add(Conv2D(32, 3,activation ='relu'))
    #recognizer.add(Dropout(rate=.2))
    #构建池化层，指定池化口的高度和宽度
   # recognizer.add(MaxPool2D(pool_size=(2,2)))
    # recognizer.add(Dense(units = 256, activation = "relu"))
    # recognizer.add(Dropout(0.25))

    #recognizer.add(Conv2D(64, 3,activation ='relu'))
    #recognizer.add(MaxPool2D(pool_size=(2, 2)))

    #recognizer.add(Flatten())

    #recognizer.add(Dense(units = 124, activation = "relu"))
    #recognizer.add(Dropout(.2))

    #recognizer.add(Dense(4, activation='softmax'))
    #recognizer.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # units: 正整数，输出空间维度。
    # activation: 激活函数

    # units: 正整数，输出空间维度。
    # activation: 激活函数
    #recognizer.add(Dense(units=256, activation='relu'))
    #recognizer.add(Dense(units=256, activation="relu"))
    #recognizer.add(Dropout(0.5))
   # recognizer.add(Dense(units=100, activation="softmax"))

    #optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    # optimizer: 字符串（优化器名）或者优化器对象。详见 optimizers。
    # loss: 字符串（目标函数名）或目标函数。
    # 如果模型具有多个输出，则可以通过传递损失函数的字典或列表，
    # 在每个输出上使用不同的损失。模型将最小化的损失值将是所有单个损失的总和。
    # metrics: 在训练和测试期间的模型评估标准。通常你会使用 metrics = ['accuracy']。
    # 要为多输出模型的不同输出指定不同的评估标准
    #recognizer.compile(optimizer=optimizer, loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    # batch_size: 整数或 None。每次提度更新的样本数。如果未指定，默认为 32.
    # epochs: 整数。训练模型迭代轮次。一个轮次是在整个 x 或 y 上的一轮迭代。
    # 请注意，与 initial_epoch 一起，epochs 被理解为 「最终轮次」。
    # 模型并不是训练了 epochs 轮，而是到第 epochs 轮停止训练。
   # recognizer.fit(Feature_x, tag_y, epochs=12, batch_size=32,verbose=2)
   # recognizer.save("CNN_model.h5")
    # joblib.dump(recognizer,"CNN_model.plk")

def cross_val_train(Feature_x, tag_y):
    kfold = StratifiedKFold(n_splits=config.Model.n_splits,shuffle=False)
    # 循环分层中的训练下标和测试下标
    for train_index, test_index in kfold.split(Feature_x, tag_y):
        # print("Train Index:", train_index, ",Test Index:", test_index)
        x_train, x_test = Feature_x[train_index], tag_y[test_index]
        y_train, y_test = Feature_x[train_index], tag_y[test_index]
        create_model(Feature_x,x_train,x_test,y_train,y_test)

    #Kfloads=split_dnumpy_train_test(X,Y)
    #return Kfloads
    #kfold = StratifiedKFold(n_splits=10,shuffle=False)
    #for train,test in kfold.split(X,Y):
    ##    X_train = X[train]
    #    X_test = X[test]
    #    Y_train = to_categorical(Y[train])
    #    Y_test = to_categorical(Y[test])
    #    acc = create_model(X_train,X_test,Y_train,Y_test,i)
    #    print('acc: {0}%'.format(acc*100))


def create_model(Feature_x, x_train, x_test, y_train, y_test):
    model = Sequential()

    model.add(Conv2D(64, kernel_size=(2, 2),
                     input_shape=(Feature_x.shape[1], Feature_x.shape[2], 1)))  # ,data_format='channels_first')
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(1, 1)))

    model.add(Conv2D(32, kernel_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(1, 1)))

    model.add(Conv2D(32, kernel_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(1, 1)))

    model.add(Conv2D(32, kernel_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(1, 1)))

    # Flatten层把多維的輸入一維化，常用在從卷積層到全連接層的過渡。
    model.add(Flatten())

    model.add(Dropout(0.4))
    model.add(Dense(32, activation='relu'))
    # Add output layer
    model.add(Dense(7, activation='softmax'))

    model.compile(loss='categorical_crossentropy'
                  , optimizer='adam', metrics=["accuracy"])

    # Show model information
    # model.summary()
    # ES=EarlyStopping(monitor='val_acc',patience=1000,mode='max')
    # model.fit(X_train,Y_train,batch_size=32,
    #      verbose=0,epochs=660)

    # score, acc = model.evaluate(X_test, Y_test, batch_size=32)
    # print(score,acc)
    # joblib.dump(model, "CNN_model.plk")
    # apply_SKfold(model,folds)

    # 训练模型
    # print(fold)
    model.fit(x_train, y_train, batch_size=32, verbose=1, epochs=50)
    score, acc = model.evaluate(x_test, y_test, batch_size=32)
    print("score:", score, "acc:", acc)


if __name__ == "__main__":
    main()