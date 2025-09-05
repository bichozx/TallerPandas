import pandas as pd

##################################################################
##     1. Crea una serie de pandas para cada uno de los         ##
##      siguientes conjuntos de datos. Utiliza los nombres      ##
##      proporcionados para cada serie.                         ##
##                                                              ##
##################################################################

# Índice: Región, Valores: Porcentaje de energía renovable
energia_renovable = pd.Series([85, 78, 65, 92, 55], index=['América Latina', 'Europa', 'Asia', 'África', 'América del Norte'])
print(f"Porcentaje de energía renovable por región:\n", energia_renovable, "\n")

residuos_pc = pd.Series([1.2, 1.5, 0.8, 2.1, 1.1], index=['Bogotá', 'Nueva York', 'Tokio', 'Dubái', 'París'])
print(f"Residuos per cápita (kg/día):\n", residuos_pc, "\n")

emisiones_co2 = pd.Series([4.5, 16.2, 7.8, 1.9, 12.5], index=['Brasil', 'Estados Unidos', 'Alemania', 'Nigeria', 'Canadá'])
print(f"Emisiones de CO2 per cápita (toneladas):\n", emisiones_co2, "\n")

deforestacion = pd.Series([0.5, 1.2, 0.8, 2.5, 0.3], index=['Amazonía', 'Congo', 'Borneo', 'Siberia', 'Canadá'])
print(f"Tasa de deforestación anual (%):\n", deforestacion, "\n")


##################################################################
##                                                              ##
##     2. Utilizando las series creadas, calcula las siguientes ##
##      métricas y almacena los resultados en variables.        ##
##                                                              ##
##################################################################

##2.1. ¿Cuál es el porcentaje promedio de energía renovable entre las regiones?
promedio = energia_renovable.mean()
print(f"el porcentage promedio de energia renovable entre las regiones es: {promedio:.2f}%")


#2.2. ¿Cuál es el máximo y el mínimo de residuos per cápita?
maximo= residuos_pc.max()
ciudad_max=residuos_pc.idxmax()

minimo= residuos_pc.min()
ciudad_min=residuos_pc.idxmin()

print(f"El maximo residuo per cápita es {maximo} kg/dia en {ciudad_max}.")
print(f"El minimo residuo per cápita es {minimo} kg/dia en {ciudad_min}.")


#2.3. Calcula el promedio de las emisiones de CO2 y la desviación estándar.
promedio = emisiones_co2.mean()
desviacionEstandar = emisiones_co2.std()

print(f"El promedio de emision de CO2: {promedio:.2f} toneladas")
print(f"Desviación estándar de emisiones de CO2: {desviacionEstandar:.2f} toneladas")


##2.4. ¿Cuál es la suma total de la tasa de deforestación? (Aunque no es una métrica estándar, sirve para practicar la función sum()).
sumaTotal = deforestacion.sum()
print(f"La suma total de deforestacion es: {sumaTotal:.2f}")


##################################################################
##     3. Utilizando las series, responde las siguientes        ##
##      preguntas aplicando operaciones de filtrado booleano    ##
##      selección de elementos.                                 ##
##                                                              ##
##################################################################

##3.1. Filtra y muestra las regiones con un porcentaje de energía renovable superior al 80%.
filtroRenovable = energia_renovable[energia_renovable > 80]
print(f"Regiones con mas del 80% de energia renovable:\n", filtroRenovable)

##3.2. Identifica la ciudad con la menor generación de residuos per cápita.
minimo= residuos_pc.min()
ciudad_min=residuos_pc.idxmin()

print(f"La ciudad con menor generación de residuos per cápita es: {ciudad_min} con: {minimo} kg/dia.")

##3.3. Selecciona y muestra los países con emisiones de CO2 per cápita inferiores a 10 toneladas.
filtroEmisionesCo2 = emisiones_co2[emisiones_co2 < 10]
print(f"Los paises con emisiones de CO2 per cápita inferiores a 10 toneladas son:\n", filtroEmisionesCo2)

##3.4. ¿Qué zonas boscosas tienen una tasa de deforestación anual superior al 1%?
filtroDeforestacion = deforestacion[deforestacion > 1]
print(f"Las zonas boscosas que tienen una tasa de deforestación anual superior al 1% son:\n", filtroDeforestacion)


##################################################################
##     4. Muestra una lista de ciudades que generan menos       ##
##      de 1.5 kg/día de residuos per cápita Y que,             ##
##      hipotéticamente, se encuentran en países con emisiones  ##
##      de CO2 per cápita menores a 10 toneladas                ##
##################################################################

##(asume la correspondencia de Bogotá -> Brasil, Tokio -> Alemania, París -> Brasil).

ciudad_pais={
    'Bogotá': 'Brasil',
    'Nueva York': 'Estados Unidos',
    'Tokio': 'Alemania',
    'Dubái': 'Nigeria',
    'París': 'Canadá'
}


df = pd.DataFrame({
    "Ciudad": residuos_pc.index,
    "Residuos": residuos_pc.values,
    "País": [ciudad_pais[ciudad] for ciudad in residuos_pc.index],
    "Emisiones": [emisiones_co2[ciudad_pais[ciudad]] for ciudad in residuos_pc.index]
})

filtro = df[(df['Residuos'] < 1.5 ) & (df['Emisiones'] < 10)]
print(f"Ciudades que generan menos de 1.5 kg/día de residuos y paises con emisiones de CO2 menores a 10 toneladas:\n")
print(filtro[["Ciudad", "País"]])




##################################################################
##    5. De las regiones con un porcentaje de energía renovable ##
##      inferior al 70%, identifica la que tiene la tasa        ##
##      de deforestación más baja.                              ##
##                                                              ##
##################################################################

##(Asume que Asia se correlaciona con Borneo y América del Norte con Canadá).

region_bosque = {
  'América Latina': 'Amazonía',
  'América del Norte': 'Canadá',
  'Asia': 'Borneo',
  'África': 'Congo',
  'Europa': 'Siberia',
}

filtroRegiones_bajas = energia_renovable[energia_renovable < 70]

df= pd.DataFrame({
  "Región": filtroRegiones_bajas.index,
  "Energia Renovable": filtroRegiones_bajas.values,
  "Zona Boscosa": [region_bosque[region] for region in filtroRegiones_bajas.index],
  "Deforestación": [deforestacion[region_bosque[region]] for region in filtroRegiones_bajas.index]
})

print("Regiones con energía renovable < 70%:\n")
print(df, "\n")

min_deforestacion = df.loc[df["Deforestación"].idxmin()]

print(f"La región con menor tasa de deforestación es:")
print(f"{min_deforestacion['Región']} ({min_deforestacion['Zona Boscosa']}) ", f"con {min_deforestacion['Deforestación']}% de deforestación anual.")

