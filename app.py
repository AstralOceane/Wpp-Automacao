#Automação de enchaminhamento de mensagens no wpp
#Usando a funcionalidade nativa do wpp para enchaminhar mensagnes
#enchaminhar de 5 em 5 mensagens


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")
sleep(120)

mensagem = """ Fala galera, 
testando minha automação de wpp"""

lista_contatos = ["Meu Numero","❍⃝🪷 Thaís 🍃🎋"]
#clica na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
#digita meu numero
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Meu Numero")
#da o enter
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
#escreve a mensagem
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)

input("Pressione Enter para fechar o navegador...")
nav.quit()

