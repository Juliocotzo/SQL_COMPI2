from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000
	
	ta0 = 'hola'	
	ta1 = 2	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. ValidaRegistros	
	label. retorno1
	print(inter.Reportes())	
	goto. end	
	
	label. ValidaRegistros	
	t0 = 0	
	t1 = 0	
	t2 = ta0 == 'hola'	
	if  t2 : goto. L0	
	goto. L1	
	label. L0	
	t0 = 2	
	t3 = ta1 == t0	
	if  t3 : goto. L3	
	goto. L4	
	label. L3	
	t1 = 1	
	goto. L5	
	label. L4	
	t1 = 0	
	label. L5	
	label. L1	
	print(t1 )	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1

	label .end
	return

main()
