# Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.
# 
# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.
# 
# Consider again the example from before:
# 
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# Now, the joltages are much larger:
# 
# In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
# In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
# In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
# In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
# The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.
# 
# What is the new total output joltage?

# Time to generalize...

def find_largest_joltage(bank, num_batteries):
    print(f"Finding largest {num_batteries}-digit combo in bank of length {len(bank)}: {"".join(bank)}")
    batteries = []
    joltage_string = []
    start_pos = 0 # where we start searching in the bank

    while len(joltage_string) < num_batteries:
        # declare which battery we're looking for
        remaining_needed = num_batteries - len(joltage_string) # remaining_needed = 12 on first run
        print(f"Finding digit {len(joltage_string)}. Remaining digits needed: {remaining_needed}.")

        # If there aren't enough available batteries remaining in the input, take the entire substring
        if start_pos + remaining_needed > len(bank):
            joltage_string.append(bank[start_pos:])
            return

        # Latest index we can pick the current_batt's joltage from
        end_pos = len(bank) - remaining_needed # end_pos = 100 - 12 = 88 on first run. We can take element 88
        try:
            print(f"Battery {len(joltage_string)} can be selected from indices {start_pos} ({bank[start_pos]}) to {end_pos} ({bank[end_pos]}).")
        except IndexError:
            break


        # Find the max digit in that valid range
        max_digit = bank[start_pos]
        max_index = start_pos
        print(f"Initializing max_digit = {max_digit} and max_index = {start_pos}")

        for j in range(start_pos, end_pos):
            if bank[j] > max_digit:
                max_digit = bank[j]
                max_index = j
                print(f"Found candidate for battery {len(joltage_string)}: {max_digit} at bank index {max_index}")
        
        # Add to result and move past it
        print(f"Found next max joltage ({max_digit}) at bank index {max_index}")
        joltage_string.append(max_digit)
        batteries.append(max_index)
        print(f"Current joltage: {"".join(joltage_string)}")
        start_pos = max_index + 1
        print(f"Resuming search at new start_pos: {start_pos}")

    return int("".join(joltage_string))


if __name__ == '__main__':

    total_joltage = 0
    # load input data with file I/O into comma-separated list
    with open('03_input.txt', 'r') as f:
        data = f.read().strip()

    array = data.split('\n')

    # print(f"Input: \narray")

    # test_bank = list(str(array[1]))
    # test_joltage = find_largest_joltage(test_bank, 12)
    # print(test_joltage)

    # process each bank
    for idx, bank in enumerate(array):
        print(f"Processing Bank #{idx}: {bank}")
        bank_joltage = find_largest_joltage(bank, num_batteries=12)
        print(f"Bank #{idx} joltage: {bank_joltage}")
        total_joltage += bank_joltage

    print(f"Total joltage: {total_joltage }")



