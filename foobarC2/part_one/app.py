import time
import math
from input_data import input_list
import loop_solution
import recursive_solution

print(len(input_list))
print(math.log2(max(input_list)))
samples_num = 100

aggr = 0.0
for i in range(samples_num):
    nonrec_start = time.process_time()
    loop_solution.solution(30, input_list)
    nonrec_time = time.process_time() - nonrec_start
    aggr += nonrec_time
print ('avg_non_rec_time', aggr/samples_num)

aggr = 0.0
for i in range(samples_num):
    rec_start = time.process_time()
    recursive_solution.solution(30, input_list)
    rec_time = time.process_time() - rec_start
    aggr += rec_time
print ('avg_rec_time', aggr/samples_num)
