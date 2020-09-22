# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import sys, os, glob
import pandas as pd
from os.path import isfile
if __name__ == '__main__':
    indir = sys.argv[1]
    lists = glob.glob("{}/*.dat.result".format(indir))

    for filename in lists:
        print(filename, " processing")
        x = pd.read_csv(filename, delim_whitespace=True, encoding= 'unicode_escape').reset_index(drop=True)
        x = x[::50]
        x.to_csv(filename, " ", index=False)

        eyy_filename = filename.replace(".dat.result", ".csv.result")
        
        y = pd.read_csv(eyy_filename, sep=',')

        res = pd.DataFrame()
        res["kN"] =  x["kN"].reset_index(drop=True)
        res["eyy [1] - Lagrange"] = y["eyy [1] - Lagrange"].reset_index(drop=True)
        
        res["X"] = abs(res["kN"]) / res["eyy [1] - Lagrange"]

        res.to_csv(filename.replace(".dat.result", ".result"), "\t", index=False)