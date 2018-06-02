import os
import RPi.GPIO as GPIO             #Importamos a libraria GPIO
import time                         #Importamos time (time.sleep)
GPIO.setmode(GPIO.BCM)              #Colocamos a placa em modo BCM
GPIO_TRIGGER = 20                   #Usamos o pin GPIO 20 como TRIGGER
GPIO_ECHO    = 21                   #Usamos o pin GPIO 21 como ECHO
GPIO.setwarnings(False)             #Desabilitando warnings
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)   #Configuramos Trigger como saida
GPIO.setup(GPIO_ECHO,GPIO.IN)       #Configuramos Echo como entrada
GPIO.output(GPIO_TRIGGER,False)     #Colocamos o pin 20 como LOW

 
GPIO.output(GPIO_TRIGGER,True)          #Enviamos uma pressao de ultrasonidos
time.sleep(0.00001)                     #Uma pequena pausa
GPIO.output(GPIO_TRIGGER,False)         #Apagamos a pressao
start = time.time()                     #Guarda o tempo atual mediante time.time()

while GPIO.input(GPIO_ECHO)==0:         #Enquanto o sensor nao receba sinal...
    start = time.time()                 #Mantemos o tempo actual mediante time.time()

while GPIO.input(GPIO_ECHO)==1:         #Se o sensor recebe sinal...
    stop = time.time()                  #Guarda o tempo actual mediante time.time() noutra variavel


elapsed = stop-start                    #Obtemos o tempo decorrido entre envio y rececao
distance = (elapsed * 34300)/2          #Distancia e igual ao tempo por velocidade partido por 2   D = (T x V)/2
distanceRound = round(distance,2)

bruto = (25 - round(distance,2))
if (bruto < 0):
    bruto = 0

perc = ((bruto * 100) / 18)
print round(perc,2)                     #Devolvemos a quantidade de agua no reservatorio (em porcentagem)

time.sleep(1)                           #Pequena pausa para nao saturar o procesador do Raspberry

GPIO.cleanup()
