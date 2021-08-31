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
import plotly.graph_objects as go


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# @app.callback(
#     Output("graph1_borrar", "figure"),
#     Output("graph2_borrar", "figure"),
#     Output("graph3_borrar", "figure"),
#     Output("graph4_borrar", "figure"),    
#     Input('data-start-1', 'date'))
# def display_time_series(data_selection):
#     # fig = px.line(df, x='Fecha', y=data_selection)

#     data_selection = 'kW/h price daily mean'
#     temp = df[['Date', data_selection]]
#     temp = temp[temp[data_selection].notnull()]

#     fig = px.line(
#         temp, x='Date', y=data_selection,
#         title="Receipts by Payer Gender and Day of Week")

#     fig.update_layout( # customize font and legend orientation & position
#         # font_family="Rockwell",
#         margin=dict(l=80, r=20, t=75, b=20),
#         font_color='#757575'
#     )

#     return fig, fig, fig, fig
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Output("graph2", "figure"),
# Output("graph3", "figure"),
# Output("graph4", "figure"),

@app.callback(
    Output("graph1", "figure"),    
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

    # fig2 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 2")

    # fig2.update_layout(
    #     # font_family="Rockwell",
    #     margin=dict(l=80, r=20, t=75, b=20),
    #     font_color='#757575'
    # )

    # :::::::::::::::::::::::

    # fig3 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 3")

    # fig3.update_layout(
    #     # font_family="Rockwell",
    #     margin=dict(l=80, r=20, t=75, b=20),
    #     font_color='#757575'
    # )

    # :::::::::::::::::::::::

    # fig4 = px.line(temp, x='Date', y=data_selection, title="Wasa wasa 4")

    # fig4.update_layout(
    #     # font_family="Rockwell",
    #     margin=dict(l=80, r=20, t=75, b=20),
    #     font_color='#757575'
    # )

    # :::::::::::::::::::::::
    del temp
    return fig1 #, fig2, fig3, fig4

# --------------------------------------------------------------------------
@app.callback(
    Output("graph5", "figure"),
    Output("graph6", "figure"),
    Output("graph7", "figure"),
    Output("graph8", "figure"),
    Output("graph5_description", "children"),
    Output("graph6_description", "children"),
    Input('year_tab1', 'value'),
    Input('month_tab1', 'value'),
    Input('energy_type', 'value'),
    Input('graph5_switch', 'value'),
    Input('graph6_switch', 'value'))
def description_power_generated(year, month, data_selection, graph5_switch, graph6_switch):
    
    temp = df.copy()
    prom_diario_temp = prom_diario.copy()
    prom_diario_real_temp = prom_diario_real.copy()

    graph5_switch = len(graph5_switch)
    graph6_switch = len(graph6_switch)

    if year != 'All':
        temp = temp[temp['Year']==year]
        prom_diario_temp = prom_diario_temp[prom_diario_temp['Year']==year]        
        prom_diario_real_temp = prom_diario_real_temp[prom_diario_real_temp['Year']==year]        

    if month != 'All':
        temp = temp[temp['Month']==month]
        prom_diario_temp = prom_diario_temp[prom_diario_temp['Month2']==month]
        prom_diario_real_temp = prom_diario_real_temp[prom_diario_real_temp['Month2']==month]

    if data_selection == 'All':
        data_var = 'Total availability'
        energy_type_filter='All'
    elif data_selection == 'Hydraulic energy':
        data_var = 'Hydraulic availability'
        energy_type_filter='HIDRAULICA'
    elif data_selection == 'Thermal energy':
        data_var = 'Thermal availability'
        energy_type_filter='TERMICA'
    elif data_selection == 'Solar energy':
        data_var = 'Solar availability'
        energy_type_filter='SOLAR'

    temp = temp[temp[data_var].fillna(0)!=0]
    if energy_type_filter!='All':
        prom_diario_real_temp=prom_diario_real_temp[prom_diario_real_temp['Energy type']==energy_type_filter]

    temp2 = df.copy()
    temp2 = temp2.groupby(['Month2', 'Month'])['Total availability'].agg('sum')
    temp2 = temp2.reset_index().drop('Month2', axis = 1)
    
    annual_production=prom_diario_temp.groupby(["Year"]).mean().reset_index()
    monthly_production=prom_diario_temp.groupby(["Month"]).mean().reset_index()

    annual_production_real=prom_diario_real_temp.groupby(["Year"]).sum().reset_index()
    monthly_production_real=prom_diario_real_temp.groupby(["Month"]).sum().reset_index()

    # :::::::::::::::::::::::

    if graph5_switch==0:
        fig5 = px.bar(annual_production, x="Year", y="Total power generation", title="Average percentage of energy generated by year (All energy types)")
        fig5.update_layout(
            xaxis = dict(tickmode = 'linear'),
            margin=dict(l=80, r=20, t=75, b=20),
            font_color='#757575')
        fig5.update_yaxes(range=[60,100])

        graph5_description=[
            'On this ',
            dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
            ' we can see the average percentage of energy produced concerning the maximum capacity of production by year.', 
        ]
    else:
        fig5 = px.bar(monthly_production, x="Month", y="Total power generation", title="Average percentage of energy generated by month (All energy types)")
        fig5.update_layout(xaxis = dict(
            tickmode = 'array', 
            tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
            ticktext = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
            margin=dict(l=80, r=20, t=75, b=20),
            font_color='#757575'
        )
        fig5.update_yaxes(range=[60,100])

        graph5_description=[
            'On this ',
            dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
            ' we can see the average percentage of energy produced concerning the maximum capacity of production by month.', 
        ]    

    # :::::::::::::::::::::::

    if graph6_switch==0:
        if energy_type_filter=='All':
            titulo='Total energy generated by year'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of total energy generated on GW, year over year in Colombia.']
        elif energy_type_filter=='HIDRAULICA':
            titulo='Total energy generated by hydraulic source yearly'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of hydraulic energy generated on GW, year over year in Colombia.']
        elif energy_type_filter=='TERMICA':
            titulo='Total energy generated by thermal source yearly'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of thermal energy generated on GW, year over year in Colombia.']
        elif energy_type_filter=='SOLAR':
            titulo='Total energy generated by solar source yearly'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of solar energy generated on GW, year over year in Colombia.']

        fig6 = px.bar(annual_production_real, x="Year", y="Total energy generated GW", title=titulo)
        fig6.update_layout(
            xaxis = dict(tickmode = 'linear'),
            margin=dict(l=80, r=20, t=75, b=20),
            font_color='#757575')        

    else:
        if energy_type_filter=='All':
            titulo='Total energy generated by month'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of total energy generated on GW, month over month in Colombia.']
        elif energy_type_filter=='HIDRAULICA':
            titulo='Total energy generated by hydraulic source monthly'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of energy generated by hydroplants on GW, month over month in Colombia.']
        elif energy_type_filter=='TERMICA':
            titulo='Total energy generated by thermal source monthly'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of energy generated by thermal plants on GW, month over month in Colombia.']
        elif energy_type_filter=='SOLAR':
            titulo='Total energy generated by solar source monthly'
            graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                ', we can see the evolution of energy generated by solar plants on GW, month over month in Colombia.']

        fig6 = px.bar(monthly_production_real, x="Month", y="Total energy generated GW", title=titulo)
        fig6.update_layout(xaxis = dict(
            tickmode = 'array', 
            tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
            ticktext = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
            margin=dict(l=80, r=20, t=75, b=20),
            font_color='#757575'
        )        

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

    dark_gray = '#383648'
    rowEvenColor = '#e2e2e2'
    rowOddColor = 'white'

    table_data=prom_diario_real_temp.groupby(['Company', "Energy type"])["Total energy generated GW"].sum().reset_index().sort_values("Total energy generated GW", ascending=False)
    table_data["Total energy generated GW"] = table_data["Total energy generated GW"].astype(int)
    table_data['Total energy generated GW'] = table_data['Total energy generated GW'].astype(str).str.replace(r"(?!^)(?=(?:\d{3})+$)", ".")
    table_data = table_data.reset_index(drop=True).reset_index()
    table_data['index']=table_data['index']+1
    table_data.rename(columns={'index':'Ranking'}, inplace=True)

    fig8 = go.Figure(data=[go.Table(
        header=dict(
            values=list(table_data.columns),
            line_color=dark_gray,
            font=dict(color='white', size=14),
            fill_color=dark_gray,
        ),
        cells=dict(
            values=[table_data['Ranking'], table_data['Company'], table_data['Energy type'], table_data['Total energy generated GW']],
            line_color=dark_gray,
            font = dict(color = dark_gray, size=12),
            fill_color = [[rowOddColor, rowEvenColor]*200],
        )
    )])

    # :::::::::::::::::::::::
    del temp, prom_diario_temp, prom_diario_real_temp
    return fig5, fig6, fig7, fig8, graph5_description, graph6_description

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
        title="Scatterplot between flow contribution vs energy contribution",
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
        title='Boxplot of the flow contribution ("energy contribution") by month')

    fig10.update_layout( # customize font and legend orientation & position
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575',
        showlegend=False
    )
    
    # :::::::::::::::::::::::

    fig11 = px.scatter(    
        temp, x=data_var, y='kW/h price daily mean', 
        title='Scatterplot between flow contribution ("energy contribution") with the energy price',
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
        title='Time serie of flow contribution ("energy contribution")'
    )

    fig12.update_layout(
        # font_family="Rockwell",
        margin=dict(l=80, r=20, t=75, b=20),
        font_color='#757575'
    )

    # :::::::::::::::::::::::
    del temp
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

