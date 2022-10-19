import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

           

app = dash.Dash()
app.layout = html.Div([
    
    html.H1(children ="This first Dash Webpage",style = {"textAlign" : "center", "color" : "red"}),
    #html.H2("This is header 2 ", style = {"textAlign" : "center","color" : "blue"} ),
    #html.H2("This is header 3 "),
    #html.H2("This is header 4 "),
    #html.H2("This is header 5 "),
    #html.H2("This is header 6 "),
    #html.H2("This is header 7 "),
    
    
    dcc.Graph(id="graph1",
        figure={
            "data":[
                {"x":[1,2,3], "y":[3,5,6],"type":"bar"},
                {"x":[1,2,3], "y":[9,6,2],"type":"bar"}
                
                ],
            "Layout":{
                "title" : " This is my first dash graph"
                
                
                }
                })
    
    
    
    
    
    
    
    
    
    ])

if __name__ == "__main__":
    app.run_server(port = 8051)