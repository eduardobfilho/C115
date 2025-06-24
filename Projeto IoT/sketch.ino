#define BLYNK_PRINT Serial

// Dados do seu dispositivo no Blynk
#define BLYNK_TEMPLATE_ID "TMPL2Ui6y0t8b"
#define BLYNK_TEMPLATE_NAME "Smart Fridge"
#define BLYNK_AUTH_TOKEN "EgB9zj-2P1KBTlZGmeu5IN-uTnuzcBYq"

// Bibliotecas
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include "DHT.h"
#include "HX711.h"

// Credenciais WiFi
char ssid[] = "Wokwi-GUEST";
char pass[] = "";

// Configuração do DHT22
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// Configuração do HX711
#define DT 5
#define SCK 18
HX711 scale;

// Timer do Blynk
BlynkTimer timer;

// Função para enviar dados
void sendSensorData() {
  float temp = dht.readTemperature();
  float peso = scale.get_units();

  if (isnan(temp)) {
    Serial.println("Falha na leitura do DHT22!");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temp);
  Serial.println(" °C");

  Serial.print("Peso (g): ");
  Serial.println(peso);

  Blynk.virtualWrite(V0, temp); // Temperatura no app
  Blynk.virtualWrite(V1, peso); // Peso no app
}

void setup() {
  Serial.begin(9600);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
  dht.begin();

  scale.begin(DT, SCK);
  scale.set_scale();
  scale.tare();       // Zera a balança

  timer.setInterval(2000L, sendSensorData); // A cada 2 segundos
}

void loop() {
  Blynk.run();
  timer.run();
}
