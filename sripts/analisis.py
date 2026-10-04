import numpy as np
import pandas as pd

# 1. SIMULACIÓN: genera 30 clientes de una farmacia (semilla fija = reproducible)
rng = np.random.default_rng(2026)
df = pd.DataFrame({
    "id_cliente": np.arange(1, 31),
    "tiempo_entre_llegadas_min": rng.exponential(6.0, 30).round(2),
    "tiempo_servicio_min": rng.exponential(4.5, 30).round(2),
})
df.to_csv("datos/datos.csv", index=False)

# 2. VARIABLE PRINCIPAL: tiempo de servicio por cliente (minutos)
x = df["tiempo_servicio_min"]

# 3. ESTADÍSTICOS BÁSICOS
media, mediana = x.mean(), x.median()
desv = x.std(ddof=1)
resumen = {
    "n": len(x), "media": media, "mediana": mediana, "desv_est": desv,
    "varianza": x.var(ddof=1), "minimo": x.min(), "maximo": x.max(),
    "rango": x.max() - x.min(), "Q1": x.quantile(0.25), "Q3": x.quantile(0.75),
    "asimetria": x.skew(), "curtosis": x.kurt(),
}

# 4. OUTLIERS: Z-Score = (x - media) / desviación; atípico si |z| > 3
df["z_score"] = ((x - media) / desv).round(3)
outliers = df[df["z_score"].abs() > 3]
sospechosos = df[df["z_score"].abs() > 2]   # referencia: límite más estricto

# 5. SALIDA: imprime resultados para copiarlos al informe
print("ESTADÍSTICOS (tiempo_servicio_min)")
for k, v in resumen.items():
    print(f"  {k}: {v:.3f}")
print("\nOutliers |z|>3:", len(outliers))
print(outliers[["id_cliente", "tiempo_servicio_min", "z_score"]].to_string(index=False))
print("\nValores con |z|>2:", len(sospechosos))
print(sospechosos[["id_cliente", "tiempo_servicio_min", "z_score"]].to_string(index=False))
print("\nTiempo medio entre llegadas:", round(df["tiempo_entre_llegadas_min"].mean(), 3))
