import machine  # Importa biblioteca para micropython
import onewire  # Importa biblioteca para comunicação OneWire
import ds18x20  # Importa biblioteca para sensor DS18B20
import time  # Importa biblioteca para funções de tempo

# Define o pino de dados conectado ao sensor DS18B20
pino_dado = machine.Pin(5)

# Cria um objeto OneWire no pino de dados
sensor = ds18x20.DS18X20(onewire.OneWire(pino_dado))  # Faixa de -55ºC a 125ºC, variação +- 0,5ºC

def ler_temperatura():
  """
   Lê a temperatura do sensor DS18B20 e retorna o valor em Celsius.
  """
  # Busca sensores na rede
  enderecos = sensor.scan()

  # Verifica se algum sensor foi encontrado
  if not enderecos:
    print("Nenhum sensor DS18B20 encontrado!")
    return None

  # Inicia conversão de temperatura para todos os sensores
  sensor.convert_temp()

  # Loop por cada endereço ROM do sensor
  for endereco in enderecos:
    # Lê a temperatura do sensor
    temperatura = sensor.read_temp(endereco)
    # Imprime a temperatura em Celsius
    print("Temperatura: {:.2f} °C".format(temperatura))
    return temperatura  # Retorna a temperatura para uso posterior (opcional)

while True:
  # Lê a temperatura a cada 2 segundos
  temperatura = ler_temperatura()
  # Você pode usar o valor da temperatura aqui (e.g., imprimir na serial, enviar para servidor)
  time.sleep(2)
