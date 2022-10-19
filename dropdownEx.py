# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:11:24 2022

@author: KORA
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:00:31 2022

@author: KORA
"""

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
    
   dcc.Dropdown(
   options=[
       {"label" : "Maruthi", "value" : "Maruthi"}, 
       {"label" : "BMW",     "value" : "BMW"},
       {"label" : "Benz",    "value" : "Benz"},
       {"label" : "Volvo",   "value" : "Volvo"},
   ],
   value='Maruthi',
   multi=True,
   style = dict(
       width = '40%',
       display = 'inline-block',
       verticalAlign = "middle"
               )
)


    ])


if __name__ == "__main__":
    app.run_server(port = 8051)