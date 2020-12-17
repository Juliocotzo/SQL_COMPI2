import tc as TC
from  expresiones import * 

tc_global = TC.TablaDeTipos()

'''variable = TC.Tipo('Compi2','usuario','id_usuario','varchar(50)',None,None,None,[OPCIONES_CONSTRAINT.FOREIGN,OPCIONES_CONSTRAINT.NOT_NULL])
tc_global.agregar(variable)'''
buscar = tc_global.obtenerReturn('Compi2','usuario','id_usuario')
'''
variable1 = TC.Tipo('Compi2','usuario2','id_usuario','varchar(50)',None,None,None,[OPCIONES_CONSTRAINT.FOREIGN,OPCIONES_CONSTRAINT.NOT_NULL])
tc_global.agregar(variable1)
variable1 = TC.Tipo('Compi2','usuario2','usuario','varchar(50)',None,None,None,[OPCIONES_CONSTRAINT.FOREIGN,OPCIONES_CONSTRAINT.NOT_NULL])
tc_global.agregar(variable1)'''

if buscar != False:
    tempA = buscar.listaCons
    tempA.remove(OPCIONES_CONSTRAINT.FOREIGN)
    print(tempA)
    variable2 = TC.Tipo('Compi2','usuario','id_usuario','varchar(60)',None,None,None,tempA)
    tc_global.actualizar(variable2,'Compi2','usuario','id_usuario')
else:
    variable = TC.Tipo('Compi2','usuario','id_usuario','varchar(50)',None,None,None,[OPCIONES_CONSTRAINT.FOREIGN,OPCIONES_CONSTRAINT.NOT_NULL])
    tc_global.agregar(variable)
#tc_global.eliminarTabla('Compi2','usuario2')
#tc_global.eliminarID('Compi2','usuario2','id_usuario')
#tc_global.eliminarDatabase('Compi2')

i = 0
while i < len(tc_global.tipos):
    j = 0
    while j < len(tc_global.tipos[i].listaCons):
        print(str(i+1),str(tc_global.tipos[i].database) ,str(tc_global.tipos[i].tabla),str(tc_global.tipos[i].id),str(tc_global.tipos[i].tipo),str(tc_global.tipos[i].restriccion),str(tc_global.tipos[i].referencia),str(tc_global.tipos[i].tablaRef),tc_global.tipos[i].listaCons[j])
        j+=1
    i += 1