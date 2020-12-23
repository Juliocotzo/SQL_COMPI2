import numpy as np

import math
'''arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6,7], [7, 8,10]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr[0][2])

print([1,2,3,5])'''
   
'''a = np.array([(3, 2), (6, 2), (3, 6), (3, 4), (5, 3)])

ind = np.lexsort((a[:,1],a[:,0]))    

a[ind]

print(a[ind])'''


'''a = np.array([[2, 'LopDlMa', 'passwordLop', '653497674', 'Monamon', 25], [3, 'azurdiajonatan', 'passwordAzu', '305539638', 'Smach Mean Chey', 25], [4, 'mdmata20', 'passwordMd', '512175902', 'El Puente', 20], [5, 'franciscolezana', 'Fpassword', '232979832', 'Luobuqiongzi', 21]])
dt = [tuple(['id_ususario', a.dtype]),tuple(['usuario', a.dtype]),tuple(['password', a.dtype]),tuple(['telefono', a.dtype]),tuple(['direccion', a.dtype]),tuple(['edad', a.dtype])]
b = a.ravel().view(dt)
b.sort(order=['id_usuario'])

print(b)'''

print(math.degrees(math.atan2(20,10)))