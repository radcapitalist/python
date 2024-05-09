
import os
import pandas
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
data_dname = dname + "/../Day25"
os.chdir(dname)

DATA_FNAME = data_dname + "/weather_data.csv"

pf = pandas.read_csv(DATA_FNAME)
print(pf)
for (index, row) in pf.iterrows():
    print(row.condition)