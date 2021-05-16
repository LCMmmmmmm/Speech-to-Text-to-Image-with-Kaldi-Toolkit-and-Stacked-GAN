import os
import pickle
import pandas as pd




namepath = 'Data/birds/CUB_200_2011/images.txt'
splitpath = 'Data/birds/CUB_200_2011/train_test_split.txt'

df_filenames = pd.read_csv(namepath, delim_whitespace=True, header=None)
filenames = df_filenames[1].tolist()

df_splitflag = pd.read_csv(splitpath, delim_whitespace=True, header=None)
splitflag = df_splitflag[1].tolist()

train = []
test = []

for i in range(0,len(filenames)):
    if splitflag[i] == 1:
       train.append(filenames[i])
    else:
       test.append(filenames[i])

with open('Data/birds/train/filenames.pickle','wb') as f:
     pickle.dump(train,f)

with open('Data/birds/test/filenames.pickle','wb') as f:
     pickle.dump(test,f)


