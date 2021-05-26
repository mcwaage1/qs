# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser 
# (or whatever you set the port=<value> in app.run_server())
# https://dash.plotly.com/deployment

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

filename = "qs/dashboard/test_app.py"

# https://pythonspot.com/read-file/
with open('/home/mcwaage1/' + filename) as f:
    testfile = f.read().splitlines()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('~/qs/dashboard/date_weight_df.csv')

def file_iterator_to_html(file):
    lines = []
    for line in file:
        lines.append(html.Pre(line))
    return html.Div(lines)

def make_code(file):
    return html.Div([
        html.Details([
            html.Summary('Code'),
            html.Div(file_iterator_to_html(file))
        ])
    ], style={'padding-bottom': '2em'})

def make_footer():
    return html.Div(html.Footer(['Matthew Waage',
                        html.A('github.com/mcwaage1',
                               href='http://www.github.com/mcwaage1',
                               target='_blank',
                               style = {'margin': '.5em'}),
                        html.A('mcwaage1@gmail.com',
                               href="mailto:mcwaage1@gmail.com",
                               target='_blank',
                               style = {'margin': '.5em'}),
                        html.A('waage.dev',
                               href='http://www.waage.dev', 
                               target='_blank',
                               style = {'margin': '.5em'})
                       ], style={'position': 'fixed',
                                 'text-align': 'right',
                                 'left': '0px',
                                 'bottom': '0px',
                                 'margin-right': '10%',
                                 'color': 'black',
                                 'display': 'inline-block',
                                 'background': '#f2f2f2',
                                 'border-top': 'solid 2px #e4e4e4',
                                 'width': '100%'}))

def make_hist_with_bins(series, bins, tickangle):
    
    title = f"Number of Days <br>At Specified {series.name} Level"
    
    fig = go.Figure(data=[go.Histogram(x=series)])
    
    fig.update_layout(title=dict(text=title, 
                                 yanchor="top",
                                 y=.85,
                                 xanchor="left",
                                 x=.075),
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1),
                     bargap=0.1)
    fig.update_traces(xbins_start=min(series), xbins_size=bins, selector=dict(type='histogram'))
    fig.update_xaxes(tickmode='linear', dtick=bins, tickangle=tickangle)
    fig.update_xaxes(title_text=f"{series.name} Level")
    fig.update_yaxes(title_text=title)
    
    return html.Div([
        dcc.Graph(
            figure=fig
        )
    ])

def make_scatter(series):
    
    x = df['Date']
    y = series
    rolling = 7
    y2 = round(y.rolling(rolling).mean(), 2)   
    title= f"{y.name} Over Time"
        
    fig = go.Figure(data=[go.Scatter(x=x, y=y, name=f'{y.name}', mode='markers'),
                          go.Scatter(x=x, y=y2, name=f"{rolling} Day Rolling Average {y.name}", marker_color='blue')])

    fig.update_layout(title=dict(text=title, 
                                 yanchor="top",
                                 y=.85,
                                 xanchor="left",
                                 x=.075),
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1))

    fig.update_xaxes(title_text=f"{x.name}")
    fig.update_yaxes(title_text=f"{y.name}")
    
    return html.Div([
        dcc.Graph(
            figure=fig
        )
    ])

def make_dashboard(series, file, bins, tickangle):
    
    title = '2020 Weight Dashboard'
    
    app = dash.Dash(__name__,
                    external_stylesheets=external_stylesheets, 
                    title=f"{title}")
    
    server = app.server

    app.layout = html.Div([
        html.H4(f"{title}", style={'padding-left': '5%'}),
        html.Div([
            html.P("This is an interactive Plotly-Dash dashboard."),
            html.P("You can; hover your mouse over the various points for more detailed information, click on the legend to turn off or on whatever points or lines there may be, or click and drag to get a closer look at whatever information you're most interested in."),
            html.P("In this particular graph we have my weight for all of 2020, with all of it's variability. Check it out."),
        ], style={'padding-left': '5%',
                  'padding-top': '2em'}),
        make_scatter(series),
        make_hist_with_bins(series, bins, tickangle),
        make_code(file),
        make_footer()
    ])

    if __name__ == '__main__':
        app.run_server(debug=False, use_reloader=True)
        
make_dashboard(series=df['Weight'], file=testfile, bins=.2, tickangle=305)