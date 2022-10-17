import pandas as pd
rutaFileCsv ='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str) -> str:
    df=pd.read_csv(rutaFileCsv,index_col=['Country','Language'],na_values='None')
    h=pd.pivot_table(df,index=['Country','Language'])
    f=pd.DataFrame(h.loc[:,'Gross Earnings'])
    g=pd.DataFrame(f.iloc[0:10])
    print (g)
    return g
print(listaPeliculas(rutaFileCsv))


import pandas as pd
# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str) -> str:
    df=pd.read_csv(rutaFileCsv,index_col=['Country','Language'],na_values='None')
    h=pd.pivot_table(df,index=['Country','Language'])
    f=pd.DataFrame(h.loc[:,'Gross Earnings'])
    print(f[:10])
    return f

print(listaPeliculas(rutaFileCsv))