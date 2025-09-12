import pandas as pd
import numpy as np

###################################################################
##                 taller de DataFrame                           ##
##                 ACTIVIDAD DE DATAFRAMES                       ##
##                                                               ##
###################################################################

###################################################################
##1. Imagina que eres un analista de datos y tienes la siguiente ##
## información sobre 5 productos de una tienda de electrónica:   ##
##                                                               ##
##                                                               ##
###################################################################

tienda_electrica = { 
  "Id_Producto": [101, 102, 103, 104, 105], 
  "Nombre_Producto": ["Laptop","Mouse", "Teclado", "Monitor", "Webcam"], 
  "Categoria":["Computadoras", "Accesorios", "Accesorios", "Computadoras", "Accesorios"], 
  "Precio(USD)":[1200, 25, 75, 300, 50], 
  "Stock":[15,50,30,10,25] 
} 

##a. Crea un DataFrame de pandas con estos datos. 

df_tienda_electrica = pd.DataFrame(tienda_electrica )
print(f'DataFrame creado con los productos de la tienda:')
print("="*40)
print("DataFrame completo:")
print(df_tienda_electrica )

##b. Muestra las primeras 3 filas del DataFrame. 
Primeras_3_filas = df_tienda_electrica.head(3)
print("="*40)
print("Primeras 3 filas:")
print(Primeras_3_filas)


##c. Imprime la información general del DataFrame 
##   (tipos de datos, valores no nulos, etc.) usando el método info(). 
print("="*40)
print('Informacion general del DataFrame')
df_tienda_electrica.info()

##d. Calcula y muestra las estadísticas descriptivas de las columnas numéricas con el método describe(). 
estadistica_descriptivas=df_tienda_electrica.describe()
print("="*40)
print('Estadisticas Descriptivas')
print(estadistica_descriptivas)


###################################################################
##                                                               ##
##           2. Usando el DataFrame del Ejercicio 1:             ##
##                                                               ##
##                                                               ##
###################################################################

##a. Filtra y muestra solo los productos que tienen un precio mayor a $100. 
prdc_precio_mayor_a_100 = df_tienda_electrica[df_tienda_electrica["Precio(USD)"]>100]
print("="*40)
print('los productos con precio mayor a 100 son')
print(prdc_precio_mayor_a_100)

##b. Selecciona y muestra el "Nombre del Producto" y la "Categoría" de todos los productos que no están en la categoría 'Accesorios'. 
categoria_computadoras = df_tienda_electrica[df_tienda_electrica["Categoria"] != "Accesorios"][["Nombre_Producto", "Categoria"]]
print("="*40)
print("los productos de categoria 'Computadora' son: ")
print(categoria_computadoras)

##c. Encuentra y muestra todos los productos que tienen un precio entre $50 y $150 (inclusive). 
productos_50_150= df_tienda_electrica[(df_tienda_electrica["Precio(USD)"] >= 50) & (df_tienda_electrica["Precio(USD)"] <= 150)]
print("="*40)
print("Productos con precio entre $50 y $150:")
print(productos_50_150)


###################################################################
##                                                               ##
##           3. Usando el DataFrame del Ejercicio 1:             ##
##                                                               ##
##                                                               ##
###################################################################

##a. Calcula el precio promedio de los productos por cada "Categoría". 
precio_promedio_categoria = df_tienda_electrica.groupby("Categoria")["Precio(USD)"].mean()
print("="*40)
print("Precio promedio de los productos por categoría:")
print(precio_promedio_categoria)

##b. Determina el número total de productos disponibles ("En Stock") por cada "Categoría". 
stock_categoria = df_tienda_electrica.groupby("Categoria")["Stock"].sum()
print("="*40)
print("Stock total de productos por categoría:")
print(stock_categoria)

##c. Encuentra el precio máximo y mínimo de los productos en la categoría 'Computadoras'. 
precios_computadoras = df_tienda_electrica[df_tienda_electrica["Categoria"] == "Computadoras"]["Precio(USD)"]

precio_max = precios_computadoras.max()
precio_min = precios_computadoras.min()

print("="*40)
print("Precios en la categoría 'Computadoras':")
print(f"Precio máximo: ${precio_max}")
print(f"Precio mínimo: ${precio_min}")

###################################################################
##                                                               ##
##    4.Tienes el DataFrame del Ejercicio 1 y  un nuevo          ##
##      DataFrame con información de las ventas de cada producto ##
##                                                               ##
###################################################################

ventas = {
    "Id_Producto": [101, 103, 102, 104, 105],
    "ventas_totales": [50, 75, 120, 40, 90]
}


##a. Crea un segundo DataFrame con los datos de ventas. 
df_ventas = pd.DataFrame(ventas)
print("="*40)
print("DataFrame de Ventas:")
print(df_ventas)

##b. Combina ambos DataFrames en uno solo, usando la columna "ID del Producto" como clave de fusión. 
df_combinado = pd.merge(df_tienda_electrica, df_ventas, on="Id_Producto")
print("="*40)
print("DataFrame combinado (productos + ventas):")
print(df_combinado)

# c. Filtrar productos con ventas mayores al stock
ventas_mayores_stock = df_combinado[df_combinado["ventas_totales"] > df_combinado["Stock"]]
print("="*40)
print("Productos cuyas ventas superan el stock disponible:")
print(ventas_mayores_stock)


###################################################################
##                                                               ##
##    5. Tienes un DataFrame de clientes con algunos             ##
##        datos faltantes:                                       ##
##                                                               ##
###################################################################


data_clientes = {
    "ID Cliente": ["C001", "C002", "C003", "C004", "C005"],
    "Nombre": ["Ana", "Luis", "Sofía", "Pedro", "Marta"],
    "Ciudad": ["Bogotá", "Medellín", "Bogotá", np.nan, "Medellín"],
    "Edad": [34, np.nan,  28, 45, 31]
}

##a. Crea este DataFrame. 
df_clientes = pd.DataFrame(data_clientes)
print("="*40)
print("DataFrame de Clientes:")
print(df_clientes)


##b. Reemplaza los valores NaN en la columna 'Ciudad' por la cadena 'Desconocida'. 
df_clientes["Ciudad"] = df_clientes["Ciudad"].replace(np.nan, "Desconocida")
print("="*40)
print("Después de reemplazar NaN en Ciudad con replace:")
print(df_clientes)

##c. Reemplaza los valores NaN en la columna 'Edad' por la edad promedio de los clientes.
edad_promedio = df_clientes["Edad"].mean()

df_clientes["Edad"] = df_clientes["Edad"].fillna(edad_promedio)
print("="*40)
print("Después de reemplazar NaN en Edad con el promedio:")
print(df_clientes)

##d. Crea una nueva columna llamada Grupo de Edad que categorice a los clientes: 'Joven' (si la edad es menor de 30) y 'Adulto' (si la edad es 30 o más). 
df_clientes["Grupo de Edad"] = np.where(df_clientes["Edad"] < 30, "Joven", "Adulto")
print("="*40)
print(df_clientes)