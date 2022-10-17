#Llamando a funciones y librerias de python
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print (a)

a0=np.ones((3,3))
print(a0)

import pandas as pd

d={'a':1, 'b':2, 'c':3}
ser=pd.Series(data=d, index=['a','b','c'], name='columna')
print(ser)