import serial, time
import os


arduino = serial.Serial('COM3', 9600)

TIEMPO_EXPERIMENTO = 20
salida = '[{';

#'Valor":1,"Tiempo":2},{"Valor":4,"Tiempo":5}]";
i = 0

# LEER TEMPERATURA
while i < TIEMPO_EXPERIMENTO:
    line = arduino.readline()
    rawLine = line.decode('ASCII')
    salida = salida+'"Tiempo":'+str(rawLine)
    line = arduino.readline()
    rawLine = line.decode('ASCII')
    salida = salida+',"Temperatura":'+str(rawLine)
    i=i+1
    print(salida)
    if i<TIEMPO_EXPERIMENTO:
        salida = salida+'},{'
        
    if i==TIEMPO_EXPERIMENTO:
        salida = salida+'}'
    
salida = salida+']'
print(salida)
file = open("./input.json", "w")
file.write(salida)
file.close()
os.system("python codigo_python_receptor_generador.py")