
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
print(pf)
num = 123
print(f"Types: num: {type(num)}, pf: {type(pf)}")
print(type(pf["temp"]))
as_dict = pf.to_dict()
print(as_dict)
temp_list = pf["temp"].to_list()
print(temp_list)
sum = 0
for temp in temp_list:
    sum += temp
print(f"Average: {sum / len(temp_list)}")
print(f"Max: {pf['temp'].max()}")
# print(f"Average2: {pf["temp"].mean()}")
#print(pf.temp)
print(pf.temp[3])
print("New")
print(pf[pf.day == "Tuesday"])
tues = pf[pf.day == "Tuesday"]
print(tues.condition, type(tues.condition))
print(f"tues temp type: {type(tues.temp)}")
print(tues.condition[1])
#print(f"tues temp: {tues.temp[0]}")
# print(pf["temp"])
# print(pf.head(4))
# print(pf.info())
# pf.plot()
# plt.show()

sunny = pf[pf.condition == "Sunny"]
print(type(sunny))
print(sunny)
print(sunny.temp[0])


#print(pf.plot())
