#	File:	onemax_batch.py
#	Date:	6 May 2018
#	Author: Chris Simons
#
#	Use with onemax.py to process results of multiple runs
#	
#	Important - set the number of generations and runs
#	to be the same as that set in onemax.py

num_gen = 25
num_runs = 25

#	-----------------------------------------------------------------
#	read the results from 'onemax_results.dat'
#	-----------------------------------------------------------------

results_file = open( 'onemax_results.dat', mode = 'r', encoding = 'utf-8' )

myList = [ ]
worst = [ ] 
average = [ ] 
best = [ ]

for line in results_file:
	myList.append( line )
	numbers = line.split( ' ' )
	worst.append( int( numbers[ 1 ] ) )
	average.append( int( numbers[ 2 ] ) )
	best.append( int( numbers[ 3 ] ) )

#	for debug of reading results file
#
#	print( myList )
#	print( '\n worst is: ' )
#	print( worst )
#	print( '\n average is: ' )
#	print( average )
#	print( '\n best is : ' )
#	print( best )

#	-----------------------------------------------------------------
#	calculate the generational values for each run
#	-----------------------------------------------------------------

worst_sum = 0 
average_sum = 0 
best_sum = 0

value = 0 
run = 0
num_values = num_gen * num_runs
generation = 0

generational_worst_list = [ ]
generational_average_list = [ ]
generational_best_list = [ ]

for generation in range( num_gen):
	generational_worst_list.append( 0 )
	generational_average_list.append( 0 )
	generational_best_list.append( 0 )
	
#	for debug
#	print( '\n generational worst list before is: ' )
#	print( generational_worst_list )

generation = 0

while run < num_runs:
#	print( '\tin run number {0}: '.format( run ) )
	counter = run * num_gen
#	print( '\t\tcounter is: {0}'.format( counter ) )
	generation = 0
	while generation < num_gen:
		temp = worst[ generation + counter ]
		worst_sum += temp;	
		generational_worst_list[ generation ] += temp;
		temp = average[ generation + counter ]
		average_sum += temp;	
		generational_average_list[ generation ] += temp;	
		temp = best[ generation + counter ]
		best_sum += temp;	
		generational_best_list[ generation ] += temp;					
		generation += 1
	run += 1

#	for debug	
#	print( '\n generational worst list after is: ' )
#	print( generational_worst_list )	
#	print( '\n generational average list after is: ' )
#	print( generational_average_list )
#	print( '\n generational best list after is: ' )
#	print( generational_best_list )	 
#	print( '\n\n worst sum is: ' )
#	print( worst_sum)
#	print( '\n average sum is: ' )
#	print( average_sum )
#	print( '\n best list is: ' )
#	print( best_sum )

#	-----------------------------------------------------------------
#	set up a text file and write average generational results
#	-----------------------------------------------------------------

generation = 0
average_generational_worst = 0.0
average_generational_average = 0.0
average_generational_best = 0.0

a_file = open( 'onemax_batch_results.dat', mode = 'a', encoding = 'utf-8' )

for generation in range( num_gen):
	average_generational_worst = generational_worst_list[ generation ] / num_runs
	print( 'average worst for generation {0} is: {1}'.format( generation, average_generational_worst ) )
	
	average_generational_average = generational_average_list[ generation ] / num_runs
	print( 'average average for generation {0} is: {1}'.format( generation, average_generational_average ) )
	
	average_generational_best = generational_best_list[ generation ] / num_runs
	print( 'average best for generation {0} is: {1}'.format( generation, average_generational_best ) )
	print( '\n' )

	a_file.write( '{0} {1:.2f} {2:.2f} {3:.2f} \n'.format( generation, average_generational_worst, average_generational_average, average_generational_best ) )
	