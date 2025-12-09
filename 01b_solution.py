# given dial starts at 50
# given input as .txt with each line having one value
# values start with R or L then an integer
# R = positive
# L = negative
# can only go 1 digit at a time
# actual password is the number of times the current_value is 0
# the counter is modulo 100, so if it goes above 100, it wraps around to 0

# solution:
import os

# keep a running count 
num_zeroes = 0
# keep a running sum 
current_value = 50

# read each line into an array[str]
with open("01_input.txt", "r") as f:
	code = f.readlines()
array = [line.strip() for line in code]



# loop over the array
# areas for improvement: avoid nested loops, makes it O(n^2)
for i in array:
    if i[0] == 'R':
        while int(i[1:]) > 0:
            current_value += 1
            i = i[0] + str(int(i[1:]) - 1)
            # print(f"current value: {current_value}\n")
            if (current_value % 100) == 0:
                num_zeroes += 1
    elif i[0] == 'L':
        while int(i[1:]) > 0:
            current_value -= 1
            i = i[0] + str(int(i[1:]) - 1)
            # print(f"current value: {current_value}\n")
            if (current_value % 100) == 0:
                num_zeroes += 1
    else:
        continue
print(f"encountered {num_zeroes} zeroes")