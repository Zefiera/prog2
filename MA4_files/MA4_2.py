#!/usr/bin/env python3

from person import Person
from time import perf_counter
from numba import njit
import matplotlib.pyplot as pl

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
	pl.subplot(211)
	pl.legend()
	line1,=pl.plot(n,time_py,'ro', label='Python')
	line2,=pl.plot(n,time_nu,'bo',label='Numba')
	pl.legend(handles=[line1,line2])
	pl.xlabel("n [-]")
	pl.ylabel("Time [s]")
	pl.title("Python vs. Numba vs. C++")

	n=[x for x in range(30,46)]
	time_py,time_nu,time_c=[],[],[]
	persons=[Person(x) for x in n]
	for ind, i in enumerate(n):
		s=perf_counter()
		fib_py(i)
		e=perf_counter()
		time_py.append(e-s)
		s=perf_counter()
		fib_numba(i)
		e=perf_counter()
		time_nu.append(e-s)
		s=perf_counter()
		persons[ind].fib()
		e=perf_counter()
		time_c.append(e-s)
	pl.plot(n,time_py,'ro',n,time_nu,'bo',n,time_c,'co')
	pl.subplot(212)
	line1,=pl.plot(n,time_py,'ro', label='Python')
	line2,=pl.plot(n,time_nu,'bo',label='Numba')
	line3,=pl.plot(n,time_c,'go',label='C++')
	pl.legend(handles=[line1,line2,line3])
	pl.xlabel("n [-]")
	pl.ylabel("Time [s]")
	pl.savefig("pynuc.png")
	
	f=Person(47)
	start=perf_counter()
	print(f.fib())
	end=perf_counter()
	print(f'f.fib(47): {end-start}')
	start=perf_counter()
	print(fib_numba(47))
	end=perf_counter()
	print(f'fib_numba(47): {end-start}')

if __name__ == '__main__':
	main()
