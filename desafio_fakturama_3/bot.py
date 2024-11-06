"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

import json

class Bot(DesktopBot):

    def config(self):
        # Configure whether or not to run on headless mode
        self.headless = False

    def carrega_json(self):

        caminho_arquivo = r"Desafios_LgDx_bots\\desafio_fakturama_3\\resources\\produtos.json"

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
        return dados

    def abre_fakturama(self):

        try:
            self.execute(r"C:\\Program Files\\Fakturama2\\Fakturama.exe")
            self.wait(5000)

            if not self.find("tela_cheia", matching=0.97, waiting_time=10000):
                self.not_found("tela_cheia")
            self.click()
            
        except Exception as ex:
            print('Erro ao abrir o aplicativo fakturama')
            self.save_screenshot('error.png')

    def adiciona_produto(self):
        load = self.carrega_json()
        produtos = load['load']['products']

        for produto in produtos:
            if not self.find_text("novo_produto", threshold=230, waiting_time=10000):
                self.not_found("novo_produto")
            self.click()
            
            if not self.find("item_number", matching=0.97, waiting_time=10000):
                    self.not_found("item_number")
            self.click_relative(134, 13)
            self.paste(produto["item_number"])

            if not self.find("Name", matching=0.97, waiting_time=10000):
                self.not_found("Name")
            self.click_relative(83, 14)
            self.paste(produto["name"])

            if not self.find("Category", matching=0.97, waiting_time=10000):
                self.not_found("Category")
            self.click_relative(95, 13)
            self.paste(produto["category"])

            if not self.find("GTIN", matching=0.97, waiting_time=10000):
                self.not_found("GTIN")
            self.click_relative(67, 14)
            self.paste(produto["gtin"])

            if not self.find("supplier code", matching=0.97, waiting_time=10000):
                self.not_found("supplier code")
            self.click_relative(137, 10)
            self.paste(produto["supplier_code"])

            if not self.find("Description", matching=0.97, waiting_time=10000):
                self.not_found("Description")
            self.click_relative(135, -1)
            self.paste(produto["description"])

            if not self.find("Price", matching=0.97, waiting_time=10000):
                self.not_found("Price")
            self.click_relative(253, 12)
            produto['price'] = produto['price'].replace('.', ',')
            self.paste(produto["price"])

            if not self.find("cost", matching=0.97, waiting_time=10000):
                self.not_found("cost")
            self.click_relative(198, 10)
            produto['cost'] = produto['cost'].replace('.', ',')
            self.paste(produto["cost"])

            if not self.find("allow", matching=0.97, waiting_time=10000):
                self.not_found("allow")
            self.click_relative(143, 17)
            produto['allowance'] = produto['allowance'].replace('.', ',')
            self.paste(produto['allowance'])

            if not self.find("vat", matching=0.97, waiting_time=10000):
                    self.not_found("vat")
            self.click_relative(115, 10)
            
            if not self.find("confirm_vat", matching=0.97, waiting_time=10000):
                self.not_found("confirm_vat")
            self.click()
              
            if not self.find("stock", matching=0.97, waiting_time=10000):
                self.not_found("stock")
            self.click_relative(102, 16)
            self.paste(produto['stock'])

            if not self.find("save", matching=0.97, waiting_time=10000):
                self.not_found("save")
            self.click()
            
            
    def action(self, execution = None):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        # Configure whether or not to run on headless mode
        self.headless = False

        # Implement here your logic...
        try:
            self.config()
            maestro.alert(
                task_id=execution.task_id,
                title="Inicializando",
                message="Alerta de inicialização",
                alert_type=AlertType.INFO
            )

            self.abre_fakturama()

            maestro.alert(
            task_id=execution.task_id,
            title="Inserindo produtos",
            message="Inserindo produtos no fakturama",
            alert_type=AlertType.INFO
            )

            self.adiciona_produto()

            self.wait(5000)
            maestro.alert(
            task_id=execution.task_id,
            title="Finalizado",
            message="Tarefa finalizada",
            alert_type=AlertType.INFO
            )

            maestro.finish_task(
                task_id=execution.task_id,
                status=AutomationTaskFinishStatus.SUCCESS,
                message="Task Finished OK."
            )
            if not self.find("fechar_janela", matching=0.97, waiting_time=10000):
                self.not_found("fechar_janela")
            self.click()
            
        except Exception as ex:
            print('Erro', ex)
            self.save_screenshot('erro.png')

            maestro.finish_task(
                task_id=execution.task_id,
                status=AutomationTaskFinishStatus.FAILED,
                message="Task Finished OK."
            )
        finally:
            # Wait 3 seconds before closing
            self.wait(3000)

            # Finish and clean up the Web Browser
            # You MUST invoke the stop_browser to avoid
            # leaving instances of the webdriver open


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

    
