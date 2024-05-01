
import os
import csv
import pandas
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

DATA_FNAME = "weather_data.csv"

# with open(f"{DATA_FNAME}") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if not row[0] == 'day':
#             temperatures.append(float(row[1]))

pf = pandas.read_csv(DATA_FNAME)
print(pf["temp"])
print(pf.head(4))
print(pf.info())
pf.plot()
plt.show()

#print(pf.plot())
