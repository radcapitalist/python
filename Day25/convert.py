
import os
import pandas
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

DATA_FNAME = "weather_data.csv"

pf = pandas.read_csv(DATA_FNAME)

monday = pf[pf.day == "Monday"]
montemp = monday.temp[0]
fahr = ((9 * montemp) / 5) + 32
boil = ((9 * 100) / 5) + 32
print(boil, fahr)
