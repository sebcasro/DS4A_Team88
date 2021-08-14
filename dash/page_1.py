import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import dash_daq as daq

# from datetime import date
# from layout import *

layout_p1 = html.Div([

    dbc.Row([

        dbc.Col([ html.Img(src='/assets/images/map.png', id='map') ], className='test', id='container-map', md=5),
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
                    html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus elit dui, ultrices nec quam vitae, eleifend congue risus. Donec sed neque at nisi malesuada elementum. Curabitur non odio aliquet, maximus diam ut, iaculis nunc. Cras vel ornare dui. Integer et neque vitae magna ultrices rhoncus molestie sed augue. Suspendisse condimentum purus vel purus maximus ultrices. Mauris consectetur tortor orci, quis ultricies felis eleifend aliquet. Nulla massa neque, mattis at vehicula aliquam, eleifend sed augue. Ut posuere tristique massa quis semper. Pellentesque vitae dapibus neque. Pellentesque id eleifend metus, sit amet lacinia ex. Donec malesuada viverra magna a rutrum. Suspendisse potenti.'),

                    html.P('Quisque varius, eros eu facilisis lacinia, leo erat ornare magna, sit amet imperdiet metus lacus sit amet dui. Fusce eu porttitor enim, ut pellentesque tellus. Nunc ac egestas enim, finibus feugiat est. Morbi ac magna ex. Cras in egestas ligula. Etiam ornare convallis libero rhoncus vestibulum. Cras finibus sagittis sem, non ultrices neque placerat eget. Donec eu lacus commodo, mattis lorem at, finibus nulla.'),

                    html.P('Praesent ac erat metus. Curabitur euismod nisl risus, sodales malesuada erat sollicitudin eu. Proin vestibulum aliquam risus ullamcorper cursus. In aliquet mauris arcu, a aliquet diam facilisis sed. Maecenas ut ullamcorper odio. Duis vestibulum ipsum quis massa pharetra, a aliquam tellus cursus. Nunc tempor vulputate faucibus. Aenean tincidunt eros ipsum, fermentum vehicula nisi posuere vehicula. Sed vel nunc in nulla porttitor aliquet. Aliquam eu nulla rhoncus, faucibus lectus dignissim, tristique eros. Proin eu elit id tortor laoreet tincidunt quis sed felis. Ut laoreet in elit non ultricies. Quisque ut ipsum vitae neque tempor pharetra ut nec ligula.'),

                    # html.P('Duis at finibus est, non tempus justo. Donec vestibulum iaculis semper. Sed quis leo convallis, venenatis ante et, elementum erat. Etiam libero risus, commodo sit amet molestie at, placerat facilisis lectus. Morbi ultrices accumsan est a luctus. Donec congue a arcu in gravida. Curabitur non velit malesuada, elementum turpis in, auctor mi. Nulla facilisi. Phasellus nec mi a ipsum sagittis semper ac in magna. Nulla vitae congue quam, id efficitur nunc. Vestibulum eget consectetur libero, eget vehicula odio.')
                ], className='test', id='project_description', md=12),
            ], className='test'),
        
            dbc.Row([
                dbc.Col([ dcc.Link('Access application', href='/dashboard') ], className='test', md=4),
                dbc.Col([ dcc.Link('About us', href='/about-us') ], className='test', md=4),
            ], className='test seccion_links'),
        ], className='test home_text', md=7),

    ], className='box-shadow2 test'),
])