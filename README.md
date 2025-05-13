#  Anlise de Dados Forenses em Python no Ubuntu

# 🔍 Laboratório de Análise Forense com Python no Ubuntu

Este projeto é um laboratório prático de análise de dados forenses utilizando Python no sistema operacional Ubuntu.

## 🎯 Objetivo

Investigar atividades suspeitas em um sistema Linux por meio de:

- Análise de **tentativas de login falhas** usando arquivos de log do sistema (`auth.log`);
- Análise de **tráfego de rede** capturado via `tcpdump`, usando a biblioteca `Scapy`.

---

## 📁 Estrutura do Projeto

```
lab-forense/
├── system_logs.txt              # Logs de autenticação exportados
├── network_traffic.pcap         # Pacotes de rede capturados (opcional)
├── analisa_logs.py              # Script de análise de tentativas de login
├── analisa_pacotes.py           # Script de análise de pacotes de rede
└── laboratorio_analise_forense_ubuntu.md  # Documentação do laboratório
```

---

## 📦 Dependências

Instale os pacotes com pip:

```bash
pip install pandas matplotlib scapy
```

---

## ⚙️ Como usar

### 1. Exportar os logs do sistema:

```bash
sudo cat /var/log/auth.log > system_logs.txt
```

### 2. Rodar o script de análise de login:

```bash
python3 analisa_logs.py
```

### 3. (Opcional) Capturar pacotes de rede:

```bash
sudo tcpdump -i eth0 -w network_traffic.pcap
```

### 4. Rodar o script de análise de pacotes:

```bash
python3 analisa_pacotes.py
```

---

## 📊 Resultado

O script gera um gráfico mostrando **em quais horários do dia** ocorreram mais tentativas de login falhas.

O script de rede exibe os **10 IPs de origem** que mais enviaram pacotes TCP no período capturado.

---

## 👩‍💻 Autor(a)

Este projeto foi desenvolvido como parte de estudos forenses utilizando Python.

---
