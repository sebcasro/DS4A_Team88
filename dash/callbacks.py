import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from layouts import *
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

    fig = px.line(temp, x='Fecha', y=data_selection)
    return fig, fig, fig, fig

@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

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
    if pathname in ["/", "/page-1"]:
        return layout_p1

    elif pathname == "/page-2":
        return layout_p2

    elif pathname == "/page-3":
        return layout_p3

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )