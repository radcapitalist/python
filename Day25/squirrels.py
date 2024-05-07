import os
import pandas
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

DATA_FNAME = "squirrel_data.csv"

df_squirrels = pandas.read_csv(DATA_FNAME)
color = df_squirrels["Primary Fur Color"]
print(color)
red = df_squirrels[df_squirrels["Primary Fur Color"] == "Cinnamon"]
n_red = red.shape[0]
gray = df_squirrels[df_squirrels["Primary Fur Color"] == "Gray"]
n_gray = gray.shape[0]

black = df_squirrels[df_squirrels["Primary Fur Color"] == "Black"]
n_black = black.shape[0]

print(n_red, n_gray, n_black)

dict = {
    "color": ["gray", "red", "black"],
    "count": [n_gray, n_red, n_black]
}
print(dict)

summ_df = pandas.DataFrame.from_dict(dict)
print(summ_df)

summ_df.to_csv("squirrel_counts.csv")

