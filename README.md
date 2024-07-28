
# Monitoramento de Temperatura IoT com ESP32 e DS18B20

Este projeto é um sistema de monitoramento de temperatura utilizando um ESP32 e um sensor DS18B20, que se conecta a uma rede Wi-Fi e exibe a temperatura em um servidor web. O servidor web mostra a temperatura atual em uma interface simples.

## Sumário

- [Monitoramento de Temperatura IoT com ESP32 e DS18B20](#monitoramento-de-temperatura-iot-com-esp32-e-ds18b20)
  - [Sumário](#sumário)
  - [Visão Geral](#visão-geral)
  - [Requisitos](#requisitos)
  - [Instalação](#instalação)
  - [Configuração](#configuração)
  - [Uso](#uso)
  - [Contribuição](#contribuição)
  - [Licença](#licença)

## Visão Geral

O projeto foi desenvolvido para monitorar a temperatura de ambientes utilizando um microcontrolador ESP32 e um sensor de temperatura DS18B20. Os dados de temperatura são lidos periodicamente e exibidos em uma página web acessível via Wi-Fi.

## Requisitos

- [ESP32](https://www.espressif.com/en/products/socs/esp32)
- [Sensor DS18B20](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf)
- [MicroPython](https://micropython.org/)
- [Biblioteca MicroWebSrv](https://github.com/jczic/MicroWebSrv)

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
2. Faça o upload do código para o ESP32 usando uma ferramenta como o [Thonny](https://thonny.org/) ou [ampy](https://github.com/scientifichackers/ampy).

## Configuração

1. **Defina a rede Wi-Fi:**
   No código, configure o SSID e a senha da sua rede Wi-Fi:
   ```python
   ssid = "Wokwi-GUEST"
   password = ""
   ```

2. **Defina o pino de dados do sensor:**
   No código, configure o pino GPIO utilizado para conectar o sensor DS18B20:
   ```python
   data_pin = machine.Pin(5)
   ```

## Uso

1. Conecte o ESP32 à rede Wi-Fi configurada.
2. Acesse o servidor web do ESP32 pelo endereço IP fornecido na saída do console (geralmente `http://<endereço_ip_esp32>`).
3. A interface web exibirá a temperatura atual lida pelo sensor DS18B20.

## Contribuição

1. Faça um fork deste repositório.
2. Crie um branch com a sua feature: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona minha feature'`
4. Envie para o branch: `git push origin minha-feature`
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT
