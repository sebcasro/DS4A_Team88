import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div
from dash_html_components.Hr import Hr
import dash_daq as daq
from app import app

from datetime import date
import plotly.express as px
import pandas as pd

#####################################
# Add your data
#####################################

df2 = pd.read_csv('ts_kwh_dataframe.csv')
df2 = df2.drop(columns=['Unnamed: 0'])

df = pd.read_csv('ts_kwh_dataframe.csv')
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


#####################################
# Styles & Colors
#####################################

# the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 62.5,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "height": "100%",
#     "z-index": 1,
#     "overflow-x": "hidden",
#     "transition": "all 0.5s",
#     "padding": "0.5rem 1rem",
#     "background-color": "#f8f9fa",
# }

# SIDEBAR_HIDEN = {
#     "position": "fixed",
#     "top": 62.5,
#     "left": "-16rem",
#     "bottom": 0,
#     "width": "16rem",
#     "height": "100%",
#     "z-index": 1,
#     "overflow-x": "hidden",
#     "transition": "all 0.5s",
#     "padding": "0rem 0rem",
#     "background-color": "#f8f9fa",
# }

# the styles for the main content position it to the right of the sidebar and
# add some padding.
# CONTENT_STYLE_SIDEBAR = {
#     "transition": "margin-left .5s",
#     "margin-left": "18rem",
#     "margin-right": "1rem",
#     "padding": "2rem 1rem"
# }

CONTENT_STYLE_NO_SIDEBAR = {
    # "transition": "margin-left .5s",
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
            dbc.NavItem(dbc.NavLink("Testing", href="/test")),
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
