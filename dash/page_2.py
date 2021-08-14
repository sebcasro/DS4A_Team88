import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq

from datetime import date
from layout import *

layout_p2 = html.Div([
    # Título prediction
    dbc.Row([
        dbc.Col([ html.H4("Prediction", className='') ], className='', md=12),
    ], className='_pink'),

    dbc.Row([
        # Filtros
        dbc.Col([
            html.Div([
                html.H5("Filter", className='test1'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([ 
                    # Dates filter
                    dbc.Col([ html.Label('Dates') ], className='test1 right', md=4),

                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-1',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),

                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-1',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                ], className='test1'),

                html.Hr(),
                html.H5("Prediction scenarios", className='test1'),
                html.H6("Power generation availability", className='test1'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    # Hydraulic energy
                    dbc.Col([ html.Label('Hydraulic energy') ], className='test1 right', md=4),

                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-2',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-2',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-2',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),
                ], className='test1 p-bottom'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    dbc.Col([ html.Label('Thermal energy') ], className='test1 right', md=4),
                    
                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-3',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-3',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-3',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),               
                ], className='test1 p-bottom'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    dbc.Col([ html.Label('Solar energy') ], className='test1 right', md=4),
                    
                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-4',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-4',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-4',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),               
                ], className='test1 p-bottom'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    dbc.Col([ html.Label('Aporte caudal m3/s') ], className='test1 right', md=4),
                    
                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-5',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-5',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-5',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),               
                ], className='test1 p-bottom'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    dbc.Col([ html.Label('Aporte energía gW/h ') ], className='test1 right', md=4),
                    
                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-6',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-6',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-6',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),               
                ], className='test1 p-bottom'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    dbc.Col([ html.Label('Volumen útil diario Mm3') ], className='test1 right', md=4),
                    
                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-7',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-7',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-7',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),               
                ], className='test1 p-bottom'),

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                dbc.Row([
                    dbc.Col([ html.Label('Vertimientos miles m3') ], className='test1 right', md=4),
                    
                    # DatePickerSingle - start date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-start-8',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='Start date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # DatePickerSingle - end date
                    dbc.Col([ 
                        dcc.DatePickerSingle(
                            id='data-end-8',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            placeholder='End date',
                            with_portal=True,
                            display_format='DD/MM/YYYY'
                        ),
                    ], className='test1', md=3),
                    
                    # Percentage input
                    dbc.Col([ 
                        daq.NumericInput(
                            id='percentage-8',
                            min=0,
                            max=100,
                            value=100
                        )
                     ], className='test1', md=2),
                ], className='test1 p-bottom'),

                # Buttons
                dbc.Row([
                    dbc.Col([ ], className='test1', md=2),
                    dbc.Col([ 
                        # html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),
                        dbc.Button("Clear changes", color="primary", block=True, className="mr-1", id='clear_button'),
                    ], className='col_button', md=4),
                    dbc.Col([ 
                        # html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),
                        dbc.Button("Apply changes", color="primary", block=True, className="mr-1", id='changes_button'),
                    ], className='col_button', md=4),
                    dbc.Col([ ], className='test1', md=2),

                ], className='test1'),
                
            ], className='box-shadow', style={'height': '100%'})
        ], className='box test1', md=4),

        # Gráfica principal
        dbc.Col([ html.Div([ dcc.Graph(id='graph1', style={'height': '48vh'}, className='') ], className='box-shadow') ], className='box', md=8),
    ]),

    html.Hr(),

    # Título description
    dbc.Row([
        dbc.Col([ html.H4("Description", className='') ], className='_pink', md=12),
    ], className='class'),

    dbc.Row([
        # Gráfica 2
        dbc.Col([ html.Div([ dcc.Graph(id='graph2', style={'height': '32vh'}, className='') ], className='box-shadow') ], className='box', md=4),

        # Gráfica 3
        dbc.Col([ html.Div([ dcc.Graph(id='graph3', style={'height': '32vh'}, className='') ], className='box-shadow') ], className='box', md=4),

        # Gráfica 4
        dbc.Col([ html.Div([ dcc.Graph(id='graph4', style={'height': '32vh'}, className='') ], className='box-shadow') ], className='box', md=4),
    ], className=''),

    html.Hr(),

    dbc.Row([
        dbc.Col([    
            html.Label('Selection'),
            dcc.Dropdown(
                id="data_selection", value=df.columns[1], clearable=False,
                options=[{"label": x, "value": x} for x in df.columns[1:]]
            ),
        ], className='box', md=4),
    ], className=''),
])