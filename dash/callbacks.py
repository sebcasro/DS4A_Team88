import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from layout import *
from page_1 import layout_p1
from page_2 import layout_p2
from page_3 import layout_p3
from layout__dashboard__old import testing
from app import app

import plotly.express as px


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
@app.callback(
    Output("graph1_borrar", "figure"),
    Output("graph2_borrar", "figure"),
    Output("graph3_borrar", "figure"),
    Output("graph4_borrar", "figure"),    
    Input('data-start-1', 'date'))
def display_time_series(data_selection):
    # fig = px.line(df, x='Fecha', y=data_selection)

    data_selection = 'kW/h price daily mean'
    temp = df[['Date', data_selection]]
    temp = temp[temp[data_selection].notnull()]

    fig = px.line(
        temp, x='Date', y=data_selection,
        title="Receipts by Payer Gender and Day of Week")

    fig.update_layout( # customize font and legend orientation & position
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )
    return fig, fig, fig, fig
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output("graph4", "figure"),
    Input('temp_dropdown', 'value'))
def prediction(data_selection):
    # fig = px.line(df, x='Fecha', y=data_selection)

    data_selection = 'kW/h price daily mean'
    temp = df[['Date', data_selection]]
    temp = temp[temp[data_selection].notnull()]

    # :::::::::::::::::::::::

    fig1 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 1")

    fig1.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::

    fig2 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 2")

    fig2.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::

    fig3 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 3")

    fig3.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::

    fig4 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 4")

    fig4.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::

    return fig1, fig2, fig3, fig4

# --------------------------------------------------------------------------
@app.callback(
    Output("graph5", "figure"),
    Output("graph6", "figure"),
    Output("graph7", "figure"),
    Output("graph8", "figure"),
    Input('year_tab1', 'value'),
    Input('month_tab1', 'value'),
    Input('energy_type', 'value'))
def description_power_generated(year, month, data_selection):

    temp = df.copy()
    if year != 'All':
        temp = temp[temp['Year']==year]

    if month != 'All':
        temp = temp[temp['Month']==month]

    if data_selection == 'All':
        data_var = 'Total availability'
    elif data_selection == 'Hydraulic energy':
        data_var = 'Hydraulic availability'
    elif data_selection == 'Thermal energy':
        data_var = 'Thermal availability'
    elif data_selection == 'Solar energy':
        data_var = 'Solar availability'
    
    temp = temp[temp[data_var].fillna(0)!=0]

    temp2 = df.copy()
    temp2 = temp2.groupby(['Month2', 'Month'])['Total availability'].agg('sum')
    temp2 = temp2.reset_index().drop('Month2', axis = 1)
    
    # :::::::::::::::::::::::

    fig = px.line(df2, x="Date", y='Flow contribution (m3/s)', title="Wasa wasa 8")

    fig.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::

    fig5 = px.bar(temp2, x='Month', y='Total availability', title="Wasa wasa 5")

    # :::::::::::::::::::::::

    fig6 = px.bar(temp2, x='Month', y='Total availability', title="Wasa wasa 6")

    # :::::::::::::::::::::::

    fig7 = px.scatter(temp, x=data_var, y='kW/h price daily mean', title="Wasa wasa 7",
        trendline="ols", trendline_color_override="#ff516e"
    )

    fig7.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    fig7.update_traces(
        marker=dict(size=6, line=dict(width=1, color='#383648')),
        selector=dict(mode='markers')
    )

    # :::::::::::::::::::::::

    return fig5, fig6, fig7, fig

# --------------------------------------------------------------------------
@app.callback(
    Output("graph9", "figure"),
    Output("graph10", "figure"),
    Output("graph11", "figure"),
    Output("graph12", "figure"),
    Input('year_tab2', 'value'),
    Input('month_tab2', 'value'),
    Input('radio_input', 'value'))
def description_contribution(year, month, data_selection):

    temp = df.copy()
    if year != 'All':
        temp = temp[temp['Year']==year]

    if month != 'All':
        temp = temp[temp['Month']==month]

    if data_selection == 'm3/s':
        data_var = 'Flow contribution (m3/s)'
    else:
        data_var = 'Energy contribution (gWh)'

    # :::::::::::::::::::::::

    fig9 = px.scatter(    
        temp, x='Flow contribution (m3/s)', y='Energy contribution (gWh)', 
        title="Wasa wasa 9",
        trendline="ols", trendline_color_override="#ff516e"
    )

    fig9.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    fig9.update_traces(
        marker=dict(size=6, line=dict(width=1, color='#383648')),
        selector=dict(mode='markers')
    )

    # :::::::::::::::::::::::

    fig10 = px.box(
        temp, x='Month', y=data_var, color='Month',
        title="Wasa wasa 10")

    fig10.update_layout( # customize font and legend orientation & position
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575',
        showlegend=False
    )
    
    # :::::::::::::::::::::::

    fig11 = px.scatter(    
        temp, x=data_var, y='kW/h price daily mean', 
        title="Wasa wasa 11",
        trendline="ols", trendline_color_override="#ff516e"
    )

    fig11.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    fig11.update_traces(
        marker=dict(size=6, line=dict(width=1, color='#383648')),
        selector=dict(mode='markers')
    )

    # :::::::::::::::::::::::

    fig12 = px.line(
        temp, x="Date", y=data_var, 
        title='Wasa wasa 12'
    )

    fig12.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::

    return fig9, fig10, fig11, fig12

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

    elif pathname == "/test":
        return testing

    else:
        layout_pError = html.Div([
            dbc.Jumbotron([
                html.H1("404: Not found", className="text-danger"),
                html.P(f"The pathname {pathname} was not recognised.", className="lead",),
                html.Hr(className="my-2"),
                html.P("Click on the above button to return to the main page"),
                html.P(dbc.Button("Visit home page", color="primary", href="/"), className="lead"),
            ], className='white-background')
        ])

        return layout_pError

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

