# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

# drop all databases if exists
j.dropAll()

# create database
j.createDatabase('world')

# create tables
j.createTable('world', 'countries', 4)
j.createTable('world', 'cities',    4)
j.createTable('world', 'languages', 4)

# show all data
j.showCollection()