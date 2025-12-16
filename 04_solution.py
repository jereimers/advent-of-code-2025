# %%
import logging
import pandas as pd

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# %%

with open('04_input.txt', 'r') as f:
    data = f.read().strip().split('\n')

data_grid = [list(row) for row in data]

df = pd.DataFrame(data_grid)
binary_df = (df == '@').astype(int)
step = 0
total_valid_rolls = 0

#%%

while True:
    step += 1

    neighbor_counts = pd.DataFrame(0, index=binary_df.index, columns=binary_df.columns)
    directions = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,0), (1,1)]

    for r_shift, c_shift in directions:
        # shift(n) shifts rows (vertical)
        # shift(n, axis=1) shifts columns (horizontal)

        shifted = binary_df.shift(r_shift, axis=0).shift(c_shift, axis=1).fillna(0)
        neighbor_counts += shifted

    valid_mask = (binary_df == 1) & (neighbor_counts < 4)

    current_count = valid_mask.sum().sum()

    if current_count == 0:
        print(f"Loop ended after {step - 1} steps")
        break

    # now repeating this procedure until we can't get any more rolls
    binary_df[valid_mask] = 0

    total_valid_rolls += current_count


# %%
print(f"{total_valid_rolls}")