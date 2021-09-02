import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Input, Output

from app import app, server 

from layout import *
from callbacks import *

# Define basic structure of app:
app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar(),
        # sidebar(),
        content(),
    ],
)

#Runs the server at http://127.0.0.1:5000/
if __name__ == '__main__':
    # app.run_server(port=5000, host= '127.0.0.1',debug=True)
    app.run_server(debug=True)