# given input: unsorted list of string literals.
#              where each element is a range of integers (e.g. "35-112").
#              numbers are arbitrary size, and ranges can be overlapping.
#              range is inclusive of both bounds.

# challenge:   scan through all in-range integers to detect those with repeating decimal groups.
#              any number with repeating decimal groups is an "invalid ID"
#              answer is the sum of all invalid IDs

# examples:    998-1012 has one invalid ID, 1010
#              102102 is invalid, as is 121212, as is 111111

# variables & conventions:
#   - var ID: the number being checked for validity
#   - var chunk: the integer subgroup being checked for repetition
#   - var lo_bound, hi_bound: the lower and upper bounds of the range to scan
#   - list invalid_IDs: the running collection of invalid_IDs

# things I notice: repeating group can only be as long as half the parent number
#                   e.g., scanning the range 23459876-23469875 should only require scanning for repeating groups of size 1, 2, and 4
#                  not 3, because all numbers in the range are 8 digits, and a repeating 3-some wouldn't fit.

#     ---------->  so invalid_IDs must be comprised of chunks such that ID_length % chunk_length == 0   <----------
#                   AKA, we can discount/avoid checking chunks where ID_length % chunk_length != 0

#                   we could also discount 1 and 2 here, but not because of the length ratios.
#                  in the example range, only the last 5 digits vary between lo_bound and hi_bound. (How do we detect this?)
#                       hi_bound - lo_bound = range
#                       range_length (the number of digits in range) gives us a mask we can apply to ID
#                  I digress. In this example, the non-varying digits are "234*****". "234" is not a 1-chunk, and we already threw 3-chunks out,
#                  and 2-chunks are out as well, because "234" already violates the pattern required for any 2-chunk repeating pattern to exist in the larger ID.  
#                       (it would need to be "232*****" for us to include 2-chunks)
#                  so we're checking for 4-chunks only.
#                  which 4-chunks are even possible? 
#                   lo_bound = 23459876 ----> chunk_1 = 2345
#                       23452345 < lo_bound, so chunk_1 is out
#                   hi_bound = 23469875 ----> chunk_2 = 2346
#                       lo_bound < 23462346 < hi_bound, so chunk_2 is an invalid_ID ----> add it to invalid_IDs
#                  
#
#       ...? should I treat them as strings instead of integers? Then I could use python's substr() and other string functions
#       ...? will regex be the most useful tool/framework for this?

# steps:
#   1. load input data with file I/O into comma-separated list
#   2. sort list by element_length to get small ranges on the left and large ranges on the right
#   3. split each element (on "-") into [lo_bound, hi_bound]


