# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

# create database
print(j.showDatabases())
print(j.showDatabases())

print(j.alterDatabase('world','hola1'))
print(j.showDatabases())