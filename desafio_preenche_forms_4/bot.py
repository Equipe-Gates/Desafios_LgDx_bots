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
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

from webdriver_manager.chrome import ChromeDriverManager

import os

import pandas as pd

class Bot_teste(WebBot):

    @classmethod
    def diretorio_atual(cls):
        diretorio_atual = os.getcwd()
        return diretorio_atual

    def execution(self, execution=None):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

    def config_bot(self):
        # Configure whether or not to run on headless mode
        self.headless = False
        
        # Uncomment to change the default Browser to Firefox
        self.browser = Browser.CHROME

        # Uncomment to set the WebDriver path
        self.driver_path = ChromeDriverManager().install()

    def url_entra(self):
        # Opens the BotCity website.
        self.browse("https://docs.google.com/forms/d/e/1FAIpQLSeQ12ubChFxcM6xhOEhzRc_f0C01Oojqbs0ibjOslAL_UgLmw/viewform?usp=sf_link")
        self.maximize_window()

    def preenche_form(self, row):

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH, waiting_time=10000).click()
        self.paste(row['NOME'])

        if row['GÊNERO'] == 'Masculino':
            self.find_element('//*[@id="i11"]/div[3]/div', By.XPATH, waiting_time=10000).click()
        elif row['GÊNERO'] == 'Feminino':
            self.find_element('//*[@id="i14"]/div[3]/div', By.XPATH, waiting_time=10000).click()
        else:
            ...

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH, waiting_time=10000).click()
        self.paste(row['EMAIL'])

        self.wait(500)

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH, waiting_time=10000).click()
        self.paste(row['DEPARTAMENTO'])

        self.wait(500)

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', By.XPATH, waiting_time=10000).click()
        self.paste(row['ENDEREÇO'])

        self.wait(500)

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH, waiting_time=10000).click()
        self.paste(row['CPF'])

        self.wait(500)

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH, waiting_time=10000).click()
        self.paste(row['RG'])

        self.wait(500)

        if row['TURNO'] == 'Primeiro':
            self.find_element('//*[@id="i47"]/div[3]/div', By.XPATH, waiting_time=10000).click()
                    
        elif row['TURNO'] == 'Segundo':
            self.find_element('//*[@id="i50"]/div[3]/div', By.XPATH, waiting_time=10000).click()
                    
        elif row['TURNO'] == 'Comercial':
                    self.find_element('//*[@id="i53"]/div[3]/div', By.XPATH, waiting_time=10000).click()
                    
        else:
            ...

        self.wait(500)

        self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span', By.XPATH, waiting_time=10000).click()

    def lendo_excel(self):
        diretorio = Bot_teste.diretorio_atual()
        df = pd.read_excel(f'{diretorio}\\desafio_4\\resources\\DADOS_FUNCIONARIOS.xlsx', engine='openpyxl')
        
        for index, row in df.iterrows():
            
            self.url_entra()
                            
            if row['STATUS'] != 'Cadastrado':
                
                self.preenche_form(row)

                df.at[index, 'STATUS'] = 'Cadastrado'
                df.to_excel(f'{diretorio}\\desafio_4\\resources\\DADOS_FUNCIONARIOS.xlsx', index=False, engine='openpyxl')
                self.wait(2000)

    def action(self):
        
        # Implement here your logic...
        try:
            self.execution()
            self.config_bot()
            self.lendo_excel()
        except Exception as ex:
            print(f'Error na execução {ex}')
            self.save_screenshot('error.png')
        finally:
            # Wait 3 seconds before closing
            self.wait(10000)

            # Finish and clean up the Web Browser
            # You MUST invoke the stop_browser to avoid
            # leaving instances of the webdriver open
            self.stop_browser()

            # Uncomment to mark this task as finished on BotMaestro
            # maestro.finish_task(
            #     task_id=execution.task_id,
            #     status=AutomationTaskFinishStatus.SUCCESS,
            #     message="Task Finished OK."
            # )


    def not_found(self, label):
        print(f"Element not found: {label}")

bot = ... 
if __name__ == '__main__':
    Bot_teste().action()
