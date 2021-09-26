from sklearn.model_selection import StratifiedKFold
import numpy as np
x=np.array([[1,2,3,4],
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34],
    [41,42,43,44],
    [51,52,53,54],
    [61,62,63,64],
    [71,72,73,74]])
print(x)
y=np.array([1,1,0,0,1,1,0,0])
kfolder = StratifiedKFold(n_splits=4)
print(kfolder)
for train,test in kfolder.split(x,y):
    print("train:",train)
    print("test:", test)