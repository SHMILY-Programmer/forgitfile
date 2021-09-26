import numpy
import config
import time
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt
#将数据集拆分为特征x和标签y
def split_dframe_x_y(dframe):
    dnumpy=numpy.array(dframe)
    size=dnumpy.shape[1]
    #print('dnumpy.shape',dnumpy.shape)
   # print("size",size)
    x_dnumpy=dnumpy[:,:size-1]
    y_dnumpy=dnumpy[:,size-1]
    return x_dnumpy,y_dnumpy

#将数据集分为训练集和测试集
def split_dnumpy_train_test(dnumpy_x,dnumpy_y):
    #创建分层K折交叉验证(1000)层
    #StratifiedKFold 分层采样交叉切分，确保训练集，测试集中各类别样本的比例与原始数据集中相同。
    kfold=StratifiedKFold(n_splits=config.Model.n_splits)
    folds=[]
    #循环分层中的训练下标和测试下标
    for train_index,test_index in kfold.split(dnumpy_x,dnumpy_y):
        #print("Train Index:", train_index, ",Test Index:", test_index)
        x_train,x_test =dnumpy_x[train_index],dnumpy_x[test_index]
        y_train,y_test=dnumpy_y[train_index],dnumpy_y[test_index]
        folds.append([x_train,y_train,x_test,y_test])
    return folds

def train_model(model,data_x,data_y):
    model.fit(data_x,data_y)



#应用k折交叉验证
def apply_SKfold(model,folds):
    #得到当前时间
    start_time=time.time()
    print("folds:",len(folds))
    scores=[]
    count=0
    for fold in folds:
        #训练模型
        model.fit(fold[0],fold[1])
        #测试模型分数
        score=model.score(fold[2],fold[3])
        print("训练集大小:",fold[1].size,"测试集大小:",fold[3].size)
        print("预测分数:",score)
        scores.append(score)
        print(" -----")
        count=count+1
    print("总轮数：",count)
    #计算平均分数
    avg_score=numpy.mean(scores)
    #计算训练和测试模型消耗的时间
    time_consumed=time.time()-start_time
    print("-------------------------------------")
    print("模型平均分数:",avg_score)
    print("消耗时间:",time_consumed,"秒")


