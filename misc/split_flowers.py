import os
import pickle
import pandas as pd
import random

filepath = 'Data/flowers/jpg'
filenames = os.listdir(filepath)

random.seed(1)

random.shuffle(filenames)
train_index = int(len(filenames)/2) + 100

train = filenames[0:train_index]
test = filenames[train_index:]


with open('Data/flowers/train/filenames.pickle','wb') as f:
     pickle.dump(train,f)

with open('Data/flowers/test/filenames.pickle','wb') as f:
     pickle.dump(test,f)

