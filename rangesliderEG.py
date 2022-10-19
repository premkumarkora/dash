import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from dash import Input, Output



app = dash.Dash()
app.layout = html.Div([
    
    html.H1(children ="call backs",style = {"textAlign" : "center", "color" : "red"}),
    html.Div([
        "Please enter your Name ",
        dcc.Input(id="my_input", value="Prem", type="text")]),
        
        html.Br(),
        html.Div(id="my_ouput"),
        ])

@app.callback(
        Output(component_id="my_ouput", component_property="children"),
        Input(component_id="my_input", component_property="value")
        
        )

def update_output_div(input_value):
    input_value = "Hi, How are you" + input_value
    return f'Output:{input_value}'


if __name__ == "__main__":
    app.run_server(port = 8051)