
# 🧊 Smart Fridge - Geladeira Inteligente com IoT

Este projeto é uma simulação de uma geladeira inteligente utilizando IoT, sensores e um microcontrolador ESP32. A geladeira é capaz de monitorar a temperatura interna e o peso de um produto (como suco, leite etc.), e enviar essas informações para um aplicativo móvel via Blynk.

---

## 🚀 Tecnologias Utilizadas

- ESP32 (microcontrolador)
- Sensor de temperatura e umidade **DHT22**
- Módulo de célula de carga com amplificador **HX711**
- Blynk IoT
- Simulação com **Wokwi**
- Arduino IDE

---

## 📁 Estrutura do Projeto

- `sketch.ino` → Código principal para o ESP32
- `project.png` → Diagrama das conexões
- `Smart Fridge.pptx` → Slides utilizados na apresentação
- `logo_smartfridge.png` → Logotipo do projeto
- `libraries.txt` → Bibliotecas utilizadas
- `https://wokwi.com/projects/434612547347469313` → Link da simulação online

---

## 📡 Funcionalidades

- Monitoramento em tempo real da temperatura da geladeira
- Leitura do peso de um item com célula de carga
- Envio dos dados via Wi-Fi para o Blynk App
- Interface no app com indicadores de temperatura e peso

---

## 🧪 Simulação no Wokwi

Você pode testar este projeto no simulador online Wokwi:

👉 [Clique aqui para abrir a simulação (Wokwi)](https://wokwi.com/projects/434612547347469313)

---

## 📱 Visual do App (Blynk)

No app do Blynk:
- `V0`: Temperatura (em °C)
- `V1`: Peso do produto (em gramas)

Widgets recomendados:
- **Gauge** ou **Display** para cada leitura
- **Notificações** (se desejar alertar sobre níveis baixos)

---

## 🧠 Considerações Finais

Esse projeto demonstra a aplicação prática de IoT no dia a dia, com foco em automação doméstica, economia de energia e controle inteligente de recursos.

---

## 📎 Referências

- [Blynk IoT Docs](https://docs.blynk.io)
- [Wokwi Simulator](https://wokwi.com)
- [DHT Sensor Library (Adafruit)](https://github.com/adafruit/DHT-sensor-library)
- [HX711 Arduino Library](https://github.com/bogde/HX711)