from goto import with_goto

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000
	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. createDB	
	label. retorno1	
	Sra = Sra + 1	
	Ss0[Sra] = 2	
	goto. createDB2	
	label. retorno2	
	goto. end	
	
	label. createDB	
	t0 = True	
	t1 = 30	
	t2 = t0 == False	
	if  t2 : goto. L0	
	goto. L1	
	label. L0	
	print('ES MENOR A 20  ')	
	goto. L2	
	label. L1	
	print('ES MAYOR A 20  ')	
	label. L2	
	t3 = '*' != '+'	
	if t3: goto. L4	
	print('SUMA  ')	
	goto. L3	
	label. L4	
	t4 = '*' != '-'	
	if t4: goto. L5	
	print('RESTA  ')	
	goto. L3	
	label. L5	
	print('NO ES SUMA NI RESTA  ')	
	label. L3	
	goto. retorno	
	
	label. createDB2	
	t5 = True	
	t6 = 30	
	t7 = t5 == False	
	if  t7 : goto. L6	
	goto. L7	
	label. L6	
	print('ES MENOR A 20  ')	
	goto. L8	
	label. L7	
	print('ES MAYOR A 20  ')	
	label. L8	
	t8 = '*' != '+'	
	if t8: goto. L10	
	print('SUMA  ')	
	goto. L9	
	label. L10	
	t9 = '*' != '-'	
	if t9: goto. L11	
	print('RESTA  ')	
	goto. L9	
	label. L11	
	print('NO ES SUMA NI RESTA  ')	
	label. L9	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1	
	if Ssp == 2: goto. retorno2

	label .end
	return

main()
