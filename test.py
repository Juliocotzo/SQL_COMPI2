# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

j.createTable('compiladores2','materia',3)
print(j.showDatabases())
print(j.showTables('compiladores2'))