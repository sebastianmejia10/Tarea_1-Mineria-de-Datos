import pandas as pd
import numpy as np
import sqlite3

exoplanetas = pd.read_csv("exoplanetas.csv")
exoplanetas.columns = ["Nombre","Radio","Masa"]
conn = sqlite3.connect("datos_mision.db")
exoplanetas.to_sql('exoplanetas', conn, if_exists='replace', index=False)
conn.close()
 
