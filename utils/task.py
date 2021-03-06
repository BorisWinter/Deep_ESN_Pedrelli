'''
Task configuration file

----

This file is a part of the DeepESN Python Library (DeepESNpy)

Luca Pedrelli
luca.pedrelli@di.unipi.it
lucapedrelli@gmail.com

Department of Computer Science - University of Pisa (Italy)
Computational Intelligence & Machine Learning (CIML) Group
http://www.di.unipi.it/groups/ciml/

----
'''

import functools
import os
from scipy.io import loadmat
import numpy as np
import pandas as pd

class Struct(object): pass

def select_indexes(data, indexes, transient=0):

    if len(data) == 1:
        return [data[0][:,indexes][:,transient:]]

    return [data[i][:,transient:] for i in indexes]

def load_pianomidi(path, metric_function):

    data = loadmat(os.path.join(path, 'pianomidi.mat')) # load dataset

    dataset = Struct()
    dataset.name = data['dataset'][0][0][0][0]
    dataset.inputs = data['dataset'][0][0][1][0].tolist()
    dataset.targets = data['dataset'][0][0][2][0].tolist()

    # input dimension
    Nu = dataset.inputs[0].shape[0]

    # function used for model evaluation
    error_function = functools.partial(metric_function, 0.5)

    # select the model that achieves the maximum accuracy on validation set
    optimization_problem = np.argmax


    TR_indexes = range(87) # indexes for training, validation and test set in Piano-midi.de task
    VL_indexes = range(87,99)
    TS_indexes = range(99,124)

    return dataset, Nu, error_function, optimization_problem, TR_indexes, VL_indexes, TS_indexes

def load_MG(path):

    data = loadmat(os.path.join(path, 'MG.mat')) # load dataset

    dataset = Struct()
    dataset.name = data['dataset'][0][0][0][0]
    dataset.inputs = data['dataset'][0][0][1][0]
    dataset.targets = data['dataset'][0][0][2][0]

    print(dataset.inputs)
    # print("length = ", len(dataset.inputs[0][0]))

    # input dimension
    Nu = dataset.inputs[0].shape[0]

    # function used for model evaluation
    # error_function = metric_function

    # select the model that achieves the maximum accuracy on validation set
    # optimization_problem = np.argmin


    TR_indexes = range(7000) # indexes for training, validation and test set in Piano-midi.de task
    VL_indexes = range(7000,8000)
    TS_indexes = range(8000,9999)

    return dataset, Nu, TR_indexes, VL_indexes, TS_indexes
    # return dataset, Nu, error_function, optimization_problem, TR_indexes, VL_indexes, TS_indexes


'''
Function for loading the chest data
'''
def load_chest(path, data_size=None, sampling_rate=None):

    # data = loadmat(os.path.join(path, 'MG.mat')) # load dataset
    data = pd.read_csv(os.path.join(path, 'subject2_baseline_train.csv'))
    if sampling_rate is not None:
        data = data[::sampling_rate] #sampling to increase timestep length

    if data_size is not None:
        data = data[:data_size] #shorten for lower computational demand



    dataset = Struct()
    dataset.name = 'Chest'
    dataset.inputs = [np.array([data['Chest_ECG'][:-1]])]
    dataset.targets = [np.array([data['Chest_ECG'][1:]])]

    # print(dataset.inputs)
    input_length = len(dataset.inputs[0][0])
    print("input length = ", input_length)
    # print("target length = ", len(dataset.targets))

    # input dimension
    Nu = dataset.inputs[0].shape[0]
    # print("Nu = ", Nu)

    TR_indexes = range(int(.7*input_length)) # indexes for training, validation and test set in Piano-midi.de task
    VL_indexes = range(int(.7*input_length), int(.8*input_length))
    TS_indexes = range(int(.8*input_length), int(input_length-1))

    print(".7 = ", int(.7*input_length))
    print(".8 = ", int(.8*input_length))
    print("-1 = ", int(input_length - 1))

    print("Done loading data")
    return dataset, Nu, TR_indexes, VL_indexes, TS_indexes


def load_chest_full(path):

    # data = loadmat(os.path.join(path, 'MG.mat')) # load dataset
    data1 = pd.read_csv(os.path.join(path, 'subject2_baseline_train.csv'))
    data2 = pd.read_csv(os.path.join(path, 'subject2_baseline_test.csv'))
    data = data1.append(data2)
    data = data[20000:]#delete first 20k rows, as they have been used for the parameter sweep.
    # data = data[:80000]  #optionally shorten dataset

    dataset = Struct()
    dataset.name = 'Chest'
    dataset.inputs = [np.array([data['Chest_ECG'][:-1]])]
    dataset.targets = [np.array([data['Chest_ECG'][1:]])]

    # print(dataset.inputs)
    input_length = len(dataset.inputs[0][0])
    print("input length = ", input_length)
    # print("target length = ", len(dataset.targets))

    # input dimension
    Nu = dataset.inputs[0].shape[0]
    # print("Nu = ", Nu)

    TR_indexes = range(int(.7*input_length)) # indexes for training, validation and test set in task
    VL_indexes = range(int(.7*input_length), int(.8*input_length))
    TS_indexes = range(int(.8*input_length), int(input_length-1))

    print(".7 = ", int(.7*input_length))
    print(".8 = ", int(.8*input_length))
    print("-1 = ", int(input_length - 1))

    print("Done loading data")
    return dataset, Nu, TR_indexes, VL_indexes, TS_indexes
