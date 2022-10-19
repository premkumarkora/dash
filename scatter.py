import plotly.express as px
import pandas as pd 

df = pd.read_csv("class2022.csv")

#df= df[df["group"] =="MPC"]

kf=df.groupby(["group","sex"]).sum()


# filter = df[df[["eng","maths", "phy", "che","cse", "language"]] >= 45].count()
# filter1 = df[df[["eng","maths", "phy", "che","cse", "language"]] < 45].count()
# df1 = pd.DataFrame({"pass":filter})
# df1["fail"] = filter1


# df3 = df1.loc[(df1 != 0).any(axis=1)]
# print(df3)


# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
#                  size='petal_length', hover_data=['petal_width'])
# fig.show()