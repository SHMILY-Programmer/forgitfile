
import matplotlib.pyplot as plt
from keras.utils import plot_model
import librosa
from sklearn.model_selection import train_test_split, StratifiedKFold
from keras.utils import to_categorical
from keras.layers import *
from keras.callbacks import *
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.models import load_model

Batch_Size = 128

#############################################

def D_open2(dirs):
    MAX_LEN = 0
    Datas = []
    Y = []
    i = 0
    for name in dirs:
        nn = os.listdir(DIR+'/'+name)
        #print("子目录",nn)
        for NN in nn:
            Data,sr = librosa.load(DIR+'/'+name+'/'+NN,sr=16000)
            Datas.append(Data)
            if(MAX_LEN<len(Data)):
                MAX_LEN=len(Data)
            Y.append(int(i))
        i += 1
        if i == 500:#加载500个就break
            break
    Datas = sequence.pad_sequences(Datas, maxlen=MAX_LEN,dtype='float32')
    X = []
    for xx in Datas:
        tmp = librosa.feature.mfcc(y=xx,sr=sr,n_mfcc=40)
        X.append(tmp)

    Y = np.asarray(Y)
    X = np.asarray(X)
    X = np.reshape(X,(X.shape[0],X.shape[1],X.shape[2],1))
    #print("X",X)
    return X , Y, i
###########################################
def cross_val_train(X,Y):#i
    kfold = StratifiedKFold(n_splits=10,shuffle=False)
    folds=[]
    for train,test in kfold.split(X,Y):
        X_train = X[train]
        X_test = X[test]
        Y_train = to_categorical(Y[train])
        Y_test = to_categorical(Y[test])
        folds.append([X_train, Y_train,X_test , Y_test])
        return folds
        #create_model(X_train,X_test,Y_train,Y_test,i)
        #print('acc: {0}%'.format(acc*100))


def create_model(folds,i):#X_train,X_test,Y_train,Y_test
    #创建顺序模型
    model=Sequential()
    print(X.shape[1],X.shape[2])

    #开始构建卷积层，当使用该层作为模型第一层时，需要提供 input_shape 参数用来指定输入的维度
    #1.filters：过滤器数量
    #指明 2D 卷积窗口的宽度和高度。 可以是一个整数，为所有空间维度指定相同的值
    #BatchNormalization()用来加快训练过程提高性能
    #定义激活函数为relu，非线性激活函数，如果使用sigmoid会发生梯度消失问题，relu计算量小于sigmoid
    #为什么要使用激活函数呢？如果不使用激励函数，不管神经网络有多少层，输出都是输入的线性组合，
    #这就属于最原始的感知机了，引入非线性激活函数就是让我们的神经网络随意逼近复杂函数，
    #让神经网络去处理复杂任务，非线性任务。
    #池化层用于
    model.add(Conv2D(32,kernel_size=(5,5),input_shape=(X.shape[1],X.shape[2],1)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))


    model.add(Conv2D(32,kernel_size=(2,2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(32,kernel_size=(2,2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(32,kernel_size=(2,2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2,2)))

    # Flatten层把多维的输入一维化，常用在从卷积层到全连接层的过度。
    model.add(Flatten())
    #Dropout降低模型复杂度，任意丢弃神经网络层中的输入，防止过拟合
    model.add(Dropout(0.4))

    model.add(Dense(32,activation='relu'))
    # 增加输出层
    model.add(Dense(i,activation='softmax'))
    #通过.compile来配置学习过程
    model.compile(loss='categorical_crossentropy'
                  ,optimizer='rmsprop',metrics=["accuracy"])

    accs_history=[]
    for fold in folds:
        history= model.fit(fold[0], fold[1], batch_size=Batch_Size, verbose=1,epochs=150)  # ,batch_size=Batch_Size,verbose=0,epochs=660
        # 绘制训练 & 验证的准确率值
        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.sans-serif'] = ['SimHei']

        plt.plot(history.history['acc'])
        #plt.plot(history.history['val_acc'])
        plt.title('模型准确度')
        plt.ylabel('准确度')
        plt.xlabel('轮次')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.savefig("acc.png",format='png')
        plt.show()

        # 绘制训练 & 验证的损失值
        plt.plot(history.history['loss'])
        #plt.plot(history.history['val_loss'])
        plt.title('模型损失度')
        plt.ylabel('损失度')
        plt.xlabel('轮次')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.savefig("loss.png", format='png')
        plt.show()
        acc_history=history.history['acc']
        # score, acc = model.evaluate(X_test, Y_test, batch_size=Batch_Size)
        print("保存模型")
        #joblib.dump(model, "CNN_model.plk")
        model.save("CNN_Model.h5")
        print("保存完成")
        accs_history.append(acc_history)

    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    #这里把模型每层的输入输出维度表示出来。
    plot_model(model, to_file='model.png',show_shapes=True)
    avg_history=np.mean(accs_history)
    print("总轮数平均精度：{0}%".format(avg_history*100))
    Apply_Model(folds)


def Apply_Model(folds):
    accs = []
    for fold in folds:
        print("加载模型")
        #model = joblib.load("CNN_model.plk")
        model=load_model("CNN_Model.h5")
        print("加载完成")
        print("开始预测：")
        #score,acc
        score= model.evaluate(fold[2], fold[3], batch_size=Batch_Size)
        accs.append(score[1])
    print("accs列表为：", accs)
    avg_acc = np.mean(accs)
    print("eval_avg_acc: {0}%".format(avg_acc * 100))

if __name__ == '__main__':
    DIR = '音频文件' #target folder
    #open files
    dirs = os.listdir(DIR)
    print("目录为：",dirs)
    X = []
    Y = []
    i = 0
    X ,Y ,i = D_open2(dirs)
    #print(X,Y,i)
    folds=cross_val_train(X,Y)#i
    create_model(folds,i)
