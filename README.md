# 🌤️ Consultor de Clima em Tempo Real

Meu primeiro projeto que consome dados reais da internet através de uma **API REST**.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JSON](https://img.shields.io/badge/json-5E5E5E?style=for-the-badge&logo=json&logoColor=white)

## 📋 Sobre o Projeto
O objetivo deste programa é conectar-se aos servidores da API **HG Brasil Weather** para buscar informações climáticas atualizadas. O projeto exercita o uso de requisições **HTTP**, manipulação de arquivos **JSON** e integração com serviços externos.

## 🚀 Funcionalidades
* **Requisições HTTP:** Uso da biblioteca `requests` para buscar dados na web.
* **Consumo de API:** Integração com o serviço HG Brasil Weather.
* **Processamento de JSON:** Extração de dados específicos (temperatura, cidade, umidade e descrição) de um dicionário complexo retornado pela API.
* **Tratamento de Exceções:** Gerenciamento de erros de conexão e falhas na busca de dados.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Biblioteca `requests`** (Instalável via pip)
* **API HG Brasil Weather**

## 🔧 Como Executar
1. Instale a dependência necessária e execute o arquivo.py:
   ```bash
   pip install requests

