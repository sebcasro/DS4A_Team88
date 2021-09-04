import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout_p1 = html.Div([
    dbc.Row([

        dbc.Col([ html.Img(src='/assets/images/map.png', id='map') ], className='test', id='container-map', md=4),
        dbc.Col([ 
            
            dbc.Row([
                dbc.Col([ 
                    html.Img(src='/assets/images/logo_mintic.png', id='logo_mintic'),
                    html.Img(src='/assets/images/logo_ds4a.png', id='logo_ds4a')
                ], className='test container-logos', md=12),
            ], className='test'),

            dbc.Row([
                dbc.Col([ html.H2("KWH PRICE PREDICTION IN THE COLOMBIAN ENERGY MARKET") ], className='test', id='container-title', md=12),
            ], className='test'),

            dbc.Row([
                dbc.Col([ 
                    html.H4("Project description"),
                    html.P('In order to implement self-generation and distributed generation projects, it is necessary, among other things, to carry out an economic study to evaluate and verify their viability. In order to achieve this in a more accurate way, it is very useful to know in advance the price of the energy offered in the electricity system. So that, supply energy price prediction will improve financial evaluation of self-generation energy and distributing projects. This information can foster renewable energy projects and make it more attractive to investors in a country where there is a high potential and needs incentives to make it real.'),
                    html.P('The formation of the energy price in the market considers a large number and variety of variables of the electricity system, factors as composition of the generating capacity, climate, oil prices, demand, technical restrictions, among others. Therefore, the energy price is one of the most volatile commodities in world markets. However, the prediction of the energy price was approached through the energy market price, a market variable that, according to experience, reflects the energy price volatility and its data is more accessible for public access.'),
                    html.P('The data used to prediction include energy data such as generation availability, as well as information about pricing and vendors and weather-related reservoir data, as the main energy source in Colombia is hydroelectric power plants. The above data set is obtained from Portal Bi of XM, which is the sole operator of the electric power grid.'),
                    html.P('With the above in mind, you will find here in a descriptive way the data used to perform the forecast, and in a second instance the result of an algorithm based on artificial intelligence capable of making a prediction of the energy market price.'),

                    # html.P('Duis at finibus est, non tempus justo. Donec vestibulum iaculis semper. Sed quis leo convallis, venenatis ante et, elementum erat. Etiam libero risus, commodo sit amet molestie at, placerat facilisis lectus. Morbi ultrices accumsan est a luctus. Donec congue a arcu in gravida. Curabitur non velit malesuada, elementum turpis in, auctor mi. Nulla facilisi. Phasellus nec mi a ipsum sagittis semper ac in magna. Nulla vitae congue quam, id efficitur nunc. Vestibulum eget consectetur libero, eget vehicula odio.')
                ], className='test', id='project_description', md=12),
            ], className='test'),

            dbc.Row([

                dbc.Col([
                    html.Div([
                        dcc.Link(html.I(className="fas fa-desktop link-icon"), href='/dashboard'),
                        dcc.Link('Access application', href='/dashboard', className='link-text')
                    ], className='test link-container'),
                ], className='test', md=3),

                dbc.Col([
                    html.Div([
                        dcc.Link(html.I(className="fab fa-youtube link-icon"), href='https://www.youtube.com/watch?v=q3agHEjSOUM', target='_blank'),
                        dcc.Link('Watch video', href='https://www.youtube.com/watch?v=q3agHEjSOUM', target='_blank', className='link-text')
                    ], className='test link-container'),
                ], className='test', md=3),

                dbc.Col([
                    html.Div([
                        dcc.Link(html.I(className="fab fa-github link-icon"), href='https://github.com/sebcasro/DS4A_Team88', target='_blank'),
                        dcc.Link('Access Code', href='https://github.com/sebcasro/DS4A_Team88', target='_blank', className='link-text') 
                    ], className='test link-container'),
                ], className='test', md=3),

                dbc.Col([
                    html.Div([
                        dcc.Link(html.I(className="fas fa-users link-icon"), href='/about-us'),
                        dcc.Link('About us', href='/about-us', className='link-text') 
                    ], className='test link-container'),
                ], className='test', md=3),

            ], className='test seccion_links'),
        ], className='test home_text', md=8),
    ], className='box-shadow2 test'),
])