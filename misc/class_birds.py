import os
import pickle
import pandas as pd




namepath = 'Data/birds/CUB_200_2011/images.txt'
splitpath = 'Data/birds/CUB_200_2011/train_test_split.txt'
classpath = 'Data/birds/CUB_200_2011/classes.txt'

df_filenames = pd.read_csv(namepath, delim_whitespace=True, header=None)
filenames = df_filenames[1].tolist()

df_splitflag = pd.read_csv(splitpath, delim_whitespace=True, header=None)
splitflag = df_splitflag[1].tolist()

df_classname = pd.read_csv(classpath, delim_whitespace=True, header=None)
classname = df_classname[1].tolist()

train = []
test = []

for i in range(0,len(filenames)):
    if splitflag[i] == 1:
       train.append(filenames[i])
    else:
       test.append(filenames[i])

class_train = []
class_test = []

for j in range(0,len(train)):
    class_train.append(classname[int(train[j][0:3])-1])

for j in range(0,len(test)):
    class_test.append(classname[int(test[j][0:3])-1])



with open('Data/birds/train/class_info.pickle','wb') as f:
     pickle.dump(class_train,f)

with open('Data/birds/test/class_info.pickle','wb') as f:
     pickle.dump(class_test,f)


