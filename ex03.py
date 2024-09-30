import json
import xml.etree.ElementTree as ET

def ler_dados_json(caminho):
    with open(caminho, 'r') as file:
        dados = json.load(file)
    return [item['valor'] for item in dados]

def ler_dados_xml(caminho):
    tree = ET.parse(caminho)
    root = tree.getroot()
    return [float(row.find('valor').text) for row in root.findall('row')]

def calcular_faturamento(faturamento):
    faturamento_validos = [dia for dia in faturamento if dia > 0]

    menor = min(faturamento_validos)
    maior = max(faturamento_validos)
    media = sum(faturamento_validos) / len(faturamento_validos)
    dias_acima_media = sum(1 for dia in faturamento_validos if dia > media)

    return menor, maior, media, dias_acima_media

# Caminhos dos arquivos
caminho_json = r'H:\PROJETOS GIT\estagiotarget\dados.json'
caminho_xml = r'H:\PROJETOS GIT\estagiotarget\dados (2).xml'

# Ler dados de ambos os arquivos
faturamento_json = ler_dados_json(caminho_json)
faturamento_xml = ler_dados_xml(caminho_xml)

# Unir dados de ambos os formatos
faturamento_total = faturamento_json + faturamento_xml

# Calcular os resultados
menor, maior, media, dias_acima_media = calcular_faturamento(faturamento_total)

# Exibir resultados
print(f'Menor faturamento: R$ {menor:.2f}')
print(f'Maior faturamento: R$ {maior:.2f}')
print(f'Média mensal: R$ {media:.2f}')
print(f'Números de dias com faturamento acima da média: {dias_acima_media}')
