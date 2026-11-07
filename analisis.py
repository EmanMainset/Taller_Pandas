import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)
    ventas_por_mes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    # TODO 8
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\n--- P1: Ingresos por categoría ---")
    print(ingresos)
    print(f"Respuesta: la categoría que más ingresos genera es {ingresos.index[0]} (${ingresos.iloc[0]:,.0f}). Criterio: suma de total.")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    # TODO 9
    canal = df.groupby("canal").agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
    print("\n--- P2: Ventas e ingresos por canal ---")
    print(canal)
    por_ingresos = canal["ingresos"].idxmax()
    por_cantidad = canal["ventas"].idxmax()
    print(f"Respuesta: por ingresos vende más {por_ingresos}; por cantidad de ventas, {por_cantidad}. Criterio principal: ingresos.")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    # TODO 10
    seg = df.groupby("segmento_cliente").agg(
        clientes=("id_cliente", "nunique"),
        compras=("id_venta", "count"),
        gasto_total=("total", "sum"),
    )
    seg["compras_por_cliente"] = seg["compras"] / seg["clientes"]
    seg["gasto_por_cliente"] = seg["gasto_total"] / seg["clientes"]
    print("\n--- P3: VIP vs Regular (promedios por cliente) ---")
    print(seg)
    mejor_c = seg["compras_por_cliente"].idxmax()
    mejor_g = seg["gasto_por_cliente"].idxmax()
    print(f"Respuesta: más compras por cliente: {mejor_c}; más gasto por cliente: {mejor_g}. Criterio: promedio por cliente, no totales.")


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    # TODO 11
    pagos = df["metodo_pago"].value_counts()
    print("\n--- P4: Método de pago ---")
    print(pagos)
    print(f"Respuesta: el método más usado es {pagos.index[0]} ({pagos.iloc[0]} ventas). Criterio: cantidad de ventas.")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    # TODO 12
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(["compras", "gasto_total"], ascending=False)
        .head(5)
    )
    print("\n--- P5: Top 5 clientes con más compras ---")
    print(top)
    print("Criterio: número de compras; gasto total como desempate.")


def ventas_por_mes(df):
    """Bonus: ventas por mes (to_period('M') separa abril de 2026 de abril de otros años)."""
    df = df.copy()
    df["mes"] = df["fecha_venta"].dt.to_period("M")
    por_mes = df.groupby("mes").agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
    print("\n--- Bonus: Ventas por mes ---")
    print(por_mes)

    # loc por etiqueta: fila del mes con más ingresos
    mejor_mes = por_mes["ingresos"].idxmax()
    print("Fila del mejor mes (con .loc):")
    print(por_mes.loc[mejor_mes])
    print(f"Respuesta: el mes que más vendió fue {mejor_mes} (${por_mes.loc[mejor_mes, 'ingresos']:,.0f}). Criterio: ingresos.")

    # iloc por posición: primer mes de la tabla
    print(f"Primer mes registrado (con .iloc): {por_mes.index[0]} -> {por_mes.iloc[0, 1]:,.0f}")

    # concat: unir la tabla mensual con su acumulado, lado a lado
    acumulado = por_mes[["ingresos"]].cumsum().rename(columns={"ingresos": "ingresos_acumulados"})
    print("Ventas por mes con acumulado (concat):")
    print(pd.concat([por_mes, acumulado], axis=1))
