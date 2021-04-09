# Deep_ESN_Pedrelli

This repository contains an implementation of the DeepESN model described in the following paper:

C. Gallicchio, A. Micheli, L. Pedrelli, "Deep Reservoir Computing: A Critical Experimental Analysis",
Neurocomputing, 2017, vol. 268, pp. 87-99

It uses files from the following DeepESNpy Pyhon Library by Luca Pedrelli, altered to work with the data in this experiment.
https://github.com/lucapedrelli/DeepESN

## Dataset
The dataset for this study is available here: https://archive.ics.uci.edu/ml/datasets/WESAD+%28Wearable+Stress+and+Affect+Detection%29

Alternatively, small example sets have been provided in the datasets folder.

## Running the experiments
The following experiments can be run with the following files:

-`sweep.ipynb` to run the parameter sweeps
-`single_model_full_traning.ipynb` to train one model on a bigger dataset

