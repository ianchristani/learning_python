
#abrindo o prompt de comando
import os
os.system()

#lendo arquivos CSV
import pandas as pd
variavel=pd.read_csv('caminho_do_arquivo')

#lendo arquivos XLS
import openpyxl
variavel=openpyxl.load_workbook('caminho_do_arquivo')

#sai do programa
import sys
sys.exit()

#criando pastas, td o que nao existir, passara a existir
import os
os.makedirs('caminho com a(s) nova(s) pasta(s)')

#abrindo arquivos de txt
variavel=open('caminho','modo')
'''
o modo pode ser:
    w = write (vai apagar o que tinha anteriormente sefor o caso)
    a = add (vai add no fim do texto)
    r = read
'''    
#lendo o arquivo txt
variavel2=variavel.read()

#copiando arquivos e pastas
import shutil, os
os.chdir('C:\\')
#note que nesse modulo usa-se sempre 2 barras ao inves de uma
shutil.copy('end_origem','end_destino')
#se no end_destino vc colocar um nome diferente, o conteudo de origem vai para
#o arquivo de nome diferente, agora se nao especificar nome, ele copia com o nome
#original

#esse copia TDS os arquivos de dentro da pasta de origem para a destino
os.chdir('C:\\')
shutil.copytree('end_origem','end_destino')
#move o arquivo de origem para o destino
shutil.move('end_origem','end_destino')

#apaga o arquivo permanentemente
os.unlink('caminho')
#apaga a pasta permanentemente
os.rmdir('caminho')

'''
webbrowser: Vem junto com o Python e abre um navegador em uma página específica.

Requests: Faz downloads de arquivos e de páginas web da Internet.

Beautiful Soup: Faz parse de HTML, que é o formato em que as páginas web são escritas.

Selenium: Inicia e controla um navegador web. O Selenium é capaz de preencher
formulários e simular cliques de mouse nesse navegador.
'''
#abrindo whatsapp no navegador CHROME e interagindo com o programa
from selenium import webdriver
driver = webdriver.Chrome(executable_path="/home/ian/Documentos/PYTHON/chromedriver")
driver.get("http://web.whatsapp.com")

#abrindo o navegadorem umapag especifica
import webbrowser
webbrowser.open('http://web.whatsapp.com')

#fazendo download de arquivos na internet
import requests
variavel=requests.get('endereco_do_arquivo')
#verificando se houve erros
variavel.raise_for_status()




