from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000
	
	ta0 = 17	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. suma	
	label. retorno1
	print(inter.Reportes())	
	goto. end	
	
	label. suma	
	t0 = 10	
	t1 = ta0 < 20	
	t2 = t0 > 5	
	t3 = t1 and t2	
	if  t3 : goto. L0	
	goto. L1	
	label. L0	
	print(ta0 )	
	t4 = ta0 + 1	
	ta0 = t4	
	ta0 = ta0	
	Sra = Sra + 1	
	Ss0[Sra] = 2	
	goto. suma	
	label. retorno2	
	goto. L2	
	label. L1	
	print('ES MAYOR A 20  ')	
	label. L2	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1	
	if Ssp == 2: goto. retorno2

	label .end
	return

main()
