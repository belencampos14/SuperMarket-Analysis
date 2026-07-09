import pandas as pd

def realizar_analisis_exploratorio(ruta_archivo):
    """
    Realiza el análisis exploratorio y estadístico del dataset del supermercado.
    """
    try:
        df = pd.read_csv(ruta_archivo)
        print(f"✅ Archivo cargado correctamente: {ruta_archivo}")
        print(f"   Dimensiones: {df.shape[0]} filas y {df.shape[1]} columnas\n")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en {ruta_archivo}")
        print("   Verifica que el archivo 'SuperMarket Analysis_Limpio.csv' esté en la carpeta 'data/'")
        return
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return

    print("=" * 80)
    print("       📊 ANÁLISIS EXPLORATORIO DEL MICROMERCADO 📊")
    print("=" * 80)

    # 1. Información general
    print("\n1. INFORMACIÓN GENERAL DEL DATASET")
    print("-" * 60)
    print(f"Total de registros: {df.shape[0]:,}")
    print(f"Total de columnas:  {df.shape[1]}")
    print("\nColumnas del dataset:")
    for col in df.columns:
        print(f"   • {col}")

    # 2. Resumen estadístico de variables numéricas
    print("\n2. RESUMEN ESTADÍSTICO DE VARIABLES CLAVE")
    print("-" * 60)
    columnas_numericas = ['Unit price', 'Quantity', 'Sales', 'gross income', 'Rating']
    print(df[columnas_numericas].describe().round(2))
    print("-" * 60)

    # 3. Indicadores financieros
    print("\n3. INDICADORES FINANCIEROS GLOBALES")
    print("-" * 60)
    total_ventas = df['Sales'].sum()
    total_ganancia = df['gross income'].sum()
    ticket_promedio = df['Sales'].mean()
    venta_max = df['Sales'].max()
    venta_min = df['Sales'].min()

    print(f"Facturación Total (Sales)      : ${total_ventas:,.2f}")
    print(f"Ganancia Bruta Total           : ${total_ganancia:,.2f}")
    print(f"Ticket Promedio por Compra     : ${ticket_promedio:,.2f}")
    print(f"Venta Más Alta                 : ${venta_max:,.2f}")
    print(f"Venta Más Baja                 : ${venta_min:,.2f}")
    print("-" * 60)

    # 4. Ventas por línea de producto
    print("\n4. VENTAS TOTALES POR LÍNEA DE PRODUCTO")
    print("-" * 60)
    ventas_producto = df.groupby('Product line')['Sales'].sum().sort_values(ascending=False)
    for producto, venta in ventas_producto.items():
        print(f"   • {producto:25} : ${venta:,.2f}")
    print("-" * 60)

    # 5. Rendimiento por sucursal y ciudad
    print("\n5. VENTAS POR SUCURSAL Y CIUDAD")
    print("-" * 60)
    ventas_sucursal = df.groupby(['City', 'Branch'])['Sales'].sum().sort_values(ascending=False)
    print(ventas_sucursal)
    print("-" * 60)

    # 6. Comportamiento del cliente
    print("\n6. GASTO PROMEDIO POR TIPO DE CLIENTE Y GÉNERO")
    print("-" * 60)
    gasto_cliente = df.groupby(['Customer type', 'Gender'])['Sales'].mean().unstack().round(2)
    print(gasto_cliente)
    print("-" * 60)

    # 7. Otros análisis útiles
    print("\n7. MÉTODOS DE PAGO MÁS USADOS")
    print("-" * 60)
    print(df['Payment'].value_counts())
    
    print("\n8. CALIFICACIÓN PROMEDIO")
    print("-" * 60)
    print(f"Rating promedio: {df['Rating'].mean():.2f} ⭐")

    # Conclusiones
    print("\n" + "="*80)
    print("CONCLUSIONES DEL ANÁLISIS EXPLORATORIO")
    print("="*80)
    print("• Se analizaron las principales variables del negocio.")
    print("• Se identificaron las líneas de producto más rentables.")
    print("• Se evaluó el rendimiento por sucursal y ciudad.")
    print("• Se analizó el comportamiento de los clientes según género y tipo.")
    print("• Se calcularon los principales indicadores financieros.")
    print("="*80)
    print("ANÁLISIS FINALIZADO EXITOSAMENTE")
    print("="*80)


if __name__ == "__main__":
    ruta = "data/SuperMarket Analysis_Limpio.csv"
    realizar_analisis_exploratorio(ruta)
actualizado analisis exploratorio con estadisticas
