import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from layout import *

years = list(reversed(df.Year.unique()))
years.insert(0, 'All')

months = list(df.Month.unique())
months.insert(0, 'All')

tab1_content = html.Div([
    dbc.Row([
        dbc.Col([
            html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
            html.Hr()
        ], className='test', id='tab_text_description', md=12),

        dbc.Col([
            dbc.Tabs([
                    # ::::::::::::::::::::::::::::::::
                    # Tab 1
                    dbc.Tab([
                        html.Div([
                            # ::::::::::::::::::::::::::::::::
                            # Filter row
                            dbc.Row([
                                dbc.Col([
                                    # Year selection dropdown
                                    dbc.FormGroup([
                                        dbc.Label("Year", html_for="year_tab1"),
                                        dcc.Dropdown(
                                            id="year_tab1", value=years[0], clearable=False,
                                            options=[
                                                {"label": x, "value": x} for x in years
                                            ],
                                        ),
                                    ]),
                                ], className='test', md=1),

                                dbc.Col([
                                    # Month selection dropdown
                                    dbc.FormGroup([
                                        dbc.Label("Month", html_for="month_tab1"),
                                        dcc.Dropdown(
                                            id="month_tab1", value=months[0], clearable=False,
                                            options=[
                                                {"label": x, "value": x} for x in months
                                            ],
                                        ),
                                    ]),
                                ], className='test', md=1),

                                dbc.Col([
                                    # Energy type dropdown
                                    dbc.FormGroup([
                                        dbc.Label("Energy type", html_for="energy_type"),
                                        dcc.Dropdown(
                                            id="energy_type", value='All', clearable=False,
                                            options=[
                                                {"label": "All" , "value": 'All'},
                                                {"label": "Hydraulic energy", "value": "Hydraulic energy"},
                                                {"label": "Thermal energy", "value": "Thermal energy"},
                                                {"label": "Solar energy", "value": "Solar energy"},
                                            ],
                                        ),
                                    ]),
                                ], className='test', md=2),
                            ], className='test min-height-84'),

                            # ::::::::::::::::::::::::::::::::
                            # First graphs row
                            dbc.Row([
                                # Gráfica 1
                                dbc.Col([
                                    html.Div([
                                        dbc.Checklist(
                                            options=[{"label": "Show data by months", "value": 0}],
                                            value=[], id="graph5_switch", switch=True,
                                        ),
                                        dcc.Graph(id='graph5', style={'height': '64vh'}, className=''),
                                        html.P(id='graph5_description', children=['graph5_description']),
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 2
                                dbc.Col([
                                    html.Div([
                                        dbc.Checklist(
                                            options=[{"label": "Show data by months", "value": 0}],
                                            value=[], id="graph6_switch", switch=True,
                                        ),
                                        dcc.Graph(id='graph6', style={'height': '64vh'}, className=''),
                                        html.P(id='graph6_description', children=['graph6_description']),
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                            # ::::::::::::::::::::::::::::::::
                            # Second graphs row
                            dbc.Row([
                                # Gráfica 3
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph7', style={'height': '64vh'}, className=''),
                                        html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'), 
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 4
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph8', style={'height': '64vh'}, className=''),
                                        html.P(
                                            id='graph8_description', 
                                            children=['On this table, you can see the plants that generate the most energy, the amount of energy generated and the source']
                                        ),
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                        ], className="test tab-border")
                    ], label="Power Generated"),

                    # ::::::::::::::::::::::::::::::::
                    # Tab 2
                    dbc.Tab([
                        html.Div([
                            # ::::::::::::::::::::::::::::::::
                            # Filter row
                            dbc.Row([
                                dbc.Col([
                                    # Year selection dropdown
                                    dbc.FormGroup([
                                        dbc.Label("Year", html_for="year_tab2"),
                                        dcc.Dropdown(
                                            id="year_tab2", value=years[0], clearable=False,
                                            options=[
                                                {"label": x, "value": x} for x in years
                                            ],
                                        ),
                                    ]),
                                ], className='test', md=1),

                                dbc.Col([
                                    # Month selection dropdown
                                    dbc.FormGroup([
                                        dbc.Label("Month", html_for="month_tab2"),
                                        dcc.Dropdown(
                                            id="month_tab2", value=months[0], clearable=False,
                                            options=[
                                                {"label": x, "value": x} for x in months
                                            ],
                                        ),
                                    ]),
                                ], className='test', md=1),

                                # m3 vs gw option
                                dbc.Col([
                                    dbc.FormGroup([
                                        dbc.Label("Choose one"),
                                        dbc.RadioItems(
                                            id="radio_input", value="m3/s", inline=True,
                                            options=[
                                                {"label": "m3/s", "value": "m3/s"},
                                                {"label": "gW", "value": "gW"},
                                            ],
                                        ),
                                    ])
                                ], className='test', md=2),
                            ], className='test min-height-84'),

                            # ::::::::::::::::::::::::::::::::
                            # First graphs row
                            dbc.Row([
                                # Gráfica 1
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph9', style={'height': '64vh'}, className=''),
                                        html.P(
                                            id='graph9_description', 
                                            children=[
                                                'On this ',
                                                dcc.Link('scatter plot,', href='https://en.wikipedia.org/wiki/Scatter_plot', target='_blank'),
                                                ' we can see the upward relationship between the flow contribution and the energy contribution in Colombia.', 
                                            ]
                                        ),
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 2
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph10', style={'height': '64vh'}, className=''),
                                        html.P(
                                            id='graph10_description', 
                                            children=[
                                                'On this ',
                                                dcc.Link('box plot,', href='https://en.wikipedia.org/wiki/Box_plot', target='_blank'),
                                                ' we can see the flow ("energy") contribution to the Hydro plants, each month in Colombia.', 
                                            ]
                                        ),
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                            # ::::::::::::::::::::::::::::::::
                            # Second graphs row
                            dbc.Row([
                                # Gráfica 3
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph11', style={'height': '64vh'}, className=''),
                                        html.P(
                                            id='graph11_description', 
                                            children=[
                                                'On this ',
                                                dcc.Link('scatter plot,', href='https://en.wikipedia.org/wiki/Scatter_plot', target='_blank'),
                                                ' we can see the relationship between the flow ("energy") contribution and the energy price in Colombia.', 
                                            ]
                                        ),
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 4
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph12', style={'height': '64vh'}, className=''),
                                        html.P(
                                            id='graph12_description', 
                                            children=[
                                                'On this ',
                                                dcc.Link('time series,', href='https://en.wikipedia.org/wiki/Time_series', target='_blank'),
                                                ' we can see the behavior of the flow ("energy") contribution over time, showing its highest and lowest flow at the same time.', 
                                            ]
                                        ),
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                        ], className="test tab-border")
                    ], label="Contribution"),



                    # ::::::::::::::::::::::::::::::::
            ])
        ], className='test no-side-padding', md=12),
    ], className='test'),
], className="test tab-border2")


tab2_content = html.Div([
    dbc.Row([
        dbc.Col([
            html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
            html.Hr()
        ], className='test', id='tab_text_prediction', md=12),

        dbc.Col([

            html.H5("Filters"),
            
            dbc.FormGroup([
                dbc.Label("Temp", html_for="temp_dropdown"),
                dcc.Dropdown(
                    id="temp_dropdown", value='01', clearable=False,
                    options=[
                        {"label": "Temp primero", "value": '01'},
                        {"label": "Temp segundo", "value": "02"},                    
                        {"label": "Temp tercero", "value": "03"},
                    ],
                ),
            ]),
        ], className='test borde-right', md=4),


        # Gráfica principal
        dbc.Col([ 
            html.Div([ 
                dcc.Graph(id='graph1', style={'height': '52vh'}, className=''),
                html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
            ], className='test')
        ], className='test', md=8),

    ], className='test'),
    
    # dbc.Row([
    #     dbc.Col([ 
    #         html.Div([ 
    #             dcc.Graph(id='graph2', style={'height': '32vh'}, className=''),
    #             html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
    #         ], className='test')
    #     ], className='test', md=4),

    #     dbc.Col([ 
    #         html.Div([ 
    #             dcc.Graph(id='graph3', style={'height': '32vh'}, className=''),
    #             html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
    #         ], className='test')
    #     ], className='test', md=4),

    #     dbc.Col([ 
    #         html.Div([
    #             dcc.Graph(id='graph4', style={'height': '32vh'}, className=''),
    #             html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
    #         ], className='test')
    #     ], className='test', md=4),

    # ], className='test borde-top'),
], className="test tab-border")


layout_p2 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(tab1_content, label="Description"),
                dbc.Tab(tab2_content, label="Prediction"),
            ])
        ], className='test no-side-padding', id='hola', md=12),
    ], className='test card-box-border'),
])