# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j


# create database
j.createDatabase('world')

# create tables
j.createTable('world', 'countries', 4)
j.createTable('world', 'cities',    4)
j.createTable('world', 'languages', 4)

# create simple primary keys
j.alterAddPK('world', 'countries', [0])
j.alterAddPK('world', 'cities',    [0])
j.alterAddPK('world', 'languages', [0, 1])

j.insert('compiladores2', 'tbUSUARIO' ,[1, 'Juliocotzo', 'password', 12345678, None, None])

'''
# insert data in cities
j.insert('world', 'cities', [1, 'Guatemala',    'Guatemala',    'GTM'])
j.insert('world', 'cities', [2, 'Cuilapa',      'Santa Rosa',   'GTM'])
j.insert('world', 'cities', [3, 'San Salvador', 'San Salvador', 'SLV'])
j.insert('world', 'cities', [4, 'San Miguel',   'San Miguel',   'SLV'])
         
# inser data in languages
j.insert('world', 'languages', ['GTM', 'Spanish', 'official',  64.7])
j.insert('world', 'languages', ['SLV', 'Spanish', 'official', 100.0])

# show all datap
print(j.extractTable('world','countries')) #SELECT
j.showCollection()
'''