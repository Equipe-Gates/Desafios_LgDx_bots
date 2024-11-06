# Automação de Cadastro de Novos Produtos no ERP Fakturama com BotCity

Este projeto utiliza o **BotCity Desktop Bot** e técnicas de visão computacional para automatizar o processo de cadastro de novos produtos no ERP  **Fakturama** . O script em Python lê dados de um arquivo **JSON** e os utiliza para preencher automaticamente os campos das telas de cadastro do Fakturama, facilitando a entrada de dados e reduzindo o tempo e erros no processo de inserção de produtos.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Arquitetura](#arquitetura)
- [Requisitos](#requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Utilizar](#como-utilizar)
- [Personalização](#personalização)

## Descrição do Projeto

A automação tem como objetivo ler um arquivo JSON contendo dados de novos produtos e realizar automaticamente o cadastro destes no ERP Fakturama. Com o uso do BotCity Desktop Bot e a visão computacional, o bot identifica os campos necessários e realiza as ações de preenchimento e confirmação em tempo real, proporcionando uma automação robusta para operações que envolvem grande volume de dados.

### Exemplo de Estrutura do JSON de Entrada

O arquivo JSON contém uma lista de produtos com as seguintes chaves (personalizável conforme a necessidade do cadastro no ERP):

```
json
{
    "load": {
        "customer": "BOTTEST",
        "products": [
            {
                "item_number": "0000000000001",
                "name": "PRODUCT DEMO 1",
                "category": "ELECTRONICS",
                "gtin": "0000000000123",
                "supplier_code": "SUPPLIER1",
                "description": "PRODUCT DEMO 1",
                "price": "100.00",
                "cost": "50.00",
                "allowance": "0.00",
                "vat": "Free of Tax",
                "stock": "100"
            },
            {
                "item_number": "0000000000002",
                "name": "PRODUCT DEMO 2",
                "category": "ELECTRONICS",
                "gtin": "0000000000124",
                "supplier_code": "SUPPLIER1",
                "description": "PRODUCT DEMO 2",
                "price": "94.90",
                "cost": "47.50",
                "allowance": "1.90",
                "vat": "Free of Tax",
                "stock": "143"
            }
        ]
    }
}

```


## Arquitetura

A aplicação é composta por:

* **Script Principal:** Script em Python que controla o fluxo de execução e a leitura dos dados do JSON.
* **Bot de Automação:** Utilizando o BotCity Desktop, o bot simula a interação humana com a interface do Fakturama, preenchendo os campos com os dados extraídos.
* **Visão Computacional:** Utilizada para localizar os campos e botões específicos na tela do Fakturama.

## Requisitos

1. **Python 3.8+**
2. **BotCity Desktop Bot**
3. **Bibliotecas Python Necessárias** :

* `botcity-framework-core`
* `json`

1. **ERP Fakturama** instalado e configurado.
2. JSON com os dados dos produtos a serem cadastrados.

## Instalação e Configuração

1. **Clone o Repositório.**
2. **Instale as Dependências** :
   Execute o seguinte comando para instalar as dependências:

   `pip install -r requirements.txt`
3. **Configuração do BotCity** :

* Instale o BotCity Studio e configure o ambiente de acordo com a documentação da [BotCity](https://botcity.dev/).
* Realize a configuração inicial para detectar os campos no Fakturama e definir as ações.

## Como Utilizar

1. **Execute o Script** :
   Inicie a automação executando o script Python com o comando:

    `python bot.py`

2.  **Monitoramento** :
   Durante a execução, o bot abrirá o Fakturama e preencherá automaticamente os dados de cada produto.

## Personalização

* **Campos Personalizáveis** :
  Caso o formato do JSON ou os campos do Fakturama sejam diferentes, ajuste o código para corresponder aos novos campos.
* **Configurações do BotCity** :
  Ajuste os pontos de interação do bot com a interface do Fakturama no BotCity Studio caso existam diferenças visuais na interface.
