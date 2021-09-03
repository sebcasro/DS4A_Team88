import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from layout import *
from page_1 import layout_p1
from page_2 import layout_p2
from page_3 import layout_p3

from app import app
from projection import *

import plotly.express as px
import plotly.graph_objects as go

import visdcc

@app.callback(
    Output("graph1", "figure"),
    Output("error_text", "children"),
    Output('impulse_date', 'date'),
    Output('forecasting_model', 'value'),
    Output('variable_shocked', 'value'),
    Output('impulse_magnitude', 'value'),
    Output('cumulative_impulse', 'value'),
    Output('forecast_convergence', 'value'),
    Input("graph1", "figure"),
    Input('prediction_zoom_year', 'value'),
    Input("error_text", "children"),
    Input('impulse_date', 'date'),
    Input('forecasting_model', 'value'),
    Input('variable_shocked', 'value'),
    Input('impulse_magnitude', 'value'),
    Input('cumulative_impulse', 'value'),
    Input('forecast_convergence', 'value'),
    Input("apply_impulse_button", "n_clicks"),
    Input("clear_button", "n_clicks"),
)
def impulse(fig1, zoom_year, error_text, impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence, n_click_apply, n_click_clear):
    try:
        projection_df_temp = ''
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

        cumulative_impulse_2 = len(cumulative_impulse)
        forecast_convergence_2 = len(forecast_convergence)

        # cambio en la selección del zoom
        if 'prediction_zoom_year' in changed_id:
            projection_df_temp = projection_df.copy()
            if zoom_year != 'All':
                projection_df_temp = projection_df_temp[projection_df_temp['Year']>=zoom_year]
            
            fig1 = px.line(projection_df_temp, x="Date", y="value", color='model', title="kW/h price forecasting")

            fig1.update_layout(
                # font_family="Rockwell",
                margin=dict(l=60, r=0, t=50, b=70),
                font_color='#757575'
            )

        # click clear_button
        if 'clear_button' in changed_id:
            projection_df_temp = projection_df.copy()
            if zoom_year != 'All':
                projection_df_temp = projection_df_temp[projection_df_temp['Year']>=zoom_year]
            
            fig1 = px.line(projection_df_temp, x="Date", y="value", color='model', title="kW/h price forecasting")

            fig1.update_layout(
                # font_family="Rockwell",
                margin=dict(l=60, r=0, t=50, b=70),
                font_color='#757575'
            )

            return fig1, '', None, 0, 0, None, [], []

        # click apply_impulse_button
        if 'apply_impulse_button' in changed_id:
            
            projection_df_temp = projection_df.copy()
            if zoom_year != 'All':
                projection_df_temp = projection_df_temp[projection_df_temp['Year']>=zoom_year]

            # Error messages :::::::::::::::::::::::::::::::::::::::::::::
            if impulse_date is None:
                del projection_df_temp
                return fig1, "Error: you need to pick an impulse input date.", impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence

            if forecasting_model == 0:
                del projection_df_temp
                return fig1, "Error: you need to select a forecasting model.", impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence

            if variable_shocked == 0:
                del projection_df_temp
                return fig1, "Error: you need to select a variable to affect.", impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence

            if impulse_magnitude is None:
                del projection_df_temp
                return fig1, "Error: (Impulse magnitude) you need to write a number between -50 and 50.", impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence

            if (impulse_magnitude < -50) or (impulse_magnitude > 50):
                del projection_df_temp                
                return fig1, "Error: (Impulse magnitude) you need to write a number between -50 and 50.", impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence
            # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

            forecasting_model_2 = f'kW/h price {forecasting_model}'
            
            # cumulative_impulse: off
            if cumulative_impulse_2 == 0:
                if variable_shocked == 'Hydraulic availability':
                    variable_shocked_2 = 'HYDRAULIC_availability'
                elif variable_shocked == 'Thermal availability':
                    variable_shocked_2 = 'THERMAL_availability'
                elif variable_shocked == 'Flow contribution':
                    variable_shocked_2 = 'flow_contribution'
                elif variable_shocked == 'Daily volume (Mm3)':
                    variable_shocked_2 = 'daily_volume_(Mm3)'
                elif variable_shocked == 'Volume (Mm3)':
                    variable_shocked_2 = 'Volume_(Mm3)'
                elif variable_shocked == 'Daily useful Volume (gWh)':
                    variable_shocked_2 = 'Daily_useful_Volume_(gWh)'

            else:
            # cumulative_impulse: on
                if variable_shocked == 'Hydraulic availability':
                    variable_shocked_2 = 'Cumulative_HYDRAULIC availability'
                elif variable_shocked == 'Thermal availability':
                    variable_shocked_2 = 'Cumulative_THERMAL availability'
                elif variable_shocked == 'Flow contribution':
                    variable_shocked_2 = 'Cumulative_flow_contribution'
                elif variable_shocked == 'Daily volume (Mm3)':
                    variable_shocked_2 = 'Cumulative_daily_volume_(Mm3)'
                elif variable_shocked == 'Volume (Mm3)':
                    variable_shocked_2 = 'Cumulative_Volume_(Mm3)'
                elif variable_shocked == 'Daily useful Volume (gWh)':
                    variable_shocked_2 = 'Cumulative_Daily_useful_Volume_(gWh)'

            # forecast_convergence: off
            if forecast_convergence_2 == 0:

                data=original_level_after_shock(impulse_date, forecasting_model_2, variable_shocked_2, factor_de_expansion(variable_shocked_2,impulse_magnitude))

                # Create traces
                fig1 = None
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(
                    x=projection_df_temp[projection_df_temp['model']=='kW/h price mean'].Date, 
                    y=projection_df_temp[projection_df_temp['model']=='kW/h price mean'].value, 
                    mode='lines', name='actual price'))

                fig1.add_trace(go.Scatter(
                    x=projection_df_temp[projection_df_temp['model']==forecasting_model_2].Date, 
                    y=projection_df_temp[projection_df_temp['model']==forecasting_model_2].value, 
                    mode='lines', name='model forecast'))

                fig1.add_trace(go.Scatter(
                    x=data[list(data)[0]].index, 
                    y=data[list(data)[0]].values, 
                    mode='lines', name=list(data)[0]))

                fig1.update_layout(
                    title=f"kW/h price forecasting - Impulse into {variable_shocked}",
                    xaxis_title="Date",
                    yaxis_title="Value",
                    legend_title="model",
                    margin=dict(l=60, r=0, t=50, b=70),
                    font_color='#757575'
                )

            else:

                data=original_level_after_shock_convergencia(impulse_date, forecasting_model_2, variable_shocked_2, factor_de_expansion(variable_shocked_2,impulse_magnitude))

                # Create traces
                fig1 = None
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(
                    x=projection_df_temp[projection_df_temp['model']=='kW/h price mean'].Date, 
                    y=projection_df_temp[projection_df_temp['model']=='kW/h price mean'].value, 
                    mode='lines', name='actual price'))

                fig1.add_trace(go.Scatter(
                    x=projection_df_temp[projection_df_temp['model']==forecasting_model_2].Date, 
                    y=projection_df_temp[projection_df_temp['model']==forecasting_model_2].value, 
                    mode='lines', name='model forecast'))

                fig1.add_trace(go.Scatter(
                    x=data[list(data)[0]].index, 
                    y=data[list(data)[0]].values, 
                    mode='lines', name=list(data)[0]))

                fig1.update_layout(
                    title=f"kW/h price forecasting - Impulse into {variable_shocked}",
                    xaxis_title="Date",
                    yaxis_title="Value",
                    legend_title="model",
                    margin=dict(l=60, r=0, t=50, b=70),
                    font_color='#757575'
                )
            
            del projection_df_temp
            return fig1, '', impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence
        
        del projection_df_temp
        return fig1, error_text, impulse_date, forecasting_model, variable_shocked, impulse_magnitude, cumulative_impulse, forecast_convergence
    
    except:        
        visdcc.Run_js(id='javascript', run="location.reload();")
        # print('Error')

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
    try:    
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
            # energy_type_filter='HIDRAULICA'
            energy_type_filter='Hydraulic'
        elif data_selection == 'Thermal energy':
            data_var = 'Thermal availability'
            # energy_type_filter='TERMICA'
            energy_type_filter='Thermal'
        elif data_selection == 'Solar energy':
            data_var = 'Solar availability'
            # energy_type_filter='SOLAR'
            energy_type_filter='Solar'

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
                margin=dict(l=80, r=0, t=50, b=20),
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
                margin=dict(l=80, r=0, t=50, b=20),
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

            elif energy_type_filter=='Hydraulic':
                titulo='Total energy generated by hydraulic source yearly'
                graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                    ', we can see the evolution of hydraulic energy generated on GW, year over year in Colombia.']

            elif energy_type_filter=='Thermal':
                titulo='Total energy generated by thermal source yearly'
                graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                    ', we can see the evolution of thermal energy generated on GW, year over year in Colombia.']

            elif energy_type_filter=='Solar':
                titulo='Total energy generated by solar source yearly'
                graph6_description=['On this ', dcc.Link('bar chart', href='https://en.wikipedia.org/wiki/Bar_chart', target='_blank'),
                    ', we can see the evolution of solar energy generated on GW, year over year in Colombia.']

            fig6 = px.bar(annual_production_real, x="Year", y="Total energy generated GW", title=titulo)
            fig6.update_layout(
                xaxis = dict(tickmode = 'linear'),
                margin=dict(l=80, r=0, t=50, b=20),
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
                margin=dict(l=80, r=0, t=50, b=20),
                font_color='#757575'
            )        

        # :::::::::::::::::::::::

        fig7 = px.scatter(temp, x=data_var, y='kW/h price daily mean', title="Scatterplot between total availability with the energy price",
            trendline="ols", trendline_color_override="#ff516e"
        )

        fig7.update_layout(
            # font_family="Rockwell",
            margin=dict(l=80, r=0, t=50, b=20),
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

        fig8.update_layout(
            title="Maximum total power generators by resource and generation type", 
            font_color='#757575',
            margin=dict(l=10, r=10, t=50, b=20)
        )

        # :::::::::::::::::::::::
        del temp, prom_diario_temp, prom_diario_real_temp
        return fig5, fig6, fig7, fig8, graph5_description, graph6_description

    except:        
        visdcc.Run_js(id='javascript', run="location.reload();")
        # print('Error')

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
    try:
        temp = df.copy()
        if year != 'All':
            temp = temp[temp['Year']==year]

        if month != 'All':
            temp = temp[temp['Month']==month]

        if data_selection == 'm3/s':
            data_var = 'Flow contribution (m3/s)'
            fig9_title = 'Scatterplot between flow contribution vs energy contribution'
            fig10_title = 'Boxplot of the flow contribution by month'
            fig11_title = 'Scatterplot between the flow contribution with the energy price'
            fig12_title = 'Time serie of flow contribution '
        else:
            data_var = 'Energy contribution (gWh)'
            fig9_title = 'Scatterplot between flow contribution vs energy contribution'
            fig10_title = 'Boxplot of the energy contribution by month description'
            fig11_title = 'Scatterplot between the energy contribution with the energy price'
            fig12_title = 'Time serie of energy contribution'

        # :::::::::::::::::::::::

        fig9 = px.scatter(    
            temp, x='Flow contribution (m3/s)', y='Energy contribution (gWh)', 
            title=fig9_title,
            trendline="ols", trendline_color_override="#ff516e"
        )

        fig9.update_layout(
            # font_family="Rockwell",
            margin=dict(l=80, r=0, t=50, b=20),
            font_color='#757575'
        )

        fig9.update_traces(
            marker=dict(size=6, line=dict(width=1, color='#383648')),
            selector=dict(mode='markers')
        )

        # :::::::::::::::::::::::

        fig10 = px.box(
            temp, x='Month', y=data_var, color='Month',
            title=fig10_title)

        fig10.update_layout( # customize font and legend orientation & position
            # font_family="Rockwell",
            margin=dict(l=80, r=0, t=50, b=20),
            font_color='#757575',
            showlegend=False
        )
        
        # :::::::::::::::::::::::

        fig11 = px.scatter(    
            temp, x=data_var, y='kW/h price daily mean', 
            title=fig11_title,
            trendline="ols", trendline_color_override="#ff516e"
        )

        fig11.update_layout(
            # font_family="Rockwell",
            margin=dict(l=80, r=0, t=50, b=20),
            font_color='#757575'
        )

        fig11.update_traces(
            marker=dict(size=6, line=dict(width=1, color='#383648')),
            selector=dict(mode='markers')
        )

        # :::::::::::::::::::::::

        fig12 = px.line(
            temp, x="Date", y=data_var, 
            title=fig12_title
        )

        fig12.update_layout(
            # font_family="Rockwell",
            margin=dict(l=80, r=0, t=50, b=20),
            font_color='#757575'
        )

        # :::::::::::::::::::::::
        del temp
        return fig9, fig10, fig11, fig12
    
    except:
        visdcc.Run_js(id='javascript', run="location.reload();")
        # print('Error')

# --------------------------------------------------------------------------

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
