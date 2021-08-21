import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


tab2_content = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Tabs([
                    # ::::::::::::::::::::::::::::::::
                    # Tab 1
                    dbc.Tab([
                        html.Div([
                            
                            dbc.Row([
                                dbc.Col([
                                    html.P("Filtros"),
                                ], className='test', id='', md=12),
                            ], className='test'),

                            dbc.Row([
                                dbc.Col([
                                    html.P("Gráfica 1"),
                                ], className='test', id='', md=6),

                                dbc.Col([
                                    html.P("Gráfica 2"),
                                ], className='test', id='', md=6),
                            ], className='test'),

                            dbc.Row([
                                dbc.Col([
                                    html.P("Gráfica 3"),
                                ], className='test', id='', md=6),

                                dbc.Col([
                                    html.P("Gráfica 4"),
                                ], className='test', id='', md=6),
                            ], className='test'),

                        ], className="test tab-border")
                    ], label="Tab 1"),

                    # ::::::::::::::::::::::::::::::::
                    # Tab 2
                    dbc.Tab([

                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                    html.P("This is tab 2!"),
                                    dbc.Button("Click here", color="success"),
                                ], className='test', id='', md=12),
                            ], className='test'),
                        ], className="test tab-border")

                    ], label="Tab 2"),
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