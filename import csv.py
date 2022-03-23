"""import pandas as pd
import wrap
data = pd.read_csv("C:/Users/Felipe/OneDrive/Escritorio/Doc la gran colombia/Programas python/Respuestas de texto/textos.csv",header=0)
df = pd.DataFrame(data)
print(df)"""

import pandas as pd
import wrap

archivo = open('C:/Users/Felipe/OneDrive/Escritorio/Doc la gran colombia/Programas python/Respuestas de texto/nuevo.txt',mode='r',encoding='utf-8')
texto = str(archivo.read().splitlines())
archivo.close()
print(type(texto))
print(texto)

