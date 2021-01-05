# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

print(j.extractTable('compiladores2','USUARIO'))
# create database
j.createDatabase('world')

j.createTable('world', 'cities',    4)

# create simple primary keys
j.alterAddPK('world', 'cities',    [0])


# insert data in cities
j.insert('world', 'cities', [1, 'Guatemala',    'Guatemala',    'GTM'])
j.insert('world', 'cities', [2, 'Cuilapa',      'Santa Rosa',   'GTM'])
j.insert('world', 'cities', [3, 'San Salvador', 'San Salvador', 'SLV'])
j.insert('world', 'cities', [4, 'San Miguel',   'San Miguel',   'SLV'])
         
# show all datap
print(j.extractTable('world','cities')) #SELECT


print(j.update('world','cities',{1:'Mexico', 3:'MX'},[1]));

print(j.extractTable('world','cities')) #SELECT
