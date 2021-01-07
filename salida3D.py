from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	pos = -1
	arr = [0] * 10000

	inter.procesar_funcion0()
	inter.procesar_funcion1()	
	ta0 = 'INICIO CALIFICACION FASE 2'	
	pos = pos + 1	
	arr[pos] = 1	
	goto. myFuncion	
	label. retorno1
	inter.procesar_funcion2()
	inter.procesar_funcion3()
	inter.procesar_funcion4()
	inter.procesar_funcion5()
	inter.procesar_funcion6()
	inter.procesar_funcion7()
	inter.procesar_funcion8()
	inter.procesar_funcion9()
	inter.procesar_funcion10()
	inter.procesar_funcion11()
	inter.procesar_funcion12()
	inter.procesar_funcion13()	
	ta1 = 'tbProducto'	
	ta2 = 8	
	pos = pos + 1	
	arr[pos] = 2	
	goto. ValidaRegistros	
	label. retorno2
	inter.procesar_funcion14()
	inter.procesar_funcion15()	
	ta1 = 'tbProductoUp'	
	ta2 = 8	
	pos = pos + 1	
	arr[pos] = 3	
	goto. ValidaRegistros	
	label. retorno3
	inter.procesar_funcion16()	
	pos = pos + 1	
	arr[pos] = 4	
	goto. CALCULOS	
	label. retorno4
	inter.procesar_funcion17()
	inter.procesar_funcion18()
	inter.procesar_funcion19()	
	pos = pos + 1	
	arr[pos] = 5	
	goto. sp_validainsert	
	label. retorno5	
	ta1 = 'tbbodega'	
	ta2 = 5	
	pos = pos + 1	
	arr[pos] = 6	
	goto. ValidaRegistros	
	label. retorno6
	inter.procesar_funcion20()	
	pos = pos + 1	
	arr[pos] = 7	
	goto. sp_validaupdate	
	label. retorno7
	inter.procesar_funcion21()	
	ta1 = 'tbbodega'	
	ta2 = 4	
	pos = pos + 1	
	arr[pos] = 8	
	goto. ValidaRegistros	
	label. retorno8
	inter.procesar_funcion22()
	inter.procesar_funcion23()
	inter.Reportes()	
	goto. end	
	
	label. myFuncion	
	print(ta0 )	
	goto. retorno	
	
	label. ValidaRegistros	
	t0 = 0	
	t1 = 0	
	t2 = ta1 == 'tbProducto'	
	if  t2 : goto. L0	
	goto. L1	
	label. L0	
	t0 = 2	
	t3 = ta2 == t0	
	if  t3 : goto. L3	
	goto. L4	
	label. L3	
	t1 = 1	
	goto. L5	
	label. L4	
	t1 = 0	
	label. L5	
	label. L1	
	t4 = ta1 == 'tbProductoUp'	
	if  t4 : goto. L6	
	goto. L7	
	label. L6	
	t0 = 2	
	t5 = ta2 == t0	
	if  t5 : goto. L9	
	goto. L10	
	label. L9	
	t1 = 1	
	goto. L11	
	label. L10	
	t1 = 0	
	label. L11	
	label. L7	
	t6 = ta1 == 'tbbodega'	
	if  t6 : goto. L12	
	goto. L13	
	label. L12	
	t0 = 2	
	t7 = ta2 == t0	
	if  t7 : goto. L15	
	goto. L16	
	label. L15	
	t1 = 1	
	goto. L17	
	label. L16	
	t1 = 0	
	label. L17	
	label. L13	
	print(t1 )	
	goto. retorno	
	
	label. CALCULOS	
	t8 = 0	
	t9 = 0	
	t10 = 0	
	t11 = 0	
	t8 = 2	
	t9 = 3	
	t10 = 4	
	t12 = t10 + 2	
	t10 = t12	
	t11 = 3	
	t11 = 4	
	t13 = t10 + t11	
	t14 = t13 / 2	
	t10 = t14	
	t15 = t10 > 1	
	if  t15 : goto. L18	
	goto. L19	
	label. L18	
	t10 = 20	
	goto. L20	
	label. L19	
	t10 = 10	
	label. L20	
	print(t10 )	
	goto. retorno	
	
	label. sp_validainsert
	inter.procesar_funcion24()
	inter.procesar_funcion25()
	inter.procesar_funcion26()
	inter.procesar_funcion27()
	inter.procesar_funcion28()	
	print('INSERT  ')	
	goto. retorno	
	
	label. sp_validaupdate	
	print('UPDATE  ')
	inter.procesar_funcion29()	
	goto. retorno	
	
	label. retorno	
	posR = arr[pos]	
	pos = pos - 1	
	if posR == 1: goto. retorno1	
	if posR == 2: goto. retorno2	
	if posR == 3: goto. retorno3	
	if posR == 4: goto. retorno4	
	if posR == 5: goto. retorno5	
	if posR == 6: goto. retorno6	
	if posR == 7: goto. retorno7	
	if posR == 8: goto. retorno8

	label .end
	return

main()
