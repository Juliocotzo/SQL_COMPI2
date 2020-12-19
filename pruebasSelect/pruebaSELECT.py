import random


arraySelect = [
    ['id_usuario','nombre','apellido'],
    [201503392,'MYNOR','MOLINA'],
    [201503421,'JORGE','VASQUEZ'],
    [201503442,'YADIRA','FERRER'],
    [201503484,'ANDREA','DUARTE']
]

#print(arraySelect)

def getPosition(ts,id):    
    pos = ts[0].index(id)
    return pos

def ResolverEXP(exp,ts_):
    #print('HOLA')
    pos = getPosition(ts_,'id_usuario')
    print(ts_[1][pos])
    return random.randint(0,1)



array_salida = []
array_salida.append(arraySelect[0])


i = 1
while i < len(arraySelect):
    
    arrayTS = []
    arrayTS.append(arraySelect[0])
    arrayTS.append(arraySelect[i])
    #print(arrayTS)
    val = ResolverEXP(1,arrayTS)

    if val == 1:
        array_salida.append(arraySelect[i])
    i+=1

print(array_salida)


