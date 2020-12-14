# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

# create database
print(j.showDatabases())
j.createDatabase('world')
j.createDatabase('world1')
j.createDatabase('world2')
print(j.showDatabases())
print(j.dropDatabase('worldd1'))
print(j.showDatabases())