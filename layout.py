from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)


app.layout = html.Div(children=[
    html.Div(children=[
        html.H3(children='Kora School of Excellence'),
        html.H6(children='Come Learn Excell', style={'marginTop': '-15px', 'marginBottom': '30px'})
    ], style={'textAlign': 'center'}),

    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.H3(id='no_acc', style={'fontWeight': 'bold'}),
                html.Label('Total accidents', style={'paddingTop': '.3rem'}),
                ], className="three columns number-stat-box"),
            html.Div(children=[
                html.H3(id='no_cas', style={'fontWeight': 'bold', 'color': '#f73600'}),
                html.Label('Casualties', style={'paddingTop': '.3rem'}),
                ], className="three columns number-stat-box"),

            html.Div(children=[
                html.H3(id='no_veh', style={'fontWeight': 'bold', 'color': '#00aeef'}),
                html.Label('Total vehicles', style={'paddingTop': '.3rem'}),
                ], className="three columns number-stat-box"),
        ])
    ])









], style={'padding': '2rem'})





if __name__ == '__main__':
    app.run_server(debug=True)