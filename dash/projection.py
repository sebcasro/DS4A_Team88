import json
import numpy as np
import pandas as pd

original_df = pd.read_excel('./data/original series.xlsx')
original_df = original_df.set_index('Date')

forecast_df = pd.read_excel('./data/series forecast.xlsx')
forecast_df = forecast_df.set_index('Date')

forecast_diff_df = pd.read_excel('./data/series forecast diff.xlsx')
forecast_diff_df = forecast_diff_df.set_index('Date')

with open('./data/impulse_responses.json', 'r') as f:
    impulse_response = json.load(f)


projection_df = pd.concat([original_df, forecast_df], axis=1, join="outer")
projection_df['Year'] = projection_df.index.year
projection_df = projection_df.reset_index()

projection_df = projection_df.melt(id_vars=['Date', 'Year'], 
                           value_vars=['kW/h price mean', 'kW/h price ARIMA', 
                                       'kW/h price SARIMAX', 'kW/h price Neural Prophet', 'kW/h price mean models'], 
                           var_name='model', value_name='value')


def impulse_dataframe(date, var, expansion):
    impulse_dataframe = pd.DataFrame(impulse_response[var])*expansion
    impulse_dataframe['Date'] = pd.date_range(start=date, periods=len(impulse_response[var]), freq='D')
    impulse_dataframe['Date'] = pd.to_datetime(impulse_dataframe['Date'])
    impulse_dataframe.columns = ['price response','Date']
    impulse_dataframe = impulse_dataframe.set_index('Date')
    return impulse_dataframe


def response_dataframe(date, modelo, var, expansion):
    modelo = str(modelo)+' diff'
    temp_dataframe = pd.concat([forecast_diff_df[modelo], impulse_dataframe(date, var, expansion)], axis=1)
    temp_dataframe.columns = ['original', 'impulse']
    temp_dataframe = temp_dataframe.replace(np.nan, 0)
    temp_dataframe['response'] = temp_dataframe['original'] + temp_dataframe['impulse']
    return temp_dataframe


def original_level_after_shock(date, modelo, var, expansion):
    response = response_dataframe(date, modelo, var, expansion)['response'].tolist()
    origin = 83.2870833333333
    original_level_temp = []
    for i in range(0,len(response)):
        if i == 0:
            x = origin + response[0]
            original_level_temp.append(x)
        else:
            x = response[i] + original_level_temp[-1]
            original_level_temp.append(x)
    forecast_df = pd.DataFrame(original_level_temp)
    forecast_df['Date'] = pd.date_range(start='2021-07-15', periods=len(forecast_df), freq='D')
    forecast_df['Date'] = pd.to_datetime(forecast_df['Date'])
    forecast_df.columns = ['price response','Date']
    forecast_df = forecast_df.set_index('Date')
    return forecast_df


def response_con_convergencia(date, modelo, var, expansion):
    temp_dataframe = pd.concat([forecast_df[modelo], impulse_dataframe(date, var, expansion)], axis=1)
    temp_dataframe.columns = ['original', 'impulse']
    temp_dataframe = temp_dataframe.replace(np.nan, 0)
    temp_dataframe['response'] = temp_dataframe['original'] + temp_dataframe['impulse']
    return temp_dataframe


def original_level_after_shock_convergencia(date, modelo, var, expansion):
    response = response_con_convergencia(date, modelo, var, expansion)['response'].tolist()
    origin = 83.2870833333333
    original_level_temp = []
    for i in range(0,len(response)):
        if i == 0:
            x = response[0] #+ origin
            original_level_temp.append(x)
        else:
            x = response[i] #+ original_level_temp[-1]
            original_level_temp.append(x)
    forecast_df = pd.DataFrame(original_level_temp)
    forecast_df['Date'] = pd.date_range(start='2021-07-15', periods=len(forecast_df), freq='D')
    forecast_df['Date'] = pd.to_datetime(forecast_df['Date'])
    forecast_df.columns = ['price response','Date']
    forecast_df = forecast_df.set_index('Date')
    return forecast_df


