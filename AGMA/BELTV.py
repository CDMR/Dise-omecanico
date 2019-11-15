import math
pi = 3.14159365359
rad=180/pi#[degrees]
D1=0.1618#Diametro de paso de la shee[in]
w1=0.618#velocidad de giro[rpm]
#vb=(D1*w1)/(2)#velocidad de la banda
#vb=(D2*w2)/(2)#velocidad de la banda
#Relacion de velocidad
#(w1/w2)=(D2/D1)


B=4*L-6.28*(D2+D1)
#Distancia entre centros
C=(B+math.sqrt(math.pow(B,2)-32*math.pow((D2-D1),2)))/(16)#C=(D2-D1)/2
#La longitud de paso L
L=2*C+1.57*(D2+D1)+(math.pow((D2-D1),2))/(4*C)

#El angulo de contacto de la banda en cada polea es
tetha1=180-2*math.asin((D2-D1)/2*C)
tetha2=180+2*math.asin((D2-D1)/2*C)
