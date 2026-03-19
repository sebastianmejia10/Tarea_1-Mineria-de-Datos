import matplotlib.pyplot as plt
import sqlite3
import pandas as pd 
conexion = sqlite3.connect("datos_mision.db")

consulta = "SELECT Radio, Masa FROM exoplanetas;"
exoplanetas = pd.read_sql_query(consulta, conexion)
conexion.close()
print(exoplanetas)
