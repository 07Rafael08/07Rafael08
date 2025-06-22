import datetime
from lxml import etree

def calcular_uptime(nascimento):
    hoje = datetime.date.today()
    diff = hoje - nascimento
    anos = diff.days // 365
    meses = (diff.days % 365) // 30
    dias = (diff.days % 365) % 30
    return f"{anos} anos, {meses} meses, {dias} dias"

def atualizar_svg(arquivo_svg, novo_texto):
    tree = etree.parse(arquivo_svg)
    root = tree.getroot()
    uptime = root.find(".//*[@id='uptime_value']")
    if uptime is not None:
        uptime.text = novo_texto
        tree.write(arquivo_svg, encoding='utf-8', xml_declaration=True)
        print("✅ SVG atualizado com:", novo_texto)
    else:
        print("❌ Elemento com ID 'uptime_value' não encontrado.")

if __name__ == "__main__":
    nascimento = datetime.date(2008, 2, 7)
    texto_uptime = calcular_uptime(nascimento)
    atualizar_svg("assets/profile.svg", texto_uptime)
