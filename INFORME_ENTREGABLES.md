# Informe de entregables - Taller Pandas

Las imágenes están en `images/` (salida real de cada comando, renderizada como imagen de terminal).

## Entregable 0 - Ambiente virtual
`images/entregable0_ambiente_venv_activo_e_instalacion_librerias.png`
Ambiente creado con `python3 -m venv venv`, activado y librerías instaladas con `pip install -r requirements.txt` (pandas 3.0.2, matplotlib 3.10.8, seaborn 0.13.2).

## Entregable 1 - Exploración
- `images/entregable1_ventas_shape_info_describe.png`: `.shape` = (68, 10). La columna `producto` tiene **67** valores no nulos de 68 (falta 1).
- `images/entregable1_clientes_shape_info_describe.png`: `.shape` = (60, 5), sin nulos.
- `images/entregable1_exploracion_py_salida_completa.png`

**¿Por qué `.iloc[2, 6]` devuelve el total de V003?** Tras `set_index("id_venta")`, `id_venta` deja de ser columna y pasa a ser el índice. Las columnas quedan: 0 `id_cliente`, 1 `fecha_venta`, 2 `producto`, 3 `categoria`, 4 `cantidad`, 5 `precio_unitario`, 6 `total`. La fila de posición 2 es V003 (V001=0, V002=1, V003=2). Entonces `.iloc[2, 6]` es la fila V003, columna `total` = 520000, igual que `.loc["V003", "total"]`.

## Entregable 2 - Limpieza
`images/entregable2_menu_opcion1_y_2_limpieza_antes_y_despues.png`

Problemas encontrados y tratamiento:
- **Nulos:** `ventas.producto` tenía 1 nulo (venta V004, con total de 780000). Se rellenó con `fillna("Sin especificar")` y **no** con `dropna()`, porque eliminar la fila borraría una venta real y alteraría los ingresos de Tecnología y del canal Online. Clientes no tiene nulos.
- **Duplicados:** 0 en ambas tablas (se aplicó `drop_duplicates().reset_index(drop=True)` de todos modos).
- **Texto:** se aplicó `.str.strip()` a todas las columnas de texto y `.str.title()` a `ciudad`; no se detectaron espacios ni inconsistencias en los valores (`value_counts()` mostró categorías, canales, métodos de pago y ciudades consistentes).
- **Fechas:** `fecha_venta` venía como texto (formato AAAA-MM-DD); se convirtió con `pd.to_datetime(..., format="%Y-%m-%d", errors="coerce")`. Tras limpiar, `.info()` muestra `datetime64[us]`.

## Entregable 3 - Merge y análisis
- `images/entregable3_menu_opcion3_validacion_y_merge.png`
- `images/entregable3_menu_opcion4_analisis_completo.png`

**¿Por qué el merge tiene 14 columnas?** Ventas tiene 10 columnas y clientes 5. Ambas comparten `id_cliente`, que aparece una sola vez en el resultado: 10 + 5 - 1 = 14. Las filas se mantienen en 68 porque `how="left"` conserva todas las ventas y `validate="m:1"` garantiza que cada cliente aparece una sola vez (sin duplicar ventas).

El código está en `limpieza.py`, `merge.py` y `analisis.py`.

## Entregable 4 - Gráficos
- `images/graficos/ventas_por_categoria.png`
- `images/graficos/ventas_por_canal.png`
- `images/entregable4_menu_opcion5_graficos.png`
- `images/entregable4_archivos_png_generados.png`

Código en `graficos.py` (TODO 13 y 14).

## Bonus - Ventas por mes
| mes | ventas | ingresos |
|---|---|---|
| 2026-04 | 60 | 18.234.000 |
| 2026-05 | 8 | 942.000 |

El mes que más vendió fue **abril de 2026** (por ingresos y por cantidad de ventas). Se usó `to_period("M")`; la tabla está en `ventas_por_mes()` de `analisis.py` y se imprime con la opción 4.
