import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import plotly.graph_objs as go
from functions.data import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app = dash.Dash()

df = data

#print(df.columns)

years = get_year()
countries = get_countries()



app.layout = html.Div([
    
    html.Div([
        html.H1('Suicide Rates')
        # dcc.Markdown('# Suicide Rates')
    ], style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id = 'year-slider',
            min = min(years),
            max = max(years),
            value = min(years),
            marks = {str(year): str(year) for year in years}#,
            #step = None
        )
    ], style={'margin': 5}, ),
    html.Div([
        html.Div([
            html.P('Country History')
            # dcc.Markdown('## Country History')
        ], style={'marginTop': 40, 'textAlign': 'center'}),
        html.Div([
            dcc.Dropdown(
                style={'width': 400, 'marginLeft' : 40},
                id='dropdown',
                options=[{'label': i, 'value': i} for i in countries],
                value='Albania'
            ),
            dcc.Graph(id='graph')
        ]),
    ], style={'marginTop': 20, 'textAlign': 'center'})

])

@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')])
def update_y_timeseries(selected_country):
#def create_time_series(dff, axis_type, title):
    data = []
    axis_type = 'Linear'
    for year in years:
        data.append(get_suicides_no(year, selected_country))
    return {
        'data': [go.Scatter(
            x=years,
            y=data,
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)'
            }],
            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }




@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []

    # for para andar em cada país
    N = 1
    for i in filtered_df.country.unique():
        df_by_continent = filtered_df[filtered_df['country'] == i]
        traces.append(
            go.Scatter(
                x = (get_population(selected_year, i),),
                y = (get_suicides_no(selected_year, i),),
                text= 'Men: {} | Wonmen: {}'.format(get_suicides_no(selected_year, i, 'male'), get_suicides_no(selected_year, i, 'female')),
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            )
        )

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log','title': 'Population'},
            yaxis={'title': 'Suicide No'},
            #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }





if __name__ == '__main__':
    app.run_server(debug=True)