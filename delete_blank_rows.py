import os
from os import listdir

import csv, re
import os.path
import pandas as pd

dirpath = os.getcwd()
			
import codecs
		
def find_csv_filenames(path_to_dir, suffix=".csv" ):
    path_to_dir = os.path.normpath(path_to_dir)
    filenames = listdir(path_to_dir)

    fp = lambda f: not os.path.isdir(path_to_dir+"/"+f) and f.endswith(suffix)
    return [path_to_dir+"/"+fname for fname in filenames if fp(fname)]
csv_files = find_csv_filenames("D:/Laboratory/PetraBasillea", ".csv")

for f in csv_files:

        df = pd.read_csv(f , sep=',') 

        df.to_csv(f,  index = False)