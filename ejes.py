#EJE de giro de seccion circular solido de
d=1.618#diametro[mm]
l=10#de longitud [mm]
#Teorema de ejes paralelos para cambiar de pocision en el plano xy el eje de giro
#Teorema de ejes perpendiculares Jo=Ix+Iy para calcular el momento plar de inercia
J0=(0.5*pi)*(d/2)**4#Momento polar de inercia
Ix=(0.25*pi)*(d/2)**4#Momento de inercia de area o segundo momento de inercia (simetricos Ix=Iy )
M=F*l#Momento flector
sig=M*(d/2)/Ix#esfuerzo normales max por flexion
Ttor=(Tpar*(d/2))/J0#esfuerzo maximo por torsion
Tmax=((sig)**2+Ttor**2)**(1/2)#torsion y flexion combinados
FS=2#Factor de Seguridad
Ru=#Resistenciaa ultima[Kg/mm<sup>2</sup>]
Tadm=(Ru/2)/FS#Cortante maxio admisible
