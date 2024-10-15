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
            self.parsed_html = self.texto(self.raw_html, "html.parser")

    def retorna_texto(self):
        """
        Retorna o texto formatado da página web.
        Referencia: div>single-content
        """
        search_index = self.parsed_html.find_all("div")[6]
        search_class_formated_text = self.parsed_html.find("div", class_='single-content').text
        # for tag in self.parsed_html.find_all(re.findall(r"<p>", "Marcelle")):
        #     print(tag)
        #     sleep(1)
        #print(self.parsed_html.find(string=re.compile("p")).text)
        # print(self.parsed_html.find("p").text.strip())
        # print(self.parsed_html.find(re.findall(r"Alexandre")).text.strip())
    
        return self.parsed_html.find("div", class_='single-content').text

    def digito_arquivo(self):
        """
        """
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
        """
        Cria um novo arquivo com o texto extraído
        """
        with open(novo_arquivo, "w+", encoding="utf8", newline="") as file:
            file.write(text)

if __name__ == "__main__":
    url = "https://www.intercept.com.br/2024/10/12/twitter-voltou/"
    texto_intercept = MeuTexto(url)
    print(texto_intercept.retorna_texto())
