from typing import List

def least_interval(tasks: List[str], n: int) -> int:
    task_dict = gen_hashmap(tasks)
    max_val = -1
    maxes = 0

    for key in task_dict:
        if task_dict[key] > max_val:
            max_val = task_dict[key]
            maxes = 1
        elif task_dict[key] == max_val:
            maxes += 1
    middles = (n - maxes + 1) * (max_val - 1)
    idles = max(0, middles - (len(tasks) - max_val * maxes))
    # if middles < 0:
    #     return len(tasks)
    return len(tasks) + idles

    # maxes = 2, max_val = 3, n = 3

    



    # 'a' 'b' 'c' 'idle' 'a' 'b' 'idle' 'idle' 'a' 'b'

# def least_interval(tasks: List[str], n: int) -> int:
#     task_dict = gen_hashmap(tasks)
#     non_zeroed = len(task_dict)
#     intervals = 0
#     schedule = []
#     while non_zeroed > 0:
#         added_this_round = 0
#         for key in task_dict:
#             if task_dict[key] > 0:
#                 task_dict[key] -= 1
#                 intervals += 1
#                 added_this_round += 1
#                 schedule.append(key)
#                 if task_dict[key] == 0:
#                     non_zeroed -= 1
#         idles = max(0, n - (added_this_round - 1))
#         if non_zeroed == 0:
#             idles = 0
#         elif ceil(added_this_round / 2) >= n:
#             credit += 1
#         intervals += idles
#         schedule.append(idles)
#         print(schedule, non_zeroed, intervals)
#     return intervals


    
def gen_hashmap(tasks):
    task_dict = {}
    for task in tasks:
        if task in task_dict:
            task_dict[task] = task_dict[task] + 1
        else:
            task_dict[task] = 1
    return task_dict
    
# debug your code below
print(least_interval(['A', 'A', 'B'], 2))
print(least_interval(['a', 'a', 'b', 'b', 'c', 'c', 'c'], 3))


# 'a' 'b' 'c' 'c' 'c'
 # step 1: hash map step ('a', 2) ('b', 2) ('c', 3)
 # step 2: base ('c', 3) ('b', 2) ('a', 2) n = 3, non-zeroed = 3, intervals = 0 []
 # step 3: ('c', 2) ('b', 1) ('a', 1) n = 3, non-zeroed = 3, intervals = 4 ['c', 'b', 'a', 'idle']
 # step 3: ('c', 1) ('b', 0) ('a', 0) n = 3, non-zeroed = 1, intervals = 8 ['c', 'b', 'a', 'idle', 'c', 'b', 'a', 'idle']
 # step 3: ('c', 0) ('b', 0) ('a', 0) n = 3, non-zeroed = 0, intervals = 9 ['c', 'b', 'a', 'idle', 'c', 'b', 'a', 'idle', 'c']


# 'a' 'b' 'c' 'd' 'e'
# 

# n = 4

'a' 'b' 'c' 'idle' 'idle' 'a' 'b' 'c' 'idle' 'idle' 'idle' 'idle' 'c'
'c' 'b' 'a' 'idle' 'idle' 'c' 'b' 'a' 'idle' 'idle' 'c'
