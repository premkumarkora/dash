import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


df= pd.DataFrame(
    {
    "Brand":["Maruthi", "BMW", "Benz","Volvo","Bugatti"],
    "Model":[2012, 2014, 2021, 2022, 2020],
    "Price":[500000, 3000000, 4500000, 6000000, 7500000]
    }
    )



app = dash.Dash()
app.layout = html.Div([
    
    html.H1(children ="This first Dash Webpage",style = {"textAlign" : "center", "color" : "red"}),
    
dcc.Slider(min=1,max=10,value=3,marks={i:i*2 for i in range(11)})


    ])


if __name__ == "__main__":
    app.run_server(port = 8051)