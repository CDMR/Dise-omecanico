import math
#import numpy as np
x=[1,6,1];
pnew=0;
#se define una función que como argumento acepta grados
def sen(grados):
    return math.sin(math.radians(grados))
relacionesdevelocidad=[3,3.2,2.7]#relacion de veolocidad [p]
tetha=20#angulo de presion
for p in relacionesdevelocidad:
    zf=(2*(1/p))/(-1+math.sqrt(1+((1/p)**2+2*(1/p))*sen(tetha)**2))#numero de dientes en el piñon
    zp=math.ceil(zf)#se redondea hacia arriba el numero de dientes
    zca=(zp*p)#numero de dientes en <corona/engrane>(numero de dientes en el piññon (zp)* relacion de velocidad(p))
    zc=math.ceil(zca)#se redondea hacia arriba el numero de dientes
    x[pnew]=[zc/zp,zp,zc]#relacion de veolcidad, dientes en el piñon, dientes en la corona
    pnew=pnew+1
print (x)
