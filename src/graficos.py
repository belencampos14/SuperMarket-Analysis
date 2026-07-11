"""
Modulo de visualizacion del proyecto SuperMarket Analysis.

Este archivo contiene los graficos generados a partir
del analisis estadistico del dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

RUTA_ARCHIVO = "data/SuperMarket Analysis.csv"


RUTA_ARCHIVO = "data/SuperMarket Analysis.csv"


def cargar_datos(ruta_archivo):            
   
    try:
        df = pd.read_csv(ruta_archivo)

        print("Dataset cargado correctamente")
        print(f"Cantidad de registros: {len(df)}")

        return df

    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV")
        return None


df = cargar_datos(RUTA_ARCHIVO)
ventas_por_producto = df.groupby('Product line')['Sales'].sum() 

def grafico_ventas_categoria(df):
    """
    Genera un gráfico de barras con las ventas
    totales por categoría de producto.
    """

    ventas_categoria = (
        df.groupby("Product line")["Sales"]    #agrupa 
        .sum()                                 #suma
        .sort_values()                         #ordena de menor a mayor valores
    )


    plt.figure(figsize=(10,6))              # prepra un nuevo lienzo y define su tamaño
                                            

    ventas_categoria.plot(
        kind="barh"                            #crea las barras horizontales     
    )


    plt.title(                                #crea el titulo  
        "Ventas totales por línea de producto"
    )

    plt.xlabel(                                #asigna al eje de las X lo que tiene q visualizar 
        "Ventas ($)"
    )

    plt.ylabel(                                #asigna al eje de las y lo que tiene que visualizar
        "Categoría de producto"
    )


    plt.tight_layout()                     #Ajusta automáticamente los espacios  #del gráfico para evitar que los elementos se monten o se corten.
                                            
    plt.savefig(                           # guarda el grafico como una imagen
    "results/ventas_categoria.png",
    dpi=300,                               #define la calidad de imagen
    bbox_inches="tight"                    #Evita que Matplotlib  guarde espacios innecesarios
)
    plt.show()                              # Muestra el grafico en pantalla


ventas_sucursal = df.groupby(['City', 'Branch'])['Sales'].sum()

def grafico_ventas_ciudad_sucursal(df):
    """
    Genera un gráfico comparativo de ventas
    por ciudad y sucursal.
    """

    ventas = (
        df.groupby(["City", "Branch"])["Sales"]
        .sum()
        .unstack()                              #convierte el indice jerarquico en columnas
    )


    plt.figure(figsize=(10,6))


    ventas.plot(
        kind="bar",
        figsize=(10,6)
    )


    plt.title(
        "Ventas por ciudad y sucursal"
    )


    plt.xlabel(
        "Ciudad"
    )


    plt.ylabel(
        "Ventas ($)"
    )


    plt.xticks(                             #sirve para configurar marcas y etiquetas en X
        rotation=0                          #sirve para girar el texto de etiqueta en grados
    )


    plt.tight_layout()

    plt.savefig(
    "results/ventas_ciudad_sucursal.png",
    dpi=300,
    bbox_inches="tight"
)

    plt.show()

clientes_genero = df.groupby(['Customer type','Gender'])['Sales'].mean().unstack()

def grafico_cliente_genero(df):
    """
    Genera un gráfico del gasto promedio
    según tipo de cliente y género.
    """

    gasto_promedio = (
        df.groupby(
            ["Customer type", "Gender"]
        )["Sales"]
        .mean()
        .unstack()
    )


    plt.figure(figsize=(8,5))


    gasto_promedio.plot(
        kind="bar",
        figsize=(8,5)
    )


    plt.title(
        "Gasto promedio por tipo de cliente y género"
    )


    plt.xlabel(
        "Tipo de cliente"
    )


    plt.ylabel(
        "Promedio de compra ($)"
    )


    plt.xticks(
        rotation=0
    )


    plt.tight_layout()

    plt.savefig(
    "results/cliente_genero.png",
    dpi=300,
    bbox_inches="tight"
)

    plt.show()


    df[['Sales']].describe()
def grafico_distribucion_ventas(df):
    """
    Genera un histograma de la distribución
    de los valores de venta.
    """

    plt.figure(figsize=(8,5))


    plt.hist(
        df["Sales"],
        bins=20
    )


    plt.title(
        "Distribución de ventas del supermercado"
    )


    plt.xlabel(
        "Monto de venta ($)"
    )


    plt.ylabel(
        "Cantidad de compras"
    )


    plt.tight_layout()

    plt.savefig(
    "results/distribucion_ventas.png",
    dpi=300,
    bbox_inches="tight"
)

    plt.show()

    ventas_por_producto = df.groupby('Product line')['Sales'].sum()
def grafico_pastel_categoria(df):
    """
    Genera un gráfico circular con la participación
    de ventas por línea de producto.
    """

    ventas_categoria = (
        df.groupby("Product line")["Sales"]
        .sum()
    )


    plt.figure(figsize=(8,8))


    plt.pie(
        ventas_categoria,
        labels=ventas_categoria.index,
        autopct="%1.1f%%",
        startangle=90
    )


    plt.title(
        "Participación porcentual de ventas por categoría"
    )


    plt.tight_layout()

    plt.savefig(
    "results/participacion_categoria.png",
    dpi=300,
    bbox_inches="tight"
)

    plt.show()    

if __name__ == "__main__":  #condicion que controla archivo.py se ejecuta. 

    df = cargar_datos(RUTA_ARCHIVO)

    if df is not None:  #variable df tiene algún valor (es decir, no está vacía y no es None), entonces ejecuta el código que está dentro

        grafico_ventas_categoria(df)

        grafico_ventas_ciudad_sucursal(df)

        grafico_cliente_genero(df)

        grafico_distribucion_ventas(df)

        grafico_pastel_categoria(df)