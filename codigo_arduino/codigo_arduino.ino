#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

//Variable donde almacenaremos el numero aleatorio
long randomNumber;
int SENSOR = 2;
int i=0;
int nro_temp;
int nro_hum;
DHT dht (SENSOR, DHT11);

//Función de inicialización
void setup() {
  
  //Inicializamos la comunicación serial
  Serial.begin(9600);

}
 
//Bucle principal
void loop() {
  dht.begin();
  //Genera un numero aleatorio entre 1 y 100
  randomNumber = random(1,100);
  nro_temp = dht.readTemperature(); /* Grados celcius */
  nro_hum = dht.readHumidity();

  
  //Escribimos el numero aleatorio por el puerto serie
  Serial.println(i);
  Serial.println(nro_temp);
  i=i+1;
  delay(1000);
}
