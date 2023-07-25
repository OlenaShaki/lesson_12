def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result



tasks_count = 10000
param = [15]*tasks_count

import concurrent.futures
import time

def run_threads():
	with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
		executor.map(factorial, param)

def run_processes():
	executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
	executor.map(factorial, param)
	executor.shutdown()



if __name__ ==  '__main__':
	print(f'Execute threads for {tasks_count} tasks.')
	start = time.time()
	run_threads()
	threads_time = time.time() - start

	print(f'Execute processes for {tasks_count} tasks.')
	start = time.time()
	run_processes()
	processes_time = time.time() - start

	print(f'Threads run time: {round(threads_time, 2)} seconds.')
	print(f'Processes run time: {round(processes_time, 2)} seconds.')
	if (threads_time < processes_time):
		print(f'Threads is {round(processes_time / threads_time, 2)} times faster.')
	else:
		print(f'Processes is {round(threads_time / processes_time, 2)} times faster.')