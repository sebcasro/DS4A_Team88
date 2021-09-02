# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:15:38 2021

@author: Usuario
"""

import pandas as pd



def find_header(df):
    #Get row and column of #Fecha on the data frame
    result=df.isin(["Fecha"])   
    column_date=result.any()
    column_date=column_date[column_date==True].index[0]
    row_date=result[column_date][result[column_date]==True].index[0]
    
    #On row date get the columns where are the hours [0:23]
    hours=[i for i in range(0,24)]
    #Convert hours from integers to string, in case text above header
    hours_str = list(map(str, hours))
    #List of Combined hours in format integers and string
    hours_comb=hours+hours_str
    #Find by combined hours format
    result=df.iloc[row_date,:].isin(hours_comb) 
    #Get column names for the searched hours 
    columns_hours=list(result[result==True].index)
    
    
    #List of columns wich contains the interested header of the dataframe
    columns=list([column_date])+columns_hours
    #From dataframe only take such columns
    df=df[columns]
    #Set new columns header
    new_columns=["Fecha"]+hours_str
    df.columns=new_columns

    #Get label of parameter downloaded and assing to a entire new column
    #df['file'] = df.iloc[0][0]
    
    #Drop row where the header was found and rows before it
    drop_rows=[i for i in range(0,row_date+1)]
    df = df.drop(drop_rows).reset_index(drop=True)
    
    #Change format of elements in df that could be in string to numeric in hours column
    df[hours_str] = df[hours_str].apply(pd.to_numeric)
    
    
    #Delate nan values on Fecha column
    df.dropna(subset = ["Fecha"], inplace=True)    
    
    #Change format of Fecha column to datetime format
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    
    return df


def read_dataFile(path):
    df = pd.read_excel(path)

    df=find_header(df)

    return df

#http://portalbissrs.xm.com.co/trpr/Histricos/Precios/Precio_Bolsa_Nacional_(%24kwh)_1995.xlsx?

temp = pd.DataFrame({'Fecha' : []})

for year in range(1995, 2020):
    filePath = f'http://portalbissrs.xm.com.co/trpr/Histricos/Precios/Precio_Bolsa_Nacional_(%24kwh)_{year}.xlsx?'
    new_data = read_dataFile(filePath)
    temp = pd.concat([temp, new_data])
    

def melt_df(df):
    #Hours
    hours=[i for i in range(0,24)]
    #Convert hours from integers to string, column names
    hours_str = list(map(str, hours))
    #Melt original dataframe
    df_melt=pd.melt(df,id_vars=["Fecha"],value_vars=hours_str,var_name='Hour', value_name='Precio_Bolsa')
    #Convert string to float
    df_melt["Hour"]=pd.to_numeric(df_melt["Hour"])
    
    #Add hours to the date which only had considered the day
    df_melt["Fecha"]=df_melt["Fecha"]+pd.to_timedelta(df_melt["Hour"],unit='H')
    #Order de data
    df_melt.sort_values(by=['Fecha'], inplace=True, ascending=False) #Most recent first
    #Reset index
    df_melt=df_melt.reset_index(drop=True)
    
    return df_melt

temp_melt=melt_df(temp)
    
    
    
    
    
    