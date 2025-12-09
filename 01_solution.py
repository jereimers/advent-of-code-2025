# given dial starts at 50
# given input as .txt with each line having one value
# values start with R or L then an integer
# R = positive
# L = negative
# actual password is the number of times the sum == 0
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
for i in array:
	if i[0] == 'R':
		current_value += int(i[1:])
		print(f"current value: {current_value}\n")
	elif i[0] == 'L':
		current_value -= int(i[1:])
		print(f"current value: {current_value}\n")
	else:
		continue
	if (current_value % 100) == 0:
		num_zeroes += 1
		print(f"current_value is zero,\n num_zeroes: {num_zeroes}\n")
print(f"encountered {num_zeroes} zeroes")