# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import sys, os, glob
import pandas as pd
import numpy as np
from os.path import isfile

if __name__ == '__main__':
    indir = sys.argv[1]
    lists = glob.glob("{}/*.dat.result".format(indir))

    for filename in lists:
        print(filename, " processing")

        x = pd.read_csv(filename, dtype= {'segments':np.int32},  delim_whitespace=True).reset_index(drop=True)

        x["segments"] = x["segments"] // 2

        result = x.groupby(["segments"])["kN"].count()

        result.to_csv(filename.replace(".dat.result", ".result"), "\t")