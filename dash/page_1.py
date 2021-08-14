import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import dash_daq as daq

# from datetime import date
# from layout import *

layout_p1 = html.Div([

    dbc.Row([

        dbc.Col([ html.Span("Imagen mapa") ], className='test', md=6),
        dbc.Col([ 
            
            dbc.Row([
                dbc.Col([ html.Span("Espacio vacío") ], className='test', md=4),
                dbc.Col([ html.Span("Logo DS4A") ], className='test', md=4),
                dbc.Col([ html.Span("Logo MinTIC") ], className='test', md=4),
            ], className='test'),

            dbc.Row([
                dbc.Col([ html.H2("Título") ], className='test', md=12),
            ], className='test'),

            dbc.Row([
                dbc.Col([ 
                    html.H4("Project description"),
                    html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit sed eros vel suscipit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis euismod, justo id ultrices eleifend, sem velit bibendum enim, at luctus orci elit in sapien. Pellentesque non mi sed nulla feugiat venenatis. Curabitur et posuere lacus. Integer finibus laoreet placerat. Mauris ut pellentesque nisi, in feugiat mauris.'),

                    html.P('Suspendisse finibus nunc at risus hendrerit, eget facilisis elit sollicitudin. Etiam fermentum egestas nulla, convallis vehicula nisi vestibulum at. In sit amet viverra turpis. Cras auctor, tellus et accumsan semper, orci quam interdum nisi, et porttitor ante nibh vel nunc. Nullam auctor accumsan pulvinar. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla non mauris id tellus fringilla ultrices. Vivamus efficitur in erat nec aliquam. Donec fermentum feugiat lectus. Nunc nec neque ac nunc malesuada placerat quis sodales erat. In commodo, enim in vehicula maximus, purus elit pretium sapien, a maximus tellus ex sit amet odio. Sed sollicitudin, metus vel tristique blandit, dolor sapien mollis velit, sed fermentum turpis nisi vitae ligula. Pellentesque et rutrum sem. Curabitur nisl urna, vulputate vel mi tincidunt, hendrerit elementum magna. Pellentesque cursus risus nisl, quis lobortis neque pellentesque nec.')
                ], className='test', md=12),
            ], className='test'),
        
            dbc.Row([
                dbc.Col([ dcc.Link('Access application', href='/dashboard') ], className='test', md=6),
                dbc.Col([ dcc.Link('About us', href='/about-us') ], className='test', md=6),
            ], className='test seccion_links'),
        ], className='test', md=6),

    ], className='box-shadow test'),
])