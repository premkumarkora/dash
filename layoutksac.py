from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)



app.layout = html.Div(children=[
    html.Div(children=[
        html.Div(children=[
            html.Label('By Department'),
    
            html.Label('By Mentor:'),
    
            html.Label('Marks:'),
    
        ] ),
        html.Div(children=[
            html.Label('By Department'),
    
            html.Label('By Mentor:'),
    
            html.Label('Marks:'),
    
        ] ),
    ])
    
   
    
    
    
])
















if __name__ == '__main__':
    app.run_server(debug=True)