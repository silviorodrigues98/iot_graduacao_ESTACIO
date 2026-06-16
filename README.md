<!--

<!--
  📌 Projeto acadêmico — mantido como registro de formação
  Não recebe manutenção ativa.
-->

> **📚 Projeto acadêmico** — Desenvolvido durante o curso de **Análise e Desenvolvimento de Sistemas** (Estácio).  
> Este repositório é mantido como **registro de formação**. Não recebe manutenção ativa.  
> Para projetos atuais, veja meus repositórios em destaque no [perfil](https://github.com/silviorodrigues98).

  TEMPLATE: Academic Work
  Use para: trabalhos de graduação (ESTACIO), atividades extensionistas
-->

# Monitoramento de Temperatura IoT com ESP32 e DS18B20

![Estácio](https://img.shields.io/badge/Instituição-Estácio-0a6e1e)
![4º Semestre](https://img.shields.io/badge/Semestre-4º-blue)
![ESP32](https://img.shields.io/badge/Hardware-ESP32-red)
![MicroPython](https://img.shields.io/badge/Linguagem-MicroPython-green)
![DS18B20](https://img.shields.io/badge/Sensor-DS18B20-yellow)

> Sistema de monitoramento de temperatura utilizando um microcontrolador ESP32 e sensor DS18B20, com exibição dos dados em tempo real via servidor web embarcado. Projeto desenvolvido para a disciplina de **Cloud, IoT e Indústria 4.0** do curso de Análise e Desenvolvimento de Sistemas.

---

## 🎯 Contexto Acadêmico

| Item | Detalhe |
|------|---------|
| **Instituição** | Universidade Estácio de Sá |
| **Curso** | Análise e Desenvolvimento de Sistemas |
| **Disciplina** | Cloud, IoT e Indústria 4.0 |
| **Semestre** | 4º semestre |
| **Ano** | 2024 |

---

## 📋 Objetivo

Desenvolver um sistema de monitoramento de temperatura baseado em Internet das Coisas (IoT) utilizando um ESP32 e um sensor DS18B20. O sistema conecta-se a uma rede Wi-Fi, lê a temperatura ambiente periodicamente e disponibiliza os dados em uma interface web acessível de qualquer dispositivo conectado à mesma rede — aplicando na prática os conceitos de Cloud, IoT e Indústria 4.0.

---

## 🛠️ Tecnologias Utilizadas

- **ESP32** — microcontrolador com Wi-Fi integrado
- **MicroPython** — firmware e linguagem de programação embarcada
- **Sensor DS18B20** — sensor digital de temperatura (OneWire)
- **MicroWebSrv** — servidor web embarcado para MicroPython
- **Wi-Fi (Wokwi-GUEST)** — conectividade de rede
- **Wokwi** — simulador online de circuitos IoT

---

## ⚙️ Como Executar

```bash
# Clone
git clone https://github.com/silviorodrigues98/iot_graduacao_ESTACIO.git
cd iot_graduacao_ESTACIO

# Simulação online (recomendado)
# Acesse: https://wokwi.com/projects/403225545754858497
```

### Configuração física (opcional)

1. Faça o upload dos arquivos (`sensor_temperatura.py` e `page.html`) para o ESP32 usando [Thonny](https://thonny.org/) ou [ampy](https://github.com/scientifichackers/ampy).
2. Edite as credenciais de rede no código:
   ```python
   ssid = "sua_rede_wifi"
   password = "sua_senha"
   ```
3. Conecte o sensor DS18B20 ao pino GPIO 5 do ESP32.
4. Acesse o servidor web pelo endereço IP exibido no console.

---

## 📚 Conceitos Aplicados

- **Internet das Coisas (IoT)** — comunicação entre dispositivos físicos e a rede
- **Sensoriamento digital** — leitura de temperatura via protocolo OneWire (DS18B20)
- **Servidor web embarcado** — interface HTTP diretamente no microcontrolador
- **Conectividade Wi-Fi** — integração do ESP32 a redes sem fio
- **MicroPython** — implementação de lógica embarcada com Python
- **Simulação de hardware** — prototipagem virtual com Wokwi

---

## 🔗 Simulação

Experimente o projeto online sem necessidade de hardware físico:

<p align="center">
  <a href="https://wokwi.com/projects/403225545754858497">
    <img src="https://img.shields.io/badge/Simulação-Wokwi-1f7a1f?style=for-the-badge" alt="Simulação Wokwi">
  </a>
</p>

---

<p align="center">
  Projeto acadêmico desenvolvido para a disciplina de Cloud, IoT e Indústria 4.0 — 4º semestre de Análise e Desenvolvimento de Sistemas
</p>

<p align="center">
  <a href="https://github.com/silviorodrigues98">@silviorodrigues98</a>
</p>
