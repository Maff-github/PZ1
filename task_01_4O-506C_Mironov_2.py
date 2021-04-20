print ('Импорт требуемых библиотек')
import numpy as np
import matplotlib.pyplot as pl
import os
print ('Создание папки results')
if not os.path.exists('results'):
    os.mkdir('results')
print ('Папка создана')
x=np.linspace(-5,5,500)
y = -20*np.exp(-0.2*np.sqrt(0.5*x**2))-np.exp(0.5*
                (np.cos(2*np.pi*x+1)))+np.e+20           
print ('Построение графика заданной функции y=f(x)')
pl.title('График заданной функции y=f(x)')
pl.plot(x,y)
pl.xlabel('x')
pl.ylabel('f(x)')
pl.grid()
pl.show()
print ('Создание файла заданного формата')
p = os.path.join(os.getcwd(),'results','task_01_4O-506C_Mironov_02.csv')
print ('Файл создан')
with open(p, 'w') as f:
    f.write('№ x{0:4} y(x) \n'.format(''))
    
    for i in range(0,500):
        f.write('{0}{1}{2}{3:4}{4}{5}{6} \n'.format(str(i),',','\t',str(x[i]),',',
                                              '\t',str(y[i])))
print ('Результат работы сохранен в results\\task_01_4O-506C_Mironov_02.csv')

