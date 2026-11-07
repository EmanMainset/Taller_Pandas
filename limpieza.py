import pandas as pd


def _quitar_espacios(df):
    df = df.copy()
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip()
    return df


def limpiar_clientes(clientes):
    print("\n[clientes] Nulos por columna:")
    print(clientes.isnull().sum())
    print(f"[clientes] Filas duplicadas: {clientes.duplicated().sum()}")

    clientes = _quitar_espacios(clientes)

    # TODO 1: ciudad en formato título
    clientes["ciudad"] = clientes["ciudad"].str.title()

    # TODO 2: eliminar duplicados y reiniciar el índice
    clientes = clientes.drop_duplicates().reset_index(drop=True)
    print(f"[clientes] Duplicados después: {clientes.duplicated().sum()} | Nulos después: {clientes.isnull().sum().sum()}")

    print(f"[clientes] Filas tras limpieza: {len(clientes)}")
    return clientes


def limpiar_ventas(ventas):
    print("\n[ventas] Nulos por columna:")
    print(ventas.isnull().sum())
    print(f"[ventas] Filas duplicadas: {ventas.duplicated().sum()}")

    ventas = _quitar_espacios(ventas)

    # TODO 3: rellenar nulos de producto (no dropna: la venta tiene un total real)
    ventas["producto"] = ventas["producto"].fillna("Sin especificar")

    # TODO 4: fecha_venta a datetime (formato AAAA-MM-DD)
    ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"], format="%Y-%m-%d", errors="coerce")

    # TODO 5: eliminar duplicados y reiniciar el índice
    ventas = ventas.drop_duplicates().reset_index(drop=True)
    print(f"[ventas] Duplicados después: {ventas.duplicated().sum()} | Nulos después: {ventas.isnull().sum().sum()}")
    print("[ventas] Tipo de fecha_venta:", ventas["fecha_venta"].dtype)
    ventas.info()

    print(f"[ventas] Filas tras limpieza: {len(ventas)}")
    return ventas


def limpiar_datos(clientes, ventas):
    return limpiar_clientes(clientes), limpiar_ventas(ventas)
