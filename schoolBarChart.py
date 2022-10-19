import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import plotly.io as pio
pio.renderers.default='browser'




app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")

df = pd.read_csv("class2022.csv")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Kora School of Excellence", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_dept",
                 options=[
                     {"label": "Computer Science",  "value": "MPC"},
                     {"label": "Medicine",          "value": "MPB"},
                     {"label": "Commerce",          "value": "COM"}],
                 multi=False,
                 value="MPB",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_dept', component_property='value')]
)
def update_graph(option_slctd):
    #print(option_slctd)
    #print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["group"] ==option_slctd]
    dffmean = dff[["eng","maths", "phy", "che","biology","language", "commerce", 
                   "ecnomics","accounts","cse"] ].mean()
    dffmean.dropna(inplace=True)

    # Plotly Express
    fig = px.bar(dffmean)


    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
    
    