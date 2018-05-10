# Onemax
Python implementation of a generational evolutionary algorithm for the Onemax problem.

The Onemax problem involves evolving a string of bits from a random initialisation of zeros and ones to all ones, and could be considered a simple introductory problem for evolutionary computing. This implementation is a generational genetic algorithm.

This repository comprises the following python files:

individual.py - a class representing an individual bitstring;
onemax.py - the implementation of the generationl evolutionary algorithm; and
onemax_batch.py - a file to read the results output of onemax.py for multiple runs, and then calculate the mean results based on multiple runs of the algorithm, to be suitable for easy plotting with gnuplot (or any other plotting software). 

The repository also contains a gnuplot script for plotting the fitness curves acheived over multiple runs, onemax_batch_results.plot.

Firstly, run onemax.py to execute the algorithm over multiple runs. Then, secondly, run onemax_batch.py to read the results and then calculate the mean results of multiple runs. The resulting out put file can then be used with onemax_batch_results.plot to give a nice plot of the fitness curves for worst, average, and best fitness values in the population. 

It's important to set the parameter 'num_gen' (the number of generations in a single run of the algorithm) to be the same value in both onemax.py and onemax_batch.py. 
