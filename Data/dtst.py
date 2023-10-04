import pandas as pd


file_path = '/mnt/f/Cristobal/Tareas Prog/Prog III/Parcial1/Data/DataSetCasosCovid.csv'

df = pd.read_csv(file_path)

#NORMALIZACIÓN FECHAS++++++
df['fecha reporte web'] = pd.to_datetime(df['fecha reporte web'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de notificación'] = pd.to_datetime(df['Fecha de notificación'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de inicio de síntomas'] = pd.to_datetime(df['Fecha de inicio de síntomas'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de muerte'] = pd.to_datetime(df['Fecha de muerte'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de diagnóstico'] = pd.to_datetime(df['Fecha de diagnóstico'], format='%Y-%m-%d %H:%M:%S')
df['Fecha de recuperación'] = pd.to_datetime(df['Fecha de recuperación'], format='%Y-%m-%d %H:%M:%S')



#NORMALIZACION E IMPUTACIÓN DE LA COLUMNA UBICACIÓN DEL CASO+++++++
#'''
df['Ubicación del caso'] = df['Ubicación del caso'].replace('casa', 'Casa')
df['Ubicación del caso'] = df['Ubicación del caso'].fillna('Casa')
#LA MAYORIA DE CASOS FUERON EN LA CASA
#'''

#NORMALIZACIÓN E IMPUTACIÓN DE LA COLUMNA ESTADO++++++++
#'''
df['Estado'] = df['Estado'].replace('leve','Leve')#normalización de dato leve
df['Estado'] = df['Estado'].fillna('Fallecido')#rellenar los nulos con Fallecido
#LOS FALLECIDOS TENIAN EN PROMEDIO 69 AÑOS, EDAD QUE CONCUERDA CON LOS DE VALOR NULO EN EL ESTADO
#'''

#IMPUTACIÓN COLUMNA CÓDIGO ISO DEL PAÍS+++++++
#'''
df['Código ISO del país'] = df['Código ISO del país'].fillna(170)#los que no tienen codigo se infieren que son de colombia(ISO 170)
#'''

#IMPUTACIÓN COLUMNA NOMBRE DEL PAÍS+++++++++
#'''
df['Nombre del país'] = df['Nombre del país'].fillna('COLOMBIA')#los que no tienen nombre del país se infieren que son de COLOMBIA
#'''

#NORMALIZACIÓN E IMPUTACIÓN COLUMNA RECUPERADO++++++
#'''
df['Recuperado'] = df['Recuperado'].replace('fallecido','Fallecido')#normalizar valores
df.loc[df['Edad'] >= 70, 'Recuperado'] = 'Fallecido'#en caso de ser de mas de 69 poner fallecido
df.loc[(df['Edad'] < 70) & (df['Edad']>=42 ), 'Recuperado'] = 'Activo'#en caso de estar entre 70 y 42 poner activo
df.loc[df['Edad'] < 42 , 'Recuperado'] = 'Recuperado'#en caso de ser menor a 42 poner recuperado
#'''

#IMPUTACIÓN COLUMNA FECHA DE INICIO DE SINTOMAS++++++++
#'''
df['Fecha de inicio de síntomas'].fillna(df['fecha reporte web'], inplace=True)
#se pone en los registros de valor nan de fecha de inicio de síntomas el valor de la fecha de reporte web, siendo estos dos cercanos
#'''

#IMPUTACIÓN COLUMNA FECHA DE MUERTE
#'''
df['Fecha de muerte'].fillna('2000-01-01 00:00:00', inplace=True)
#se infiere que si no tiene fecha de muerte es porque no murió por lo que se pone un dato atípico identificable que no se tenga en cuenta
#'''

#IMPUTACIÓN COLUMNA FECHA DE DIAGNOSTICO+++++++++
#'''
df['Fecha de diagnóstico'].fillna(df['fecha reporte web'], inplace=True)
#se pone en los registros de valor nan de fecha de diagnóstico el valor de la fecha de reporte web, siendo estos dos cercanos
#'''


#INPUTACIÓN COLUMNA FECHA DE RECUPERACIÓN+++++++
#despues toca quitar los registros donde fecha de muerte y fecha de recuperación sean iguales------------------
#'''
df['Fecha de recuperación'].fillna('2000-01-01 00:00:00', inplace=True)
#se infiere que si no tiene fecha de recuperación es porque murió por lo que se pone un dato atípico identificable que no se tenga en cuenta
df = df[df['Fecha de recuperación'] != df['Fecha de muerte']]
#remover los registros en donde la fecha de recuperación y fecha de muerte para evitar incongruencia
#'''


#NORMALIZACIÓN E IMPUTACIÓN COLUMNA TIPO DE RECUPERACIÓN+++++++++
#'''
df['Tipo de recuperación'] = df['Tipo de recuperación'].replace('TIEMPO','Tiempo')#normalizar valores
df.loc[df['Recuperado'] == 'Fallecido', 'Tipo de recuperación'] = 'Fallecido'
df['Tipo de recuperación'].fillna('Tiempo', inplace=True)#rellenar los valores con 'Fallecido'
#'''

#IMPUTACIÓN COLUMNA PERTENENCIA ÉTNICA
#'''
df['Pertenencia étnica'].fillna(6, inplace=True)#rellenar los(pocos 5) valores con 6
#'''

#IMPUTACIÓN COLUMNA NOMBRE DEL GRUPO ÉTNICO
#'''
df['Nombre del grupo étnico'].fillna('Sin Comunidad', inplace=True)
#se infiere que la mayoría de personas que se atiende es porque estan mas que todo en algun lugar de civilización por lo que mayoría
#que no tienen valor se les reemplaza por sin comunidad
#'''
unique_counts = {}
for column in df.columns:
    num_unique = df[column].nunique()
    if num_unique < 200 and num_unique>1:
        unique_counts[column] = num_unique

'''print("UNICOSSFDSFDSFSDFDSF")
print(unique_counts)
print(df['Unidad de medida de edad'].unique())
print(df.info())
print(df.describe())
'''

