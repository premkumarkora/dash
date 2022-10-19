# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:16:39 2022

@author: KORA
"""

import dash
from dash import html
from dash import dcc  #dash core components

app = dash.Dash()

app.layout=html.Div(
    [
     
     html.H1("king of Dash"),
     
     
     
     dcc.Graph(
         id="my_graph",
         figure = 
         {
             "data":
             [
                 {
                     "x":[1,2,3,4],
                     "y":[3,4,5,1],
                     "type":"bar",
                     "name":"female"
                }
              ]
        }
                  
    )

        
])
     



if __name__ == "__main__":
    app.run_server()