import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("108classdata.csv")
fig = ff.create_distplot([df["Weight"].tolist()],["Weight"],show_hist = False)
fig.show()


df1 = pd.read_csv("108classdata.csv")
fig1 = ff.create_distplot([df1["Height"].tolist()],["Height"],show_hist = False)
fig1.show()