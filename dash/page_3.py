# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout_p3 = html.Div([
    dbc.Row([
        dbc.Col([ html.H2("About us - Team 88") ], className='test', id='container-title', md=12),
        
        dbc.Col([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Carlos de Oro Aguado", className="card-title"),
                        html.H6("Statistics teacher, UniNorte", className="card-subtitle"),
                        html.Hr(),
                        html.P("Mathematic with master degree of mathematics and applied statistics." ,className="card-text"),
                        dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/cdeoroaguado/", external_link =True, target="_blank"),
                        # dbc.CardLink("Link 2", href="#", external_link =True, target="_blank"),
                    ]), #style={"min-height": "18rem"},
                ]),
            ], className='about-us-card-div'),
        ], className='test', md=4),

        dbc.Col([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("David Enrique Zambrano Higuera", className="card-title"),
                        html.H6("Assistant Manager, STS", className="card-subtitle"),
                        html.Hr(),
                        html.P("Bachelor of Science in Economics with a Master of Arts in Finance and a Master of Science in Economics." ,className="card-text"),
                        dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/david-enrique-zambrano-a753a764/", external_link =True, target="_blank"),
                        dbc.CardLink("GitHub", href="https://github.com/econdavidzh", external_link =True, target="_blank"),
                    ]), #style={"min-height": "18rem"},
                ]),
            ], className='about-us-card-div'),
        ], className='test', md=4),

        dbc.Col([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Jairo Ruiz Saenz", className="card-title"),
                        html.H6("Data Scientist, DNP", className="card-subtitle"),
                        html.Hr(),
                        html.P("Bachelor of Science in Industrial Engineering with a Master degree of Information Engineering." ,className="card-text"),
                        dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/jairoruizsaenz/", external_link =True, target="_blank"),
                        dbc.CardLink("GitHub", href="https://github.com/jairoruizsaenz", external_link =True, target="_blank"),
                    ]), #style={"min-height": "18rem"},
                ]),
            ], className='about-us-card-div'),
        ], className='test', md=4),

        dbc.Col([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Juan Sebastian Castro Rodriguez", className="card-title"),
                        html.H6("Financial Analyst", className="card-subtitle"),
                        html.Hr(),
                        html.P("Bachelor of Science in Mathematics and Master candidate on Quantitative Economics." ,className="card-text"),
                        dbc.CardLink("LinkedIn", href="https://www.linkedin.com/in/juan-sebastian-castro-rodriguez-69576420b/", external_link =True, target="_blank"),                        
                    ]), #style={"min-height": "18rem"},
                ]),
            ], className='about-us-card-div'),
        ], className='test', md=4),

        dbc.Col([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Pedro José Díaz Rojas", className="card-title"),
                        html.H6("Mechanical and Electrical Engineer", className="card-subtitle"),
                        html.Hr(),
                        html.P("Bachelor of Science in Mechanical and Electrical Engineer and Msc. Student of Master in Electrical Engineering." ,className="card-text"),
                        # dbc.CardLink("Link 1", href="#", external_link =True, target="_blank"),
                        # dbc.CardLink("Link 2", href="#", external_link =True, target="_blank"),
                    ]), #style={"min-height": "18rem"},
                ]),
            ], className='about-us-card-div'),
        ], className='test', md=4),
        
    ], className='test'),
])