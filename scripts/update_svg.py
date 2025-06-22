#!/usr/bin/env python3
import datetime
from lxml import etree

SVG_PATH = "assets/profile.svg"
BIRTH = datetime.date(2008, 2, 7)

def calcula_idade(born: datetime.date, hoje: datetime.date):
    anos = hoje.year - born.year - ((hoje.month, hoje.day) < (born.month, born.day))
    meses = hoje.month - born.month - (1 if hoje.day < born.day else 0)
    if meses < 0:
        meses += 12
    
    # Calcular dias considerando o mês anterior ao atual
    ultimo_aniversario_mes = (hoje.month - 1) if hoje.month > 1 else 12
    ultimo_aniversario_ano = hoje.year if hoje.month > 1 else hoje.year - 1
    
    try:
        data_referencia = datetime.date(ultimo_aniversario_ano, ultimo_aniversario_mes, born.day)
    except ValueError:
        # se o dia não existir no mês (ex: 30 em fevereiro), pega o último dia do mês
        data_referencia = datetime.date(ultimo_aniversario_ano, ultimo_aniversario_mes + 1, 1) - datetime.timedelta(days=1)
    
    dias = (hoje - data_referencia).days
    if dias < 0:
        dias = 0

    return anos, meses, dias

def atualiza_svg():
    hoje = datetime.date.today()
    anos, meses, dias = calcula_idade(BIRTH, hoje)
    texto = f"{anos} anos, {meses} meses, {dias} dias"

    tree = etree.parse(SVG_PATH)
    root = tree.getroot()
    age = root.find(".//*[@id='age_data']")
    age_dots = root.find(".//*[@id='age_data_dots']")
    if age is not None and age_dots is not None:
        age.text = texto
        comprimento = 22
        dots = comprimento - len(texto)
        age_dots.text = " " + "."*dots + " " if dots > 0 else " "

    tree.write(SVG_PATH, xml_declaration=True, encoding="UTF-8")

if __name__ == "__main__":
    atualiza_svg()
