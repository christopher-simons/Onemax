#	File: 	onemax.py
#	Date:	15 April 2018
#	Author: Chris Simons
#
#	OneMax - the ”hello world” of evolutionary computing?
#
#	The OneMax problem consists of maximising the number of ones in a bitstring.
#	e.g. see http://tracer.lcc.uma.es/problems/onemax/onemax.html
#
#	here's the pseudocode for the evolutionary algorithm used in this program,
#	taken from "An Introduction to Evolutionary Computing", 2nd Ed., Eiben and Smith.  
#
#		initialise population at random
#		evaluate each individual
#		while( not done )
#  			select parents
#			recombine pairs of parents
#			mutate new candidate individuals
#			evaluate each individual
#			select candidates for next generation
#		end while
#
#	As the population evolves, fitness values are written to 'results.dat'
#
#	Each bitstring in the population is represented by the "Individual" class. 

from individual import Individual
import _random

#	algorithm parameters	
genotype_size = 100
num_gen = 20
pop_size = 100
xover_rate = 0.75

#	-----------------------------------------------------------------

def show_average_population_fitness( population ):
	sum = 0
	for ind in population:
#		ind.calc_fitness( )
		sum += ind.fitness
	print( '\taverage population fitness is: {0}'.format( sum / pop_size ) )
  
  
#	-----------------------------------------------------------------

def select_parents( population, mating_pool ):
	n = 0
	while n < pop_size:
		rand = _random.Random( ) 
		number1 = rand.random( )
		number1 = number1 * pop_size
		index1 = int( number1 )
		number2 = rand.random( )
		number2 = number2 * pop_size
		index2 = int( number2 )
#		print( 'index1 is: {0} and index2 is: {1}'.format( index1, index2 ) )
		if population[ index1 ].fitness > population[ index2 ].fitness:
			mating_pool.append( population[ index1 ] )	
		else:
			mating_pool.append( population[ index2 ] )		
		n += 1
#	print( 'size of mating pool is: {0}'.format( n ) )
#	n = 0
#	while n < pop_size:
#		print( mating_pool[ n ].fitness )
#		n += 1


#	-----------------------------------------------------------------

def recombine( mating_pool ):
	xover_number = int( pop_size * xover_rate ) 
#	cross over number must always be an even number
	if xover_number % 2 == 1:
		 xover_number -= 1
#	print( 'xover_number is {0}'.format( xover_number ) )

	rand = _random.Random( )
	temp = rand.random( )
#	xover_point = int( temp * genotype_size )
	xover_point = int( 0.5 * genotype_size )
#	print( 'xover_point is {0}'.format( xover_point ) )

#	because cross over involves two parents...
	n = 0
	loop_counter = 0
	loop_counter = xover_number / 2
#	print( 'xover loop counter is {0}'.format( loop_counter ) )
	
	i = 0
	ints = [ ]
	while i < genotype_size:
		ints.append( i )
		i += 1
		
#	print( ints )
	
	while n < loop_counter: 	
		number1 = rand.random( )
		length1 = len( ints )
#		print( 'BEFORE: length of ints is: {0}'.format( length1 ) )
		number1 = number1 * len( ints )
		temp1 = int( number1 )
#		print( 'BEFORE: temp1 is: {0}'.format( temp1 ) )
		index1 = ints[ temp1 ]
#		ints.remove( temp1 ) remove by value!
		del ints[ temp1 ]
		
		number2 = rand.random( )
		length2 = len( ints )
#		print( 'BEFORE: length of ints is: {0}'.format( length2 ) )
		number2 = number2 * len( ints )
		temp2 = int( number2 )
#		print( 'BEFORE: temp2 is: {0}'.format( temp2 ) )
		index2 = ints[ temp2 ]
#		ints.remove( temp2 ) remove by value!
		del ints[ temp2 ] 	
		
#		print( 'BEFORE: index1 is: {0} and index2 is: {1}'.format( index1, index2 ) )
		ind1 = mating_pool[ index1 ]
		ind2 = mating_pool[ index2 ]
		
