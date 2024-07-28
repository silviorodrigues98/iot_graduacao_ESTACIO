import machine
import onewire
import ds18x20
import time
import network
from microWebSrv import MicroWebSrv

# Define a rede Wi-Fi
ssid = "Wokwi-GUEST"
password = ""

# Define o pino de dados conectado ao sensor DS18B20
data_pin = machine.Pin(5)

# Cria um objeto OneWire no pino de dados
sensor = ds18x20.DS18X20(onewire.OneWire(data_pin))

# Cria uma variável global para armazenar a temperatura
temperature = None

def connect_wifi(ssid, password):
  """
  Conecta o ESP32 a uma rede Wi-Fi.
  """
  print("Conectando ao Wi-Fi", end=" ")
  wifi = network.WLAN(network.STA_IF)
  wifi.active(True)
  wifi.connect(ssid, password)
  while not wifi.isconnected():
    print(".", end="")
    time.sleep(0.1)
  print("Conectado ao Wi-Fi!")
  print("SSID:", ssid)
  print("Endereço IP:", wifi.ifconfig()[0])

def check_connection():
  """
  Verifica se o ESP32 está conectado à rede Wi-Fi.
  """
  wifi = network.WLAN(network.STA_IF)
  return wifi.isconnected()

def read_temperature():
  """
  Lê a temperatura do sensor DS18B20 e retorna o valor em Celsius.
  """
  # Procura por sensores na rede
  addresses = sensor.scan()

  # Verifica se algum sensor foi encontrado
  if not addresses:
    print("Nenhum sensor DS18B20 encontrado!")
    return None

  # Inicia a conversão de temperatura para todos os sensores
  sensor.convert_temp()

  # Percorre o endereço ROM de cada sensor
  for address in addresses:
    # Lê a temperatura do sensor
    temp = sensor.read_temp(address)
    # Imprime a temperatura em Celsius
    print("Temperatura: {:.2f} °C".format(temp))
    return temp  # Retorna a temperatura para uso posterior (opcional)

def update_temperature():
  """
  Atualiza a variável global de temperatura com a leitura mais recente.
  """
  global temperature
  temperature = read_temperature()

def handle_request(httpClient, httpResponse):
  """
  Manipula a solicitação HTTP e envia a temperatura como resposta.
  """
  httpResponse.WriteResponseOk(
    headers={
      "Content-Type": "text/html",
    },
    content="""<!DOCTYPE html>
    <!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MONITORAMENTO DE TEMPERATURA IOT</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background: linear-gradient(to right, #b3e5fc, #c8e6c9);
            overflow: hidden;
            user-select: none;
            -moz-user-select: none;
            -webkit-user-select: none;
            -ms-user-select: none;
        }

        #container {
            margin-top: 10%;
        }

        h1 {
            color: #333;
            margin-top: 50px;
            font-size: 4em;
        }

        h2 {
            color: #666;
            margin-top: 20px;
            font-size: 5em;
        }

        span {
            color: #333;
            font-size: 6em;
        }

        label {
            font-size: 6em;
        }
    </style>
</head>

<body>
    <div id="container">
        <h1>MONITORAMENTO DE TEMPERATURA IOT</h1>
        <h2>Temperatura Atual</h2>
        <label for="temperatura">🌡</label>
        <span id="temperatura">{}</span>
    </div>
</body>
</html>""".format(temperature)
  )

# Conecta-se ao Wi-Fi
connect_wifi(ssid, password)

# Inicia o servidor web
srv = MicroWebSrv(webPath="/")
srv.MaxWebSocketRecvLen = 256
srv.WebSocketThreaded = False
srv.BindAddress = ("0.0.0.0", 80)
srv.AddRoute("/", "GET", handle_request)
srv.Start()

while True:
  if not check_connection():
    connect_wifi(ssid, password)
  # Atualiza a temperatura
  update_temperature()
  time.sleep(2)
