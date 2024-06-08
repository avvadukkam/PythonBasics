from operator import length_hint
import time

test_list = [1, 4, 5, 7, 8]
print("The list is : ", test_list)

start_time_naive = time.time()
counter = 0
for i in test_list:
    counter += 1
end_time_naive = str(time.time() - start_time_naive)

start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)

start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)

print("Time taken using naive method is :", end_time_naive)
print("Time take using len() is : ", end_time_len)
print("Time taken using length_hint is : ", end_time_hint)
