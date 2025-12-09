# %%
import os

# load input data with file I/O into comma-separated list
with open('02_input.txt', 'r') as f:
    data = f.read().strip()

array = data.split(',')

print(array)

# %%
# initialize variables
invalid_IDs = [] # running collection of integers

# %%
# sort list by element_length to get small ranges on the left and large ranges on the right
array.sort(key=len)
print(array)

# %%
# now we gotta split each element of the array into two different values. 
# does a list of lists suffice? Or would a list of tuples be more useful? Or something else?
ranges = [[str(lo), str(hi)] for lo, hi in (item.split('-') for item in array)]
print(ranges)

# %% [markdown]
# # Logic for detecting invalid_IDs
# 
# - First off, I don't think I actually need to expand `[ranges]` into `[IDs]`
# - Let's work at the range scale using the logic I thought out.
# - 
# - think of this like building search candidates. 
# - for the set of numbers between `lo` and `hi`, get the set of possible invalid_IDs.
# 
# ## first filter
# Skip 1-digit IDs (valid by default)
# 

# %%
for item in ranges:
    if int(item[0]) < 10:
        item[0] = '10'

# %%
# this finds numbers containing any number of repeated groups

import re

invalid_IDs = []
for item in ranges:
    for num in range(int(item[0]), int(item[1]) + 1):
        s = str(num)
        max_chunk_size = len(s) // 2
        for size in range(1, max_chunk_size + 1):
            if len(s) % size != 0:
                continue
            pattern = r'^(\d{' + str(size) + r'})' + r'(\1){' + str(len(s) // size - 1) + r'}$'
            if re.match(pattern, s):
                invalid_IDs.append(num)

print(set(invalid_IDs))

# %%
# the challenge asks to find only numbers with TWO repeated groups

# import re

# invalid_IDs = []
# for item in ranges:
#     for num in range(int(item[0]), int(item[1]) + 1):
#         s = str(num)
#         if len(s) % 2 != 0:
#             continue
#         chunk_size = len(s) // 2
#         pattern = r'^(\d{' + str(chunk_size) + r'})\1$'
#         if re.match(pattern, s):
#             invalid_IDs.append(num)

# print(set(invalid_IDs))

# %%
answer = 0
# dedup by converting to set then back to list
invalid_IDs = list(set(invalid_IDs))
print(len(invalid_IDs))
for id in invalid_IDs:
    answer += int(id)

print(answer)


