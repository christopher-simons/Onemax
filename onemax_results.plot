# 	File:	onemax_results.plot
# 	Date: 	13 April 2018
#	Author: Chris Simons

set title "Evolution of the bitstrings in OneMax Problem"

set key top left

set ylabel 'fitness'
set xlabel 'generations'

set xrange [1 to 20]
set yrange [0 to 105]

plot	"onemax_results.dat" using 1:2 with linespoints title 'worst', \
		"onemax_results.dat" using 1:3 with linespoints title 'average', \
		"onemax_results.dat" using 1:4 with linespoints title 'best'
