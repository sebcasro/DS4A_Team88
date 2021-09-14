
# requires pandas, openpyxl

import pandas as pd

exportar_datos = True

def limpiar(n):
    return str(n).replace('.0', '')

def read_dataFile(path):  
    df = pd.read_excel(path)
    
    file_name = list(df)[0]
    
    if file_name == 'Unnamed: 0':
        for idx in list(df.iloc[0]):
            if isinstance(idx, str):
                file_name = idx
                break
    
    df.columns = map(limpiar, list(df.iloc[1]))    
    df = df.drop([0, 1]).reset_index(drop=True)
    df['Archivo'] = file_name

    return df

def main():
    documentos = [
    {'filename':'Disponibilidad_Real', 
     'enlace_1':'http://portalbissrs.xm.com.co/oferta/Histricos/Disponibilidad/Disponibilidad_Real_(kW)_',
     'enlace_2':'http://portalbissrs.xm.com.co/oferta/Histricos/Disponibilidad_Real_(kW)_'}
    ]
        
    for doc in documentos:
        temp = pd.DataFrame({'Fecha' : []})
        for year in range(2000, 2025):
            try:
                if year < 2020:
                    filePath = doc['enlace_1'] + f'{year}.xlsx'
                else:
                    filePath = doc['enlace_2'] + f'{year}.xlsx'
                    
                new_data = read_dataFile(filePath)
                temp = pd.concat([temp, new_data])
                print(f'{year} - Ok')

            except Exception as e:
                print(f'Error con la información del año {year} - {filePath} - {e}')
        
        if exportar_datos:
            temp.to_csv(f"{doc['filename']}.csv", index=False)

if __name__ == "__main__":
    main()