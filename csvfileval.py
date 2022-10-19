import pandas as pd
import plotly.express as px 

df = pd.read_csv("class2022.csv")
dff = df.copy()
dff = dff[dff["group"] =="COM"]

dffmean = dff[["eng","maths", "commerce", "ecnomics","accounts","language"] ].mean()
dffmax = dff[["eng","maths", "commerce", "ecnomics","accounts","language"] ].max()
dffmin = dff[["eng","maths", "commerce", "ecnomics","accounts","language"] ].min()

#dff = dff.groupby("eng").sum() == "COM"

print(dffmean)
print("Max = ",dffmax)
print(dffmin)

dff.plot.pie(subplots=True)



