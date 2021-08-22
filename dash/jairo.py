import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from layout import df

years = list(reversed(df.Year.unique()))
years.insert(0, 'All')

months = list(df.Month2.unique())
months.insert(0, 'All')

tab2_content = html.Div([
    dbc.Row([
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
                                        dcc.Graph(id='graph5', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 2
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph6', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                            # ::::::::::::::::::::::::::::::::
                            # Second graphs row
                            dbc.Row([
                                # Gráfica 3
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph7', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 4
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph8', style={'height': '32vh'}, className='') 
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
                                        dcc.Graph(id='graph9', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 2
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph10', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                            # ::::::::::::::::::::::::::::::::
                            # Second graphs row
                            dbc.Row([
                                # Gráfica 3
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph11', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),

                                # Gráfica 4
                                dbc.Col([
                                    html.Div([
                                        dcc.Graph(id='graph12', style={'height': '32vh'}, className='') 
                                    ], className='test')
                                ], className='test', md=6),
                            ], className='test'),

                        ], className="test tab-border")
                    ], label="Contribution"),









                    # ::::::::::::::::::::::::::::::::
            ])
        ], className='test no-side-padding', id='', md=12),
    ], className='test'),
], className="test tab-border2")


tab1_content = html.Div([
    dbc.Row([
        dbc.Col([
            html.P("This is tab 1!"),
            dbc.Button("Click here", color="success"),
        ], className='test', id='', md=12),
    ], className='test'),
], className="test tab-border")


layout_test = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(tab2_content, label="Description"),
                dbc.Tab(tab1_content, label="Prediction"),
            ])
        ], className='test no-side-padding', id='hola', md=12),
    ], className='test card-box-border'),
])