import sys
import time
import multiprocessing
import random

def merge_sort_multiple(results, array):
	results.append(merge_sort(array))

def merge_multiple(results, array_part_left, array_part_right):
	results.append(merge(array_part_left, array_part_right))

def merge_sort(array):
	length = len(array)
	if length <= 1:
		return array

	mid = int(length / 2)
	left_array = array[0 : mid]
	right_array = array[mid:]

	left_array = merge_sort(left_array)
	right_array = merge_sort(right_array)
	return merge(left_array, right_array)

def merge(left, right):
	sort = []
	left_array = left[:] # so changes don't affect original
	right_array = right[:]

	while len(left_array) > 0 or len(right_array) > 0:
		if len(left_array) > 0 and len(right_array) > 0:
			if left_array[0] <= right_array[0]:
				sort.append(left_array.pop())
			else:
				sort.append(right_array.pop())
		elif len(left_array) > 0:
			sort.append(left_array.pop())
		elif len(right_array) > 0:
			sort.append(right_array.pop())
	return sort

def pool_block(size): 
	pool = multiprocessing.Pool(size)
	yield pool # blocks until processes completed
	pool.close()
	pool.join()

def multi_merge_sort(array, p_count):
	chunk_size = int(length / p_count) # to divide array into chunks
	mgmt = multiprocessing.Manager() # for output of the processes
	res = mgmt.list()

	with pool_block(size=p_count) as pool:
		for i in range(p_count):
			if i < p_count - 1:
				chunk = array[i * chunk_size : (i + 1) * chunk_size]
			else: # all other elems
				chunk = array[i * chunk_size:]
			pool.apply_async(merge_sort_multiple, (res, chunk))

	while len(res) > 1:
		with pool_block(size=p_count) as pool:
			pool.apply_async( merge_multiple, (res, res.pop(0), res.pop(0)))

	return res[0]


if __name__ == '__main__':
	process_count = 4

	rand_len = random.randint(10, 60)
	rand_array = [random.randint(0, 100) for i in range(rand_len)]

	sorted_list = multi_merge_sort(rand_array, process_count)
	print "Sorted list: " + sorted_list