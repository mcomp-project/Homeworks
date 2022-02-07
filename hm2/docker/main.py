# calculating the sum of each row and each column of the matrix. Complete it with the column that contains the sums of the elements of the rows and a row whose elements are the sums of the elements of the columns.
import random
import numpy as np


m = np.array([[random.randint(0,10) for x in range(4)] for y in range(4)]) #list comprehension 
sum_c = [sum(x[z] for x in m) for z in range(len(m[0]))] #scheiße ich hab 1,5 Stunden gebraucht um diese Zeile zu schreiben
sum_r = [sum(x) for x in m]
print(f'\nThe matrix:\n{m}\nSum of columns:{sum_c}\nSum of rows:{sum_r}')         
