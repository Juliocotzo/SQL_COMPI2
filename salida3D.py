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
	if  t1 : goto. L0	
	goto. L1	
	label. L0	
	print(ta0 )	
	goto. L2	
	label. L1	
	print('ES MAYOR A 20  ')	
	label. L2	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1

	label .end
	return

main()
