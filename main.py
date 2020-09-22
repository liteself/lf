# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import glob, sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    indir = sys.argv[1]

    large_filename = "large.result.txt"
    small_filename = "small.result.txt"
    result_filename = "result.txt"

    lists = glob.glob("{}/*.dat.result".format(indir))
    lists.sort(key = lambda s: int(s.split('_')[-1].split('\\')[-1][:-11]))
    large_df = None
    small_df = None
    for filename in lists:
        print(filename, " processing")

        x = pd.read_csv(filename, delim_whitespace=True)
        if len(x) % 2 != 0:
            x = x.drop(x.index[[-1]])

        x = x.reset_index(drop=True)

        first, second = x[:2]["kN"].to_numpy()
        large_index = 0
        small_index = 1

        if first < second:
            large_index = 1
            small_index = 0

        if large_df is None:
            large_df = x[large_index::2]
        else:
            large_df = large_df.append(x[large_index::2])

        if small_df is None:
            small_df = x[small_index::2]
        else:
            small_df = small_df.append(x[small_index::2])

    large_df = large_df.reset_index(drop=True)
    small_df = small_df.reset_index(drop=True)

    large_df.to_csv(large_filename, " ", header=False)
    small_df.to_csv(small_filename, " ", header=False)

    
    result = (large_df['kN'].to_numpy() - small_df["kN"].to_numpy()) / (large_df['mm'].to_numpy() - small_df["mm"].to_numpy())

    result = pd.DataFrame(result, columns=["ratio"])
    result.to_csv(result_filename, " ", header=False)
