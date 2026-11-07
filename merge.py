from pathlib import Path

import pandas as pd

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """
    # TODO 6: validaciones
    print("\n[merge] Validación previa:")
    ok = True

    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("  X Falta la columna id_cliente en alguno de los dataframes.")
        return False
    print("  OK  La columna id_cliente existe en ambos dataframes.")

    repetidos = clientes["id_cliente"].duplicated().sum()
    if repetidos > 0:
        print(f"  X Hay {repetidos} id_cliente repetidos en clientes.")
        ok = False
    else:
        print("  OK  No hay id_cliente repetidos en clientes.")

    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print(f"  X Tipos distintos: clientes={clientes['id_cliente'].dtype}, ventas={ventas['id_cliente'].dtype}")
        ok = False
    else:
        print(f"  OK  Mismo tipo de dato en ambos: {clientes['id_cliente'].dtype}")

    sin_cliente = (~ventas["id_cliente"].isin(clientes["id_cliente"])).sum()
    print(f"  Ventas sin cliente asociado: {sin_cliente}")
    return ok


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv."""
    # TODO 7: validar, hacer el merge, guardar el CSV y devolver el dataframe.
    if not validar_premerge(clientes, ventas):
        print("[merge] La validación falló; no se realizó el merge.")
        return None

    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "merge.csv", index=False)

    print(f"\n[merge] Ventas: {ventas.shape} | Clientes: {clientes.shape} | Merge: {df.shape}")
    print(f"[merge] Columnas: {ventas.shape[1]} + {clientes.shape[1]} - 1 (id_cliente en común) = {df.shape[1]}")
    print(f"[merge] Guardado en {PROCESSED / 'merge.csv'}")
    print(df.head())
    return df
