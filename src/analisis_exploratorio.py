import pandas as pd

def realizar_analisis_micromercado(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_archivo}. Verifica la ruta.")
        return

    print("==========================================================")
    print("      📊 REPORTE ESTADÍSTICO DEL MICROMERCADO 📊         ")
    print("==========================================================\n")
    
    # 2. Resumen estadístico general de las columnas con números
    print("1. RESUMEN ESTADÍSTICO DE VARIABLES CLAVE:")
    # describe() calcula automáticamente la media, mínimos, máximos, etc.
    print(df[['Unit price', 'Quantity', 'Sales', 'gross income', 'Rating']].describe())
    print("-" * 58)
    
    # 3. Totales económicos del negocio
    total_ventas = df['Sales'].sum()         # Suma todo el dinero ingresado
    total_ganancia = df['gross income'].sum() # Suma la ganancia real (ingreso - costo)
    ticket_promedio = df['Sales'].mean()      # Calcula el gasto promedio por cliente
    
    print("2. INDICADORES FINANCIEROS GLOBALES:")
    print(f"   • Facturación Total (Sales): ${total_ventas:,.2f}")
    print(f"   • Ganancia Bruta Total (Gross Income): ${total_ganancia:,.2f}")
    print(f"   • Ticket Promedio de Compra: ${ticket_promedio:.2f}")
    print("-" * 58)
    
    # 4. Análisis por Categoría de Producto (Product line)
    print("3. VENTAS TOTALES POR LÍNEA DE PRODUCTO:")
    # Agrupa por categoría y suma las ventas de cada una
    ventas_por_producto = df.groupby('Product line')['Sales'].sum().sort_values(ascending=False)
    for producto, venta in ventas_por_producto.items():
        print(f"   • {producto}: ${venta:,.2f}")
    print("-" * 58)
    
    # 5. Análisis por Sucursal (Branch) y Ciudad (City)
    print("4. RENDIMIENTO DE VENTAS POR SUCURSAL:")
    ventas_sucursal = df.groupby(['City', 'Branch'])['Sales'].sum().sort_values(ascending=False)
    print(ventas_sucursal)
    print("-" * 58)
    
    # 6. Comportamiento del Consumidor (Tipo de cliente y Género)
    print("5. GASTO PROMEDIO POR TIPO DE CLIENTE Y GÉNERO:")
    # Calcula cuánto gasta en promedio cada perfil de cliente
    clientes_genero = df.groupby(['Customer type', 'Gender'])['Sales'].mean().unstack()
    print(clientes_genero)
    print("==========================================================")

if __name__ == "__main__":

    realizar_analisis_micromercado('/content/SuperMarket-Analysis/data/SuperMarket Analysis_Limpio.csv')
