#!/usr/bin/env python
# coding: utf-8

# # 2024-A LTIN Analítica de Datos
# # Sanchez Salazar Atziri Yoseline 0009-0004-4794-0822
# # 04 de marzo, 2024
# # 1er Evaluación Parte II
# 
# 

# In[70]:


import pandas as pd  #Importa la librería Pandas para el manejo de datos
import seaborn as sns # Seaborn para la visualización de datos
import matplotlib.pyplot as plt # Matplotlib para la visualización de datos

# Cargar los datos del archivo Data.scsv en un DataFrame
data = pd.read_csv('Data.csv')

# Eliminar filas con valores faltantes en el DataFrame
data.dropna(inplace=True)

# Establecer un estilo de gráfica
sns.set(style='whitegrid')


# In[72]:


# Crear la gráfica utilizando seaborn y matplotlib
# Crear una figura con un tamaño de 12 pulgadas de ancho por 8 pulgadas de alto
plt.figure(figsize=(12, 8))

sns.scatterplot(x='Age', y='Salary', hue='Country', style='Purchased', s=100, palette='Dark2', alpha=0.8, data=data)
plt.title('Relación entre Edad y Salario por País') # Establecer el título del gráfico
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend(title='Country', fontsize='large') # Etiqueta 'País' y ajustar el tamaño de la fuente
plt.tight_layout() # Ajustar el diseño de la gráfica

# Guardar la gráfica como un archivo PDF
plt.savefig('grafica_con_purchased_mejorada.pdf')

# Mostrar la gráfica en el notebook
plt.show()


# In[ ]:




