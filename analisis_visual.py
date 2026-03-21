import matplotlib.pyplot as plt
import sqlite3
import pandas as pd 
conexion = sqlite3.connect("datos_mision.db")

consulta = "SELECT Radio, Masa FROM exoplanetas;"
exoplanetas = pd.read_sql_query(consulta, conexion)
conexion.close()

radio = np.linspace(0,90,1000)
densidad_tierra = 5.51
masa_rocoso = (3/5.51)*(4*np.pi/3)*(radio**3)

masa_gaseoso = (1/5.51)*(4*np.pi/3)*(radio**3)

plt.scatter(exoplanetas["Masa"], exoplanetas["Radio"],color='black', alpha=0.7)
plt.plot(masa_rocoso, radio, linestyle="--", color="red", label = "Frontera planetas rocosos (ρ ≈ 3 g/cm³)")
plt.plot(masa_gaseoso, radio, linestyle="--", color="blue", label = "Frontera planetas gaseosos (ρ ≈ 1 g/cm³)")

plt.fill_betweenx(radio, 0, masa_gaseoso,
                  color='blue', alpha=0.2,
                  label="Planetas gaseosos")

plt.fill_betweenx(radio, masa_gaseoso, masa_rocoso,
                  color='yellow', alpha=0.2,
                  label="Región de transición")

plt.fill_betweenx(radio, masa_rocoso, 30000,
                  color='red', alpha=0.2,
                  label="Planetas rocosos")

plt.xlim(0, 30000)
plt.ylim(0, 90)
plt.ylabel("Radio")
plt.xlabel("Masa")
plt.title("Masa vs Radio")
plt.grid(True)
plt.legend()
plt.show()
