import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import dash_daq as daq

# from datetime import date
# from layout import *

layout_p3 = html.Div([
    
    html.H1('About us'),    
    html.Div([ dcc.Link('Home', href='/') ], className=''),
    html.Div([ dcc.Link('Access application', href='/dashboard') ], className=''),    

    dbc.Row([
        dbc.Col([ html.Span("Col 1") ], className='test', md=6),
        dbc.Col([ html.Span("Col 2") ], className='test', md=6),
    ], className='box-shadow test'),

    dbc.Row([
        dbc.Col([ html.Span("Col 3") ], className='test', md=6),
        dbc.Col([ html.Span("Col 4") ], className='test', md=6),
    ], className='box-shadow test'),
])