#数据准备
import pandas as pd
import matplotlib.pyplot as plt
import jieba.analyse
data = pd.read_excel("C:/Users/17500/Desktop/data/zhanlang2.xlsx")


#数据预处理阶段
data = data.dropna()    #删除数据中的空行
#数据探索阶段
data_shape = data.shape  #查看数据特征
data_recommend = data['推荐'] #分离出推荐情况
data_time = data['时间']   #分离出影评的时间
data_comment = data['评论内容']  #分离出具体评论内容
data_recomment_count = data_recommend.value_counts()  #统计出各个推荐出现的次数
#因为考虑数据集原时间精确到秒，细粒度过高，我们分割该时间字段，拿出具体的日期
time_1 = data_time.values
list_time=[]
for time in time_1:
    time_2 = time.split(" ")
    date = time_2[0]
    list_time.append(date)
Serise_time = pd.Series(list_time)
data_time_count = Serise_time.value_counts()  #统计不同时间段的评价人数

#电影推荐情况数据可视化
plt.figure()
plt.title("战狼2电影推荐情况直览")
#data_recomment_count.plot(kind="bar")
plt.bar(data_recomment_count.index,data_recomment_count.values)
#plt.plot()
#plt.xticks(data_recomment_count.index)
#plt.yticks(data_recomment_count.values)
plt.xlabel("推荐指数")
plt.ylabel("推荐个数")
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()

#不同时间段评价人数变化数据可视化
plt.figure()
plt.title("战狼2影评时间分布直览")
plt.bar(data_time_count.index,data_time_count.values)
#data_time_count.plot(kind="bar")
plt.xlabel("日期")
plt.ylabel("评论个数")
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()

#数据挖掘分类之一：简易文本挖掘
#文本去重
l1=len(data_comment)
data_comment_unique = data_comment.unique()
l2=len(data_comment_unique)
comment_uniqye = pd.Series(data_comment_unique)
print("删除了%s条相同评论"%(l1-l2))
comment_uniqye = pd.DataFrame(comment_uniqye,columns=['评论'])

comment_uniqye.to_csv("C:/Users/17500/Desktop/data/comment.txt",index=False,header=False,encoding='utf-8')
path="C:/Users/17500/Desktop/data/comment.txt"
fp=open(path,'r',encoding="utf-8")
content = fp.read()
try:
    jieba.analyse.set_stop_words("C:/Users/17500/Desktop/data/stoplist.txt")
    tags=jieba.analyse.extract_tags(content,topK=100,withWeight=True)
    for item in tags:
        print(item[0]+'\t'+str(int(item[1]*1000)))
finally:
    fp.close()