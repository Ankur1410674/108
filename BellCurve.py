import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
print(df.groupby("Mobile Brand")["Avg Rating"].mean()),
Fig=go.Figure(go.bar(x=df.groupby("Mobile Brand")["Avg Rating"].mean(),
y=["Samsung" , "Apple" , "Nokia" , "Motorola","HUAWEI","Sony"],
orientation="h"))
Fig.show()