import os
import re
from time import sleep
import requests
import csv
from bs4 import BeautifulSoup as soup
# re: ponto é qualquer caracter ad....s poderia ser adultos, por exemplo

class MeuTexto:
    def __init__(self, url=None):
        self.texto = soup
        self.url = url
        if self.url != None:
            self.response = requests.get(self.url)
            self.raw_html = self.response.text
            # Pesquisar com expressões regulares
            self.parsed_html = soup(self.raw_html, "html.parser")


    def retorna_texto(self):
        for tag in self.parsed_html.find_all(re.findall(r"p")):
            print(tag)
            sleep(10)
        #print(self.parsed_html.find_all(string=re.compile("Errar")))

    def digito_arquivo(self):
        if not os.path.isdir("textos"):
            os.mkdir('textos')
        else:
            nomes_arquivos = [x for x in os.listdir("textos/") if 'texto_intercept' in x]
            quant_arquivos = len(nomes_arquivos)
            for nome_arquivo in nomes_arquivos:
                if nome_arquivo[-4:] == ".txt":
                    digito = int(nome_arquivo[0])
                    if digito > 1:
                        digito += 1
                    else:
                        pass
                    novo_nome_arquivo = str(digito) + nome_arquivo[1:]
                    return novo_nome_arquivo

    def cria_txt(self, text, novo_arquivo):
        with open(novo_arquivo, "w+", encoding="utf8", newline="") as file:
            file.write(text)

url = "https://www.intercept.com.br/2023/10/12/errar-e-humano-exceto-para-pessoas-negras/"
texto_intercept = MeuTexto(url)
texto_intercept.retorna_texto()
