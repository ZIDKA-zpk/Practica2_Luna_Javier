# Práctica 2 - Formulación y análisis preliminar de un sistema real

**Caso:** tiempo de servicio en el mostrador de una farmacia (30 clientes simulados).
**Estudiante:** Luna Quisbert Javier Rodrigo

## Estructura
- `datos/datos.csv`: 30 observaciones (id, tiempo entre llegadas, tiempo de servicio).
- `scripts/analisis.py`: genera los datos, calcula estadísticos y detecta outliers con Z-Score.
- `reporte/informe.txt`: informe técnico con los 10 puntos requeridos.

## Ejecución
```bash
pip install numpy pandas
python scripts/analisis.py
```
Ejecutar desde la carpeta raíz del proyecto.

## Resultado resumido
Media de servicio 5.11 min, sin outliers (|Z| > 3), utilización del mostrador ≈ 86 %.
