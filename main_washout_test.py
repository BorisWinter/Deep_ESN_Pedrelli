'''
This is an example of the application of DeepESN model for next-step prediction on Mackey Glass time-series. 

Reference paper for DeepESN model:
C. Gallicchio, A. Micheli, L. Pedrelli, "Deep Reservoir Computing: A Critical Experimental Analysis", 
Neurocomputing, 2017, vol. 268, pp. 87-99

Reference paper for the design of DeepESN model in multivariate time-series prediction tasks:
C. Gallicchio, A. Micheli, L. Pedrelli, "Design of deep echo state networks",
Neural Networks, 2018, vol. 108, pp. 33-47 
    
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

'''
EDIT: This file serves as an experimental setup to emperically determine roughly when the initial state of the 
ESN has been washed out, thus helping us determine the correct washout time. 
'''

import numpy as np
import random
from DeepESN import DeepESN
from utils import MSE, config_MG, load_MG, config_chest, load_chest, config_washout_test, load_washout_test, select_indexes
import matplotlib.pyplot as plt
class Struct(object): pass

# sistemare indici per IP in config_pianomidi, mettere da un'altra parte
# sistema selezione indici con transiente messi all'interno della rete
def main():
    
    # fix a seed for the reproducibility of results
    np.random.seed(7)
   
    # dataset path 
    path = 'datasets'
    dataset, Nu, error_function, optimization_problem, TR_indexes, VL_indexes, TS_indexes = load_washout_test(path, MSE)

    # load configuration for pianomidi task
    configs = config_washout_test(list(TR_indexes) + list(VL_indexes))
    
    # Be careful with memory usage
    Nr = 100 # number of recurrent units
    Nl = 5 # number of recurrent layers
    reg = 0.0;
    transient = 100
    
    deepESN = DeepESN(Nu, Nr, Nl, configs)
    states = deepESN.computeState(dataset.inputs, deepESN.IPconf.DeepIP)
    
    # train_states = select_indexes(states, list(TR_indexes) + list(VL_indexes), transient)
    # train_targets = select_indexes(dataset.targets, list(TR_indexes) + list(VL_indexes), transient)
    # test_states = select_indexes(states, TS_indexes)
    # test_targets = select_indexes(dataset.targets, TS_indexes)
    
    # deepESN.trainReadout(train_states, train_targets, reg)
    
    # train_outputs = deepESN.computeOutput(train_states)
    # train_error = error_function(train_outputs, train_targets)
    # print('Training ACC: ', np.mean(train_error), '\n')
    
    # test_outputs = deepESN.computeOutput(test_states)
    # test_error = error_function(test_outputs, test_targets)
    # print('Test ACC: ', np.mean(test_error), '\n')
 

    # The interesting output would be some notion of how much a neuron's activation is changing after time
    # Therefore, since we have constant inputs, we can take the average difference over all neurons per timestep
    # and plot
    differences = np.zeros(states[0].shape)
    print(states[0].shape)
    for t in range(len(states[0].T) - 1):
        for idx, value in enumerate(states[0].T[t, :]): # iterate over all values
            differences[idx][t] = abs(states[0].T[t + 1, idx] - value)

    #now plot averages over all neurons:
    plt.plot(np.mean(differences, axis = 0)[:50])
    plt.show()
 
if __name__ == "__main__":
    main()
    
