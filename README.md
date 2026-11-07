# Taller práctico: análisis de datos con Pandas

Programa de consola que lee datos de ventas y clientes, los limpia, los une y los analiza. Se ejecuta desde un menú en la terminal, y cada opción corresponde a un módulo que vas a completar paso a paso.

Recuerda consultar la guía adjunta en PDF donde se te dará el paso a paso del trabajo.

## Requisitos

- Python 3.10 o superior
- Git (para clonar el repositorio)
- Conocimientos básicos de variables, listas y funciones

## Cómo empezar

1. Clona el repositorio y entra a la carpeta del proyecto:

   ```
   git clone <URL-DEL-REPOSITORIO>
   cd <NOMBRE-DE-LA-CARPETA>
   ```

2. Crea y activa un ambiente virtual. Las instrucciones completas, para Windows y Mac/Linux, están en `LEEME_ambiente.txt`.

3. Instala las librerías:

   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```
   python main.py
   ```

Ejecuta siempre los comandos desde la carpeta del proyecto. Los módulos buscan los archivos a partir de su ubicación.

## Estructura del proyecto

```
├── main.py            Menú principal. No lo modifiques.
├── carga.py           Lee los CSV. Ya está completo.
├── limpieza.py        Limpia clientes y ventas. TODO 1 a 5.
├── merge.py           Valida y une las tablas. TODO 6 y 7.
├── analisis.py        Responde las preguntas de negocio. TODO 8 a 12.
├── graficos.py        Dibuja dos gráficos sencillos. TODO 13 y 14.
├── exploracion.py     Ejemplos de indexación, .loc, .iloc y concat. Se ejecuta por separado.
├── requirements.txt   Versiones de las librerías.
├── LEEME_ambiente.txt Pasos para crear el ambiente virtual.
└── Data/
    ├── raw/           Datos originales (cliente.csv, ventas.csv). No los modifiques.
    └── processed/     Resultados que genera el programa.
```

## Menú

| Opción | Qué hace |
|---|---|
| 1 | Carga los archivos CSV |
| 2 | Limpia los datos |
| 3 | Valida y une las tablas con merge |
| 4 | Muestra el análisis y las respuestas del desafío |
| 5 | Dibuja los gráficos de introducción |
| 6 | Sale del programa |

Las opciones se usan en orden: primero cargar (1), luego limpiar (2), después unir (3) y finalmente analizar (4) o graficar (5).

## Cómo completar el taller

1. Abre el archivo indicado en cada TODO. Cada función tiene un docstring con pistas.
2. Completa el TODO y ejecuta `python main.py` para probar la opción correspondiente.
3. Usa `exploracion.py` para practicar indexación, `.loc`, `.iloc` y `concat()` antes de aplicarlos en tu código.

Las funciones que aún no completaste no dan error: devuelven los datos sin cambios, así que el menú siempre funciona.

## Autor

**Nombre:** Emanuel Restrepo Ceballos

## Respuestas al desafío final

Resultados tomados de la opción 4 del menú (`python main.py`, opciones 1 -> 2 -> 3 -> 4).

1. **¿Qué categoría genera más ingresos?** Tecnologia, con $14.290.000 (Hogar $3.653.000, Papeleria $749.000, Accesorios $484.000). *Criterio:* suma de `total` por categoría.
2. **¿Qué canal vende más?** Online: 35 ventas y $14.669.000, frente a Tienda con 33 ventas y $4.507.000. *Criterio:* ingresos (y también gana en cantidad de ventas).
3. **¿Los clientes VIP compran más que los Regulares?** Sí, aunque con diferencia pequeña. VIP: 1,21 compras y $336.083 de gasto por cliente; Regular: 1,08 compras y $308.611 por cliente. *Criterio:* promedio por cliente (24 VIP vs 36 Regular), no totales.
4. **¿Qué método de pago es el más usado?** Efectivo, con 30 ventas (Tarjeta 25, Transferencia 13). *Criterio:* cantidad de ventas por método de pago.
5. **¿Cuáles son los cinco clientes con más compras?** Todos con 2 compras; el desempate es el gasto total: Nicolas Cardona ($2.515.000), Matias Rodriguez ($1.278.000), Mia Quintero ($1.090.000), Luna Montoya ($1.007.000) y Luis Perez ($730.000). *Criterio:* número de compras y gasto total como desempate.

**Bonus:** abril de 2026 fue el mes que más vendió (60 ventas, $18.234.000) frente a mayo de 2026 (8 ventas, $942.000).

## Entregables

El detalle (explicaciones, evidencias y código) está en `INFORME_ENTREGABLES.md`. Las capturas están en la carpeta `images/` y los gráficos en `images/graficos/`.
