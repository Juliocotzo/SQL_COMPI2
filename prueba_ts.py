import ts as TS
ts_global = TS.TablaDeSimbolos()
ts1 = TS.Simbolo('Compi2','Database',0,None)
ts3 = TS.Simbolo('Usuario','Tabla',4,'Compi2')
ts4 = TS.Simbolo('Usuario3','Tabla',4,'Compi2')
ts5 = TS.Simbolo('usuarioNull','Constraint',0,'Usuario')

ts_global.agregar(ts1)
ts_global.agregar(ts3)
ts_global.agregar(ts4)
ts_global.agregar(ts5)

tspp = ts_global.obtener('Compi2',None)
tsss = TS.Simbolo('Compiladores2',tspp.tipo,tspp.valor,tspp.ambito)
ts_global.actualizarDB(tsss,tspp.id)
ts_global.actualizarDBTable(tspp.id,tsss.id)

'''ts3 = TS.Simbolo('Compi4','Database',0,None)
ts_global.actualizarDB(ts3,'Compi2')

ts_global.actualizarDBTable('Compi2','Compi3')'''
'''
#print(ts_global.obtenerDb('Compi2'))

ts_temp = ts_global.obtener('Usuario','Compi3')
ts_nuevo = TS.Simbolo(ts_temp.id,ts_temp.tipo,ts_temp.valor+1,ts_temp.ambito)
ts_global.actualizarValorIdTable(ts_nuevo,ts_temp.id,ts_temp.ambito)


ts_temp1 = ts_global.obtener('Usuario','Compi3')
ts_nuevo1 = TS.Simbolo('Usuario',ts_temp1.tipo,ts_temp1.valor+1,ts_temp1.ambito)
ts_global.actualizarValorIdTable(ts_nuevo1,ts_temp1.id,ts_temp1.ambito)

ts_temp2 = ts_global.obtener('usuarioNull','Usuario')
ts_nuevo2 = TS.Simbolo('ConstrintNuevo',ts_temp2.tipo,0,ts_temp2.ambito)
ts_global.actualizarValorIdTable(ts_nuevo2,ts_temp2.id,ts_temp.ambito)


#ts_global.deleteDatabase('Compi3')
'''
for tss in ts_global.simbolos:
    print (tss.id,tss.tipo,tss.valor,tss.ambito)

