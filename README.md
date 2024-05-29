# Conversor Monetário 🪙

## Descrição do Projeto:

Este projeto é um conversor monetário simples construído com Flask. 
Ele permite converter valores entre várias moedas, utilizando dados de câmbio reais e atualizados da API CoinGecko.
A aplicação suporta conversões entre as seguintes moedas: Dólar Americano (USD), Real Brasileiro (BRL), Euro (EUR), Bitcoin (BTC) e Ethereum (ETH).

## Organização do Código

A organização do código segue a estrutura padrão de um projeto Flask, com separação clara entre módulos, views e models, e distinção entre o back-end e o front-end. Os arquivos principais incluem:

- `app.py`: Ponto de entrada da aplicação Flask.
- `views/`: Contém as views da aplicação, incluindo a lógica de conversão monetária.
- `models/`: Contém a lógica de negócio, incluindo as funções para obter taxas de conversão.
- `static/`: Contém arquivos estáticos como CSS e imagens.
- `templates/`: Contém templates HTML para a renderização das páginas.

## Como Rodar a Aplicação

### Pré-requisitos

- Python 3.12.2
- Flask
- Requests
- Dotenv

### Passos para Rodar

1. Clone este repositório:  
    ```bash
    git clone git@github.com:Laura2606/conversor-monetario.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual e ative-o:  
    ```bash
    python3 -m venv .venv && source .venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:  
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:  
    ```bash
    python -m src.app
    ```

5. Acesse a aplicação em seu navegador no endereço:  
    ```
    http://127.0.0.1:5000
    ```

## Funcionalidades

- Conversão entre USD, BRL, EUR, BTC e ETH.
- Interface web simples para inserir valores e escolher moedas de conversão.
- Resultado exibido com duas casas decimais.

## Problemas Conhecidos


## Segurança

- Utilize HTTPS para comunicação segura com a API CoinGecko.

## Escolhas Técnicas

- Flask foi escolhido pela sua simplicidade e facilidade de uso para pequenos projetos.
- A API CoinGecko foi selecionada por fornecer dados de câmbio atualizados de forma gratuita.
