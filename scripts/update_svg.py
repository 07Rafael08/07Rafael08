#!/usr/bin/env python3
import datetime
from lxml import etree

SVG_PATH = "assets/profile.svg"
BIRTH = datetime.date(2008, 2, 7)

def calcula_idade(born: datetime.date, hoje: datetime.date):
    anos = hoje.year - born.year - ((hoje.month, hoje.day) < (born.month, born.day))
    md = (hoje.month - born.month - (1 if hoje.day < born.day else 0)) % 12
    # cálculo aproximado de dias do mês
    dias = (hoje - born.replace(year=hoje.year, month=hoje.month)).days
    if dias < 0:
        ultimo = born.replace(year=hoje.year, month=hoje.month) - datetime.timedelta(days=hoje.day)
        dias = (hoje - ultimo).days
    return anos, md, dias

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
        # justifica pontos
        comprimento = 22
        dots = comprimento - len(texto)
        age_dots.text = " " + "."*dots + " " if dots > 0 else " "
    tree.write(SVG_PATH, xml_declaration=True, encoding="UTF-8")

if __name__ == "__main__":
    atualiza_svg()
