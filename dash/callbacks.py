import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from layout import *
from page_1 import layout_p1
from page_2 import layout_p2
from page_3 import layout_p3
from app import app

import plotly.express as px

@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output("graph4", "figure"),
    Input("data_selection", "value"))
def display_time_series(data_selection):
    # fig = px.line(df, x='Fecha', y=data_selection)

    temp = df[['Fecha', data_selection]]
    temp = temp[temp[data_selection].notnull()]

    fig = px.line(
        temp, x='Fecha', y=data_selection,
        title="Receipts by Payer Gender and Day of Week")

    fig.update_layout( # customize font and legend orientation & position
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )
    return fig, fig, fig, fig

# @app.callback(
#     [
#         Output("sidebar", "style"),
#         Output("page-content", "style"),
#         Output("side_click", "data"),
#     ],

#     [Input("btn_sidebar", "n_clicks")],
#     [
#         State("side_click", "data"),
#     ]
# )
# def toggle_sidebar(n, nclick):
#     if n:
#         if nclick == "SHOW":
#             sidebar_style = SIDEBAR_HIDEN
#             content_style = CONTENT_STYLE_NO_SIDEBAR
#             cur_nclick = "HIDDEN"
#         else:
#             sidebar_style = SIDEBAR_STYLE
#             content_style = CONTENT_STYLE_SIDEBAR
#             cur_nclick = "SHOW"
#     else:
#         sidebar_style = SIDEBAR_STYLE
#         content_style = CONTENT_STYLE_SIDEBAR
#         cur_nclick = 'SHOW'

#     return sidebar_style, content_style, cur_nclick

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return layout_p1

    elif pathname == "/dashboard":
        return layout_p2

    elif pathname == "/about-us":
        return layout_p3

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# callback del procentaje
# @app.callback(
#     Output('numeric-input-output', 'children'),
#     Input('my-numeric-input', 'value')
# )
# def update_output(value):
#     return 'The value is {}.'.format(value)

# @app.callback(
#     Output('output-container-date-picker-range', 'children'),
#     Input('date-range-1', 'start_date'),
#     Input('date-range-1', 'end_date'))
# def update_output(start_date, end_date):
#     string_prefix = 'You have selected: '
#     if start_date is not None:
#         start_date_object = date.fromisoformat(start_date)
#         start_date_string = start_date_object.strftime('%B %d, %Y')
#         string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
#     if end_date is not None:
#         end_date_object = date.fromisoformat(end_date)
#         end_date_string = end_date_object.strftime('%B %d, %Y')
#         string_prefix = string_prefix + 'End Date: ' + end_date_string
#     if len(string_prefix) == len('You have selected: '):
#         return 'Select a date to see it displayed here'
#     else:
#         return string_prefix