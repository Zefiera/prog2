#!/usr/bin/env python3

from person import Person
from time import perf_counter
from numba import njit
import matplotlib
matplotlib.use("Agg")
import pylab as pl

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

def main():
	time_py=[]
	time_nu=[]
	n=[x for x in range(20,31)]
	for i in n:
		start=perf_counter()
		fib_py(i)
		end=perf_counter()
		time_py.append(end-start)
		start=perf_counter()
		fib_numba(i)
		end=perf_counter()
		time_nu.append(end-start)
	pl.plot(n,time_py,'ro',n,time_nu,'bo')
	pl.xlabel("n [-]")
	pl.ylabel("Time [s]")
	pl.title("Python vs. Numba")
	pl.savefig("test.png")

	f=Person(1)
	start=perf_counter()
	fib_py(1)
	end=perf_counter()
	print(end-start)
	start=perf_counter()
	f.fib()
	end=perf_counter()
	print(f'f.fib(): {end-start}')

if __name__ == '__main__':
	main()
