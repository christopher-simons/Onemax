# 	File:	onemax_batch_results.plot
# 	Date: 	3 May 2018
#	Author: Chris Simons

set title "OneMax Problem - multiple runs"

set key bottom right

set ylabel 'fitness'
set xlabel 'generations'

set xrange [1 to 20]
set yrange [20 to 105]

plot	"onemax_batch_results.dat" using 1:4 with linespoints title 'best', \
		"onemax_batch_results.dat" using 1:3 with linespoints title 'average', \
		"onemax_batch_results.dat" using 1:2 with linespoints title 'worst'