#		print( 'BEFORE: ind1 is: {0} and ind2 is: {1}'.format( ind1.barr, ind2.barr ) )
		
#		print( 'BEFORE: ints is: {0}'.format( ints ) )
		
		i = xover_point
		barr1 = bytearray( )
		barr2 = bytearray( )

		while i < genotype_size:
			barr1.append( ind1.barr[ i ] )
			barr2.append( ind2.barr[ i ] ) 
#			print( 'barr1 is: {0} and barr2 is: {1}'.format( barr1, barr2 ) )
			i += 1
		
#		print( 'BEFORE: barr1 is: {0} and barr2 is: {1}'.format( barr1, barr2 ) )
		
		i = 0
		while i < xover_point: 
			ind1.barr.pop( )
			ind2.barr.pop( )
			i += 1

#		print( 'BEFORE: cropped ind1 is: {0} and ind2 is: {1} and i is: {2}'.format( ind1.barr, ind2.barr, i ) )

		i = xover_point
		barr_counter = 0
		while i < genotype_size:
			ind1.barr.append( barr2[ barr_counter ] )
			ind2.barr.append( barr1[ barr_counter ] )
			i += 1
			barr_counter += 1

#		print( 'AFTER: ind1 is: {0} and ind2 is: {1}'.format( ind1.barr, ind2.barr ) )
#		print( 'AFTER: ints is: {0}'.format( ints ) )
		
		n += 1  

#	-----------------------------------------------------------------

def mutate( mating_pool ):
	rand = _random.Random( ) 
	number1 = rand.random( )
	number1 = number1 * pop_size
	index1 = int( number1 )
	mating_pool[ index1 ].mutate( )

#	-----------------------------------------------------------------

def evaluate( mating_pool ):
	n = 0
	while n < pop_size:
		mating_pool[ n ].calc_fitness( )
		n += 1
#	show_average_population_fitness( mating_pool )

#	-----------------------------------------------------------------

def select_candidates_for_next_generation( population, mating_pool ):
	i = 0;
	while i < pop_size:
		population.pop( )
		i += 1
	i = 0
	while i < pop_size:
		population.append( mating_pool[ i ] )
		i += 1
	i = 0	
	while i < pop_size:
		mating_pool.pop( )
		i += 1
	i = 0
#	while i < pop_size:
#		print( population[ i ].fitness )
#		i += 1
#	show_average_population_fitness( population )

#	-----------------------------------------------------------------

def write_generation_results_to_file( a_file, n, population ):
	i = 0
	best = 0
	worst = genotype_size
	sum = 0
	average = 0.0
	ave = 0
	while i < pop_size:
		if population[ i ].fitness > best:
			best = population[ i ].fitness
		if population[ i ].fitness < worst:
			worst = population[ i ].fitness
		sum += population[ i ].fitness	
		i += 1
	
	average = sum / pop_size
	ave = int( average )
	
	a_file.write( '{0} {1} {2} {3} \n'.format( n, worst, ave, best ) )

#	-----------------------------------------------------------------
#	evolution begins here by initialising population at random
#	-----------------------------------------------------------------

population = [ ]
mating_pool = [ ] 

n = 0
while n < pop_size:
	ind = Individual( genotype_size )  
	population.append( ind )
	n += 1

#	firstly evaluate each individual
print( '\n' )
print( 'population initialised' )
evaluate( population )
show_average_population_fitness( population )

#	set up a text file to record results
a_file = open( 'onemax_results.dat', mode = 'a', encoding = 'utf-8' )

#	the generational loop 
n = 1
while n <= num_gen:
	print( '\tgeneration number: {0}'.format( n ) )
	select_parents( population, mating_pool )
	recombine( mating_pool )
	mutate( mating_pool )
	evaluate( mating_pool )
	select_candidates_for_next_generation( population, mating_pool )	
	show_average_population_fitness( population )
	write_generation_results_to_file( a_file, n, population )
	n += 1

#	lastly, show the final population
n = 0
while n < pop_size:
	print( population[ n ].barr )
	n += 1