import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    
    html.Div(["Input2: ",
              dcc.Input(id='my-input2', value='initial value', type='text')]),
    html.Br(),

    html.Div(id='my-output'),
    html.Br(),
    html.Div(id='my-output2'),
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Output(component_id='my-output2', component_property='children'),
    Input(component_id='my-input', component_property='value'),
    Input(component_id='my-input2', component_property='value')
)
def update_output_div(input_value, input_value2):
    out1 = f'Output_1: in1:{input_value}'
    out2 = f'Output_2: in2:{input_value2}'
    return out1, out2


if __name__ == '__main__':
    app.run_server(debug=True)