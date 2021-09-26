#0        from sklearn.model_selection import StratifiedKFold 
#1        import numpy as np                                  
#2        x=np.array([[1,2,3,4],                              
#3            [11,12,13,14],                                  
#4            [21,22,23,24],                                  
#5            [31,32,33,34],                                  
#6            [41,42,43,44],                                  
#7            [51,52,53,54],                                  
#8            [61,62,63,64],                                  
#9            [71,72,73,74]])                                 
#10       print(x)                                            
#11       y=np.array([1,1,0,0,1,1,0,0])                       
#12       kfolder = StratifiedKFold(n_splits=4)               
#13       print(kfolder)                                      
#14       for train,test in kfolder.split(x,y):               
#15           print("train:",train)                           
#16           print("test:", test)                            
