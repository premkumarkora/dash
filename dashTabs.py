from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv("class2022.csv")

gb_df= df.groupby(["group"])[["Percent"]].mean()

fig = px.bar(gb_df)


app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(
        id="tabs-with-classes-2",
        value='tab-2',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Key Performance Indicators',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab two',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab three, multiline',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab four',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes-2')
])

@app.callback(Output('tabs-content-classes-2', 'children'),
              Input('tabs-with-classes-2', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            
            
            
            
            fig.layout.height = 300,
            dcc.Graph(id='example-graph-2',figure=fig,  ),
            
            
            
            
            
            
            
            
            
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
