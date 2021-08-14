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

df = pd.read_csv('ts_kwh_dataframe.csv')
df = df.drop(columns=['Unnamed: 0'])

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
    "margin-left": "1rem",
    "margin-right": "1rem",
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
            # dbc.DropdownMenu(
            #     children=[
            #         dbc.DropdownMenuItem("More pages", header=True),
            #         dbc.DropdownMenuItem("Page 2", href="/page-2"),
            #         dbc.DropdownMenuItem("Page 3", href="/page-3"),
            #     ],
            #     nav=True,
            #     in_navbar=True,
            #     label="More",
            # ),
        ],
        brand="Brand",
        brand_href="#",
        color="dark",
        dark=True,
        fluid=True,
    )
    return navbar

# def sidebar():
#     """
#     Creates side bar
#     """
#     navbar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.H5("bla bla bla Dashboard", style={'textAlign':'center'}),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         html.Hr(),

#         dbc.Nav(
#             [
#                 dbc.NavLink("Page 1", href="/page-1", id="page-1-link"),
#                 dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
#                 dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),
#             ],
#             vertical=True,
#             pills=True,
#         ),

#         html.Hr(),

        
#     ],    
#     id='sidebar',
#     style=SIDEBAR_STYLE,
#     )  
#     return navbar

def content():
    content = html.Div(id="page-content", style=CONTENT_STYLE_NO_SIDEBAR)
    return content