#	File: 	individual.py
#	Date: 	31 March 2018
#	Author:	Chris Simons
#
#	Class to encapsulate a bitstring used in a evolutionary algorithm
#	for the OneMax problem. 

import _random

class Individual:

	'''
		Individual - a class to represent an onemax individual.
		Representation is a byte array.
		In byte terms, 0 is 48 and 1 is 49
	'''

	def __init__( self, size ):
		self.barr = bytearray( )
		self.size = size
		self.fitness = 0
		n = 0
		while n < self.size:
			rand = _random.Random( ) 
			number = rand.random( )
			if number < 0.5:
				self.barr.append( 48 )
			else:
				self.barr.append( 49 )
			n += 1
#		for b in self.barr:
#			print( b )

	def calc_fitness( self ):
		score = 0
		counter = 0	
		while counter < self.size:
			if self.barr[ counter ] == 49:
				score += 1
			counter += 1
#			print( 'in calc_fitness, counter is: {0}, score is {1}'.format( counter, score ) )
		self.fitness = score
		return score
		
	def mutate( self ):
		index = 0
#		print( _random.__doc__)
		rand = _random.Random( ) 
		number = rand.random( )
#		print( 'generated random number is: {0}'.format( number ) )
		number2 = number * self.size
#		print( 'generated random number multiplied by size is: {0}'.format( number2 ) )
		index = int( number2 )
#		print( 'generated random index is: {0}'.format( index ) )
#		print( 'before mutation, byte array [ index ] is: {0}'.format( self.barr[ index ] ) )
		if self.barr[ index ] == 48:
#			print( 'in true branch' )
			self.barr[ index ] = 49
#			print( 'after mutation, byte array [ index ] is: {0}'.format( self.barr[ index ] ) )
		else:
#			print( 'in false branch' )
			self.barr[ index ] = 48
#			print( 'after mutation byte array [ index ] is: {0}'.format( self.barr[ index ] ) )
#		i = 0
#		while i < self.size:
#			print( 'byte is : {0}'.format( self.barr[ i ] ) )
#			i += 1


