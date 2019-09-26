import numpy as np
import pandas as pd
from keras import metrics
from keras.layers import Input, Dense, Lambda, Layer, Embedding, LSTM, Reshape, GRU
from keras.models import Model, load_model
from keras import backend as K
from keras.callbacks import EarlyStopping, CSVLogger, ModelCheckpoint, TensorBoard
import subfunc_1 as subs
from scipy.stats import norm
import csv
# select data

smile_train = pd.read_csv('./DataPool/select data/smile_train_with_161162.csv', index_col=None, header=None).values
smile_test = pd.read_csv('./DataPool/select data/smile_test_with_161162.csv', index_col=None, header=None).values

target_texts = smile_train[:, 1:51]
ytest = smile_test[:, 1:51]


smile_predict = pd.read_csv('generates_smiles_noise_v3-2.csv', index_col=None, header=None).values[:, :50]
correct_compound = 0
number = []
for i in range(1097):
    if all(target_texts[i, :] == smile_predict[i, :]) :
        correct_compound += 1
    else:
        number.append(i)

print('完全正確的分子:', correct_compound, '正確率(除1097):', correct_compound/1097)
print('錯誤的分子編號', number)

a = 0
for i in range(1097):
    for j in range(50):
        if target_texts[i, j] == smile_predict[i, j] :
            a += 1
print('答對幾格:', a , '總共幾格:', 1097*50, '格數正確率: ', a/(1097*50))
print('--------------------------------------')
smile_predict_test = pd.read_csv('generates_smiles_noise_testing_v3-2.csv', index_col=None, header=None).values[:, :50]
compound_test = 0
number_t = []
for i in range(275):
    if all(ytest[i, :] == smile_predict_test[i, :]) :
        compound_test += 1
    else:
        number_t.append(i)

print('完全正確的分子:', compound_test, '正確率(除275):', compound_test/275)
print('錯誤的分子編號', number_t)
b = 0
for i in range(275):
    for j in range(50):
        if ytest[i, j] == smile_predict_test[i, j] :
            b += 1

print('答對幾格:', b , '總共幾格:', 275*50, '格數正確率: ', b/(275*50))
