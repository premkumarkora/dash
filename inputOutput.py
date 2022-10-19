import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from dash import Input, Output


df= pd.DataFrame(
    {
    "student_id":[121,122,123,155,168],
    "marks":[1,2,3,1,2],
    }
    )

app = dash.Dash()
app.layout = html.Div([
    
    html.H1(children ="call backs",style = {"textAlign" : "center", "color" : "red"}),
    html.Div([
   dcc.Dropdown(list(range(1,5)), id="scores")
        ]),
    html.Div(id="ouput")
] )
@app.callback(
        Output("ouput", "children"),
        Input("scores", "value")
        
        )

def update_output_div(input_value):
    global df
    df1 = df[df['marks'] == input_value]
    return len(df1)


if __name__ == "__main__":
    app.run_server(port = 8051)