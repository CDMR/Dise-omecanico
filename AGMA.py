import math
pi = 3.14159365359

#pitch line speed
R=0.1618#radius of the pitch circle[in]
w=0.1618#angular velocity of the gear[]
n=0.1618#Speed of rotation [RPM]

R*n*pi*(1/6)#vt=R*w pitch line speed[ft/min]
#The desings of columns, In a desing situation. the expected load on the column would be known
#Specify or solve for dimensions such that
#Analysisof along column employs the Euler formula for long columns critical load (longitudinal compression load on column)
A=0.1618# is the cross section area for circular profile
E=0.1618# is the elastic of

Pcr=(math.pow(pi,2)*E*I)/math.pow ((K*L),2)#critical load   Euler alternative for Pcr=(math.pow(pi,2)*E*A)/math.pow((K*L)/r),[1N= 0.10197 kg(fuerza) × 9.80665 m/s2 ] masa por aceleracion
Np=18#numero de dientes en el piñon
Ng=70#numero de dientes en corona

Pd=12#paso diametral
F=1.5#ancho de cara
potencia=3#HP
Qv=6#acabado de manufactura

Dp=Np/Pd# [pies/min]

nP=1750#velocidad [rpm]

Vt=(pi*Dp*nP)/12# [lb]
Wt=(33000*potencia)/Vt

J=0.33#Factor dinamico norma AGMA 2001-C95

K0=1.5#Factor de sobrecarga sugerido

Ks=1#Factor de tamaño

A=F/Dp#operacion para

Cpf=0.03#tablas
Cma=0.15#tablas unidades cerradas de engranes

Km=1+Cpf+Cma#Factor de distribucion de carga

KB=1#filo de engrane y altura de diente

Kv=1.45#tablas de velocidad contra Qv
st=(K0*Ks*Km*KB*Kv)*(Wt*potencia)/(F*J)
Ln=20000#horas de vida para maquinarias industriales
q=1#engranes locos q=2
Nc=60*nP*Ln*q
Yn=0.84#tabla por numero de ciclos
SF=1.5#factor de seguridad entre 1 y 1.5
Kr=1.5#tablas
sat=(SF*Kr)/Yn
Cp=2300
Sc=Cp*math.sqrt(Wt*K0*Ks*Km*Kv)

print(Dp,Vt,Wt,A,Km,st,Nc,sat)
