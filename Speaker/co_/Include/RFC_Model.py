import pandas
from sklearn.externals import joblib
import TrainTestProcesser
from sklearn.ensemble import RandomForestClassifier
from Select_OF_File import get_subdir
import matplotlib.pyplot as mp
import sklearn.model_selection as ms
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np
import itertools
def main():
    #获取数据集
    #不使用第一列作为行索引
    data_set = pandas.read_csv("dataset.csv",index_col=False,encoding='gbk')
    print("数据集的shape：",data_set.shape)
    #将数据集分为特征x和标签y
    dnumpy_x,dnumpy_y = TrainTestProcesser.split_dframe_x_y(data_set)
    #使用StratifiedKFold将数据集分为训练集和测试集
    folds= TrainTestProcesser.split_dnumpy_train_test(dnumpy_x, dnumpy_y)
    #创建模型
    model=RandomForestClassifier(n_estimators=23)
    #使用kfol交叉验证
    TrainTestProcesser.apply_SKfold(model, folds)
    #训练模型
    TrainTestProcesser.train_model(model, dnumpy_x, dnumpy_y)
    #保存模型以备将来使用
    joblib.dump(model,"RFC_model.plk")



def getconfusion_matrix():
    mp.rcParams['font.family'] = ['sans-serif']
    mp.rcParams['font.sans-serif'] = ['SimHei']
    classes=get_subdir("音频文件")
    data_set = pandas.read_csv("dataset.csv",index_col=False,encoding='gbk')
    dnumpy_x, dnumpy_y = TrainTestProcesser.split_dframe_x_y(data_set)
    train_x, test_x, train_y, test_y = ms.train_test_split(dnumpy_x, dnumpy_y, test_size=0.25, random_state=7)
    model=joblib.load("RFC_model.plk")
    pred_test_y = model.predict(test_x)
    #混淆矩阵
    cm=confusion_matrix(test_y, pred_test_y)
    # 获取分类报告
    r = classification_report(test_y, pred_test_y)
    print('分类报告为：', r, sep='\n')

    mp.figure()
    plot_confusion_matrix(cm, classes=classes, normalize=True,
                          title='随机森林分类器混淆矩阵')

def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',
                                                            cmap=mp.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("混淆矩阵归一化")
    else:
        print('混淆矩阵未归一化')

    print("混淆矩阵为：",cm)

    mp.imshow(cm, interpolation='nearest', cmap=cmap)
    mp.title(title)
    mp.colorbar()
    tick_marks = np.arange(len(classes))
    mp.xticks(tick_marks, classes, rotation=45)
    mp.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        mp.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    mp.tight_layout()
    mp.ylabel('True label')
    mp.xlabel('Predicted label')
    mp.savefig('confusion_matrix_RFC.png', format='png')
    mp.show()







if __name__ == "__main__":
    main()
    getconfusion_matrix()