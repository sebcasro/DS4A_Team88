import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from layout import *
from projection import *

import plotly.express as px
from datetime import date

years_projection = list(reversed(projection_df.Year.unique()))
years_projection.insert(0, 'All')

years = list(reversed(df.Year.unique()))
years.insert(0, 'All')

months = list(df.Month.unique())
months.insert(0, 'All')

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Gráfica principal
projection_df_temp = projection_df.copy()
main_fig = px.line(projection_df_temp, x="Date", y="value", color='model', title="kW/h price forecasting")

main_fig.update_layout(
    # font_family="Rockwell",
    margin=dict(l=60, r=0, t=50, b=70),
    font_color='#757575'
)
del projection_df_temp
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

tab1_content = html.Div([
    dbc.Row([
        dbc.Col([
            html.P('Here the dataset available as input to predict the energy stock price can be explored in depth in order to identify the more relevant information. With the help of different types of graphs of the time series dataset, the behavior, trends, seasonality, other patterns and interesting relations between variables can be identified and easily explored. Also the idea is to provide you a better understanding of the data set variables available , as you can investigate them and summarize their main characteristics customizing the graphics presented below.'),
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
                                    html.P(
                                        id='graph7_description', 
                                        children=[
                                            'On this ',
                                            dcc.Link('scatter plot,', href='https://en.wikipedia.org/wiki/Scatter_plot', target='_blank'),
                                            ' we can see the relationship between the total availability and the price energy market in Colombia.',
                                        ]
                                    ),
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
            ])
        ], className='test no-side-padding', md=12),
    ], className='test'),
], className="test tab-border2")


tab2_content = html.Div([
    dbc.Row([
        dbc.Col([
            html.P('The following interactive graph presents the results of our Machine Learning models to generate the energy price forecast, constructed from historical price information and the explanatory variables: Hydraulic Availability, Thermal Availability, Flow contribution, Daily Volume (Mm3), Volume (Mm3) and Daily Useful Volume (gWh), whose definitions can be found in the tab: Glossary.'),
            html.P('Our Machine Learning models are: ARIMA, SARIMAX and Neural Prophet. These three selected models are the best performing after having tested more than 150 different models to project all the series that are required for this exercise.'),
            html.P('Given that the parameters of each model assign different values to the information that is incorporated into them, the results they deliver also differ, and for this reason we decided to add an additional projection which is the average of the former projections. This projection has the advantage of reducing what may be the furthest or most extreme values of each model with respect to the others.'),
            html.P('Finally, understanding that the greatest difficulty that time series models have in long time horizons, as in this case, is to be able to anticipate unexpected events that affect the price, we estimated and incorporated the corresponding impulse response functions from the SARIMAX model to simulate different types of shocks on our projections, and apply them over all the projections.'),
            html.Hr()
        ], className='test', id='tab_text_prediction', md=12),

        dbc.Col([

            html.H5("Prediction Impulse Scenario"),

            dbc.Label("Impulse input date: ", html_for="impulse_date"),

            dcc.DatePickerSingle(
                id='impulse_date',
                min_date_allowed=date(2021, 7, 14),
                # max_date_allowed=date(2017, 9, 19),
                initial_visible_month=date(2021, 7, 14),
                placeholder='Pick a date',
                with_portal=True,
                display_format='DD/MM/YYYY',
            ),
            
            html.Br(),

            dbc.FormGroup([
                dbc.Label("Forecasting model", html_for="forecasting_model"),
                dcc.Dropdown(
                    id="forecasting_model", value=0, clearable=False,
                    options=[
                        {"label": 'Select a forecasting model', "value": 0},
                        {"label": 'ARIMA', "value": 'ARIMA'},
                        {"label": 'SARIMAX', "value": 'SARIMAX'},
                        {"label": 'Neural Prophet', "value": 'Neural Prophet'},
                        {"label": 'mean models', "value": 'mean models'},
                    ],
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("Variable affected by impulse", html_for="variable_shocked"),
                dcc.Dropdown(
                    id="variable_shocked", value=0, clearable=False,
                    options=[
                        {"label": 'Select a variable', "value": 0},
                        {"label": 'Hydraulic availability', "value": 'Hydraulic availability'},
                        {"label": 'Thermal availability', "value": 'Thermal availability'},
                        {"label": 'Flow contribution', "value": 'Flow contribution'},
                        {"label": 'Daily volume (Mm3)', "value": 'Daily volume (Mm3)'},
                        {"label": 'Volume (Mm3)', "value": 'Volume (Mm3)'},
                        {"label": 'Daily useful Volume (gWh)', "value": 'Daily useful Volume (gWh)'},
                    ],
                ),
            ]),

            dbc.FormGroup([
                dbc.Label("Impulse magnitude", html_for="impulse_magnitude"),
                dbc.Input(id='impulse_magnitude', type="number", placeholder="Integer number between -50 and 50", min=-50, max=50),
            ]),

            dbc.Checklist(
                options=[{"label": "Cumulative impulse", "value": 0}],
                value=[], id="cumulative_impulse", switch=True,
            ),

            dbc.Checklist(
                options=[{"label": "Convergence to the forecast", "value": 0}],
                value=[], id="forecast_convergence", switch=True,
            ),

            html.Br(),
            dbc.Button("Apply impulse", color="primary", block=True, className="mr-1", id='apply_impulse_button', n_clicks=0),

            html.Br(),
            dbc.Button("Clear impulse", color="primary", block=True, className="mr-1", id='clear_button', n_clicks=0),

            html.Br(),
            html.H6(id='error_text', children=['']),

        ], className='test borde-right', md=3),

        # Gráfica principal
        dbc.Col([
            # Zoom year
            dbc.Row([
                dbc.Col([
                    dbc.FormGroup([
                        dbc.Label("Zoom graph by Year:", html_for="prediction_zoom_year"),
                        dcc.Dropdown(
                            id="prediction_zoom_year", value=years_projection[0], clearable=False,
                            options=[{"label": x, "value": x} for x in years_projection],
                        ),
                    ]),
                ], className='test', md=2),
            ], className='test'),

            # Gráfica principal
            dbc.Row([
                dbc.Col([
                    html.Div([ 
                        dcc.Graph(id='graph1', style={'height': '64vh'}, className='', figure=main_fig),
                        # html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),
                    ], className='test')
                ], className='test', md=12),
            ], className='test'),
        ], className='test', md=9),
    ], className='test'),
    
    dbc.Row([
        dbc.Col([ 
            html.Div([
                html.Br(),
                html.P('These are the indications to simulate shocks in the explanatory variables that affect future realizations of Energy Price:'),
                html.Div(
                    children=[
                        html.Ol(children=[
                            html.Li('Select the date the crash will occur.'),
                            html.Li('Select the model on which you want to see the price response to the shock.'),
                            html.Li('Select the variable that receives the shock and generates the impulse that will affect the price.'),
                            html.Li('Determine the magnitude of the shock which should be entered as a percentage. To see the effect of a 10% drop on a variable, enter -10.'),
                            html.Li('Define whether it is a cumulative impulse or not. A cumulative impulse is one in which the selected variable will receive the shock of the selected magnitude for 100 consecutive days.'),
                            html.Li('Determine if you want to simulate the crash with or without a return to the original forecast. A shock with no return to the original forecast is interpreted as a structural or long-term shock.'),
                        ])
                    ],
                ),
                html.P('Note that the different configuration between cumulative impulse or not, and shock with return to forecast or not, determine whether the shock is very short-term, short-term, long-term or structural, for example:'),

                html.Div(
                    children=[
                        html.Ul(children=[
                            html.Li('Non-cumulative impulse + return-to-forecast shock = very short-term shock.'),
                            html.Li('Non-cumulative impulse + shock with no return to forecast = long-term shock.'),
                            html.Li('Cumulative impulse + shock with return to forecast = medium-term shock.'),
                            html.Li('Cumulative impulse + shock with no return to forecast = long-term shock with structural change.'),
                        ])
                    ],
                ),

                html.P('Note that for cumulative shocks, the growth factor is accelerated since the shock is incorporated in 100 consecutive periods, therefore it is suggested to use values greater than -3 and less than 3, to obtain plausible results.'),

            ], className='test')
        ], className='test', md=12),
    ], className='test borde-top'),
], className="test tab-border")

tab3_content = html.Div([    
    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Availability, ')), 'Maximum amount of net power (expressed as a whole value in megawatts) that a generator can supply to the system during the time interval determined for economic dispatch or redispatch, reported by the company that owns the generator.']),], className='test', md=12),], className='test'),

    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Discharges, ')), 'are the amount of water that must be evacuated from reservoirs through spillways when the reservoir exceeds its maximum storage capacity, generally during rainy seasons. Spillways are a hydraulic structure built to allow free or controlled passage of water stored in a reservoir when high reservoir levels are reached.']),], className='test', md=12),], className='test'),
    
    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Energy stock price, ')), 'Under normal operating conditions, it corresponds to the highest offer price of the units with centralized dispatch that have been programmed to generate in the ideal dispatch and that do not present inflexibility. It represents a single price for the interconnected system in each hourly period. ']),], className='test', md=12),], className='test'),

    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Flow, ')), "is the amount of water contributed by one or more rivers to a reservoir of the National Interconnected System. The sum of all the country's flows is known as aggregate flow and is presented in Mm3, GWh and percentage."]),], className='test', md=12),], className='test'),

    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Inflows, ')), 'are the amount of water that reaches the reservoirs of the National Interconnected System. It is generally compared with the historical average of water received by the reservoirs for that same time of the year. It is obtained with the average of the values for each month for all the years with available information.']),], className='test', md=12),], className='test'),

    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Reserves, ')), 'are the total amount of water stored in the reservoirs.']),], className='test', md=12),], className='test'),

    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Reservoirs, ')), 'are an accumulation of water produced by the construction of a dam on the bed of a river or stream, which partially or totally closes its course.']),], className='test', md=12),], className='test'),

    dbc.Row([dbc.Col([
        html.P(children=[html.Strong(html.I('Usable volume, ')), 'is the available amount of the reserve that can be used for generation, since for technical reasons or reservoir construction specifications, not all the water contained in the reservoirs can be used for electricity generation. It is presented in Mm3, GWh and percentage and is what determines the capacity, which is the amount of energy that can be produced by each reservoir.']),], className='test', md=12),], className='test'),
    
], className="test tab-border")

layout_p2 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(tab1_content, label="Description"),
                dbc.Tab(tab2_content, label="Prediction"),
                dbc.Tab(tab3_content, label="Glossary"),
            ])
        ], className='test no-side-padding', id='hola', md=12),
    ], className='test card-box-border'),
])