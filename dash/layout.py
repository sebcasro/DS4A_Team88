import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

# from app import app
# import dash_core_components as dcc
# from dash_html_components.Div import Div
# from dash_html_components.Hr import Hr
# import dash_daq as daq
# import plotly.express as px

#####################################
# Add your data
#####################################

df = pd.read_csv('./data/ts_kwh_dataframe.csv')
df = df.drop('Unnamed: 0', axis = 1)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df['Year'] = df.index.year
df['Month2'] = df.index.month
df["Month"] = df["Month2"].replace({1:"January", 2:"February", 3:"March", 4:"April",
                                    5:"May", 6:"June", 7:"July", 8:"August", 9:"September",
                                    10:"October", 11:"November", 12:"December"})

df["Total availability"] = df["Hydraulic availability"].fillna(0) + df["Thermal availability"].fillna(0) + df["Solar availability"].fillna(0)
df = df.reset_index()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

dtypes = {'Fecha': 'object', 'Recurso': 'object', 'Código Agente': 'object', 'Archivo': 'object', 'Código Recurso': 'object'}
prom_diario=pd.read_csv("./data/Disponibilidad_Real(porcentaje).csv", dtype=dtypes)
del dtypes

prom_diario.rename(columns={'Recurso':'Company',"Tipo Generación":"Energy type", "Fecha":"Date" }, inplace=True)
prom_diario=prom_diario.drop(['Archivo', 'Código Recurso', 'Código Agente'], axis = 1)
prom_diario["Total power generation"]=prom_diario.mean(axis=1)
prom_diario['Month'] = pd.DatetimeIndex(prom_diario['Date']).month
prom_diario["Month2"] = prom_diario["Month"].replace({1:"January", 2:"February", 3:"March", 4:"April", 
                                                      5:"May", 6:"June", 7:"July", 8:"August", 9:"September",
                                                      10:"October", 11:"November", 12:"December"})
prom_diario['Day'] = pd.DatetimeIndex(prom_diario['Date']).weekday
prom_diario['Year'] = pd.DatetimeIndex(prom_diario['Date']).year

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

dtypes = {'Fecha': 'object', 'Recurso': 'object', 'Código Agente': 'object', 'Archivo': 'object', 'Código Recurso': 'object'}
prom_diario_real = pd.read_csv("./data/Disponibilidad_Real.csv", dtype=dtypes)
del dtypes

prom_diario_real[["0","1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12","13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]]=prom_diario_real[["0","1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12","13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]]/1000000
prom_diario_real.rename(columns={'Recurso':'Company',"Tipo Generación":"Energy type", "Fecha":"Date" }, inplace=True)
prom_diario_real=prom_diario_real.drop(['Archivo', 'Código Recurso', 'Código Agente'], axis = 1)
prom_diario_real["Total energy generated GW"]=prom_diario_real.sum(axis=1)
prom_diario_real['Month'] = pd.DatetimeIndex(prom_diario_real['Date']).month
prom_diario_real["Month2"] = prom_diario_real["Month"].replace({1:"January", 2:"February", 3:"March", 4:"April", 
                                                                5:"May", 6:"June", 7:"July", 8:"August", 9:"September",
                                                                10:"October", 11:"November", 12:"December"})
prom_diario_real["Energy type"] = prom_diario_real["Energy type"].replace({"HIDRAULICA":"Hydraulic", "TERMICA":"Thermal", "SOLAR":"Solar"})                                                                
prom_diario_real['Day'] = pd.DatetimeIndex(prom_diario_real['Date']).weekday
prom_diario_real['Year'] = pd.DatetimeIndex(prom_diario_real['Date']).year

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

CONTENT_STYLE_NO_SIDEBAR = {
    "marginLeft": "1rem",
    "marginRight": "1rem",
    "padding": "1rem 1rem"
}

#####################################
# Create Auxiliary Components Here
#####################################
def navbar():
    navbar = dbc.NavbarSimple(
        children=[
            # dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
            dbc.NavItem(dbc.NavLink("Home", href="/home")),
            dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
            dbc.NavItem(dbc.NavLink("About us", href="/about-us")),
        ],
        brand="DS4A - Team 88",
        brand_href="/",
        color="dark",
        dark=True,
        fluid=True,
    )
    return navbar

def content():
    content = html.Div(id="page-content", style=CONTENT_STYLE_NO_SIDEBAR)
    return content
