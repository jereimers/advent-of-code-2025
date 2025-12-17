# %%
import pandas as pd

with open('05_input.txt', 'r') as f:
    data = f.read().strip().split('\n')

# split the data into 2 sections: ranges (before the blank line) and IDs (after the blank line)
ranges = data[:data.index('')]
IDs = data[data.index('') + 1:]

# %%
# Now need to convert ranges into integer pairs like this [(start1, end1), (start2, end2), ...]
IDs_df = pd.DataFrame(IDs)
ranges_df = pd.DataFrame((range_str.split('-') for range_str in ranges), columns=['start', 'end'])

#%%
# convert to integers
ranges_df['start'] = ranges_df['start'].astype(int)
ranges_df['end'] = ranges_df['end'].astype(int)

#%%
# sort by start
# sorted = ranges_df.sort_values(by='start')
ranges_df = ranges_df.sort_values(by='start').reset_index(drop=True)

# %%
# calculate running max of 'end'
ranges_df['max_end_so_far'] = ranges_df['end'].shift().cummax()

#%%
# new group when current start > maximum end seen so far
ranges_df['new_group'] = (ranges_df['start'] > ranges_df['max_end_so_far'].fillna(-1)).cumsum()

#%%
merged_ranges = ranges_df.groupby('new_group').agg({'start': 'min', 'end': 'max'}).reset_index(drop=True)

# %%
# then for every id in IDs, check if it's in ANY of the ranges
# first convert IDs to ints
IDs_df = pd.DataFrame([int(id_val) for id_val in IDs], columns=['id'])

# %%
# add temp key for cross join
merged_ranges['key'] = 1
IDs_df['key'] = 1


# %%
# cross join
cross = IDs_df.merge(merged_ranges, on='key').drop('key', axis=1)

# %%
# check if ID is in range
cross['in_range'] = (cross['id'] >= cross['start']) & (cross['id'] <= cross['end'])

# %%
result = cross.groupby('id')['in_range'].any()

# %% 
# part 2: generating an inclusive count of all possible valid/fresh IDs
merged_ranges['count'] = merged_ranges['end'] - merged_ranges['start'] + 1

# %%
total_count = merged_ranges['count'].sum()

# %%
print(total_count)
# %%
