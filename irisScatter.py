import plotly.express as px
import plotly.io as io
io.renderers.default='browser'


df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()