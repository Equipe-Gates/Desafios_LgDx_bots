# Automação de Preenchimento de Formulário Google Forms com Atualização de Status no Excel

Este projeto tem como objetivo automatizar o preenchimento de um **formulário Google Forms** com dados extraídos de um arquivo  **Excel** . A cada preenchimento do formulário, o status do funcionário é atualizado para "Cadastrado" no Excel. Isso permite um monitoramento eficiente do progresso do cadastro dos funcionários.

### Funcionalidades:

1. Preenchimento automático de um **Google Forms** com dados de funcionários.
2. Atualização do status no arquivo Excel para indicar que o cadastro foi realizado.
3. Geração de um relatório simples, com o status atualizado dos funcionários.

### Requisitos:

* Python 3.x
* Bibliotecas:  **BotCity (webBot)** ,  **openpyxl** ,  **pandas, webdriver_manager (CHROME).**

### 1. Criação do Ambiente de Desenvolvimento

Para começar, crie um ambiente virtual para isolar as dependências do projeto. No terminal, execute:

```
# Criação do ambiente virtual
python -m venv venv

# Ativando o ambiente virtual (Windows)
venv\Scripts\activate

# Ativando o ambiente virtual (Linux/macOS)
source venv/bin/activate

```

Depois de ativar o ambiente virtual, instale as bibliotecas necessárias:

# Instalando as dependências

```
pip install -r requirements.txt
```

### 2. Automação do Preenchimento do Formulário

Usamos a **BotCity** para automatizar o preenchimento do formulário Google Forms. O script acessa o formulário, preenche os campos com os dados dos funcionários extraídos do arquivo Excel e submete o formulário.

#### Passos:

1. O script abre o navegador e acessa o link do  **Google Forms** .
2. Para cada linha de dados do arquivo Excel, preenche os campos do formulário com as informações.
3. Após preencher, o formulário é enviado e o script passa para o próximo funcionário.

### 3. Atualização do Status no Excel

Após cada envio de formulário, o status do funcionário é atualizado para "Cadastrado" no arquivo Excel.

### 4. Relatório Final

Ao final do processo, o arquivo Excel estará atualizado com o status de cada funcionário, permitindo a geração de um relatório simples, que pode ser exportado ou visualizado diretamente no arquivo.

### Considerações Finais

Esse script automatiza o preenchimento de um formulário Google Forms com os dados dos funcionários extraídos de um arquivo Excel. A cada envio, o status de cada funcionário é atualizado para "Cadastrado". Esse processo permite que você faça um cadastro em massa de funcionários, além de gerar um relatório simples com o status de cada um.

**Note:** Antes de rodar o script, teste-o em um ambiente de desenvolvimento para garantir que os campos do Google Forms estão sendo preenchidos corretamente.

### Contribuições

Se você deseja contribuir para este projeto, por favor, abra uma *issue* ou envie um *pull request* com suas sugestões e melhorias.
