import math
pi = 3.14159265359
rad=180/pi#[degrees]
D1=125/25.4#Diametro de paso de la shee[in]
w1=2000#velocidad de giro[rpm]
p=2.5#Relacion de velocidad
#p=(w1/w2)=(D2/D1)
D2=p*D1
vb=(D1*w1)/(2)#velocidad de la banda
#vb=(D2*w2)/(2)#velocidad de la banda
#Se selecciona la banda que se acerque a las especificaciones de potencia a las especificaciones de potencia la cuales dependende de modulo de elasticidad (estudiado por Thomas Young) del material con el que esten fabricadas y el segundo momento de inercia  
L=75#[inch/mm] Contitech V3/5VX750
L=2*C+1.57*(D2+D1)+(math.pow((D2-D1),2))/(4*C)
#O en primera instancia se propone una distancia de centros
#C=D1+D2
B=4*L-6.28*(D2+D1)
#Se y se re calcula la distancia C entre centros tal que cumpla
C=(B+math.sqrt(math.pow(B,2)-32*math.pow((D2-D1),2)))/(16)
L=2*C+1.57*(D2+D1)+(math.pow((D2-D1),2))/(4*C)
#La longitud S de "span" entre las dos poleas
S=math.sqrt(math.pow(C,2)-math.pow((D2-D1)/2))
#El angulo de contacto de la banda en cada polea es
tetha1=180-2*math.asin((D2-D1)/2*C)
tetha2=180+2*math.asin((D2-D1)/2*C)
#angule Vgroovie from 30 degrees to 42 degrees
