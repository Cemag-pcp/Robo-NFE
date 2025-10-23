from funcoes_selenium_innovaro import *
import pandas as pd
import gspread  # pip install gspread
import numpy as np
import psycopg2.extras
import psycopg2  # pip install psycopg2
import datetime
from datetime import datetime, timedelta
import logging
import time
import os
import glob

#logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

DB_HOST = "database-2.cdcogkfzajf0.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "15512332"

print("começando...")

def listar(nav, classe):
    
    lista_menu = nav.find_elements(By.CLASS_NAME, classe)
    
    elementos_menu = []

    for x in range (len(lista_menu)):
        a = lista_menu[x].text
        elementos_menu.append(a)

    test_lista = pd.DataFrame(elementos_menu)
    test_lista = test_lista.loc[test_lista[0] != ""].reset_index()

    return(lista_menu, test_lista)


def get_latest_download_path():
    download_folder = os.path.expanduser("~") + "\\Downloads"
    
    # Lista todos os arquivos da pasta de downloads
    files = glob.glob(os.path.join(download_folder, "*"))

    # Filtra os arquivos que NÃO terminam com '.pdf' (ignorando maiúsculas/minúsculas)
    non_pdf_files = [f for f in files if not f.lower().endswith('.pdf')]

    if non_pdf_files:
        # Retorna o arquivo mais recente entre os que não são PDF
        latest_file = max(non_pdf_files, key=os.path.getctime)
        return latest_file
    else:
        return None
    
# data_fim = (datetime.now().date()).strftime("%d/%m/%Y")
data_inicio = (datetime.now().date()).strftime("%d/%m/%Y")

nav = navegador()

logging.info("Iniciando selenium")

#Logando assistente almoxarifado Cem#@157158922618942
login(nav, "assistente almoxarifado", "Cem#@157158922618942")
print("logando...")

#Abrindo menu
menu_innovaro(nav)
print("abrindo menu...")

#Clicando em Estoque
lista_menu, test_list = listar(nav, 'webguiTreeNodeLabel')
time.sleep(1.5)
click_producao = test_list.loc[test_list[0] == 'Compra'].reset_index(drop=True)['index'][0]
print("clicando em estoque...")

lista_menu[click_producao].click() ##clicando em producao

logging.info("Navegando para o Compra")

time.sleep(1.5)

lista_menu, test_list = listar(nav, 'webguiTreeNodeLabel')
time.sleep(1.5)
click_producao = test_list.loc[test_list[0] == 'Consultas'].reset_index(drop=True)['index'][0]

lista_menu[click_producao].click() ##clicando em producao

logging.info("Navegando para o Consultas")

time.sleep(1.5)

lista_menu, test_list = listar(nav, 'webguiTreeNodeLabel')
time.sleep(1.5)
click_producao = test_list.loc[test_list[0] == 'Análise de Pedidos Pendentes ou Baixados'].reset_index(drop=True)['index'][0]

lista_menu[click_producao].click() ##clicando em producao

print("Navegando para Análise de Pedidos Pendentes ou Baixados")

time.sleep(10)

#Emissão inicial
iframes(nav)

# WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[2]/table/tbody/tr/td[1]/input'))).click()
# WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[2]/table/tbody/tr/td[1]/input'))).send_keys(Keys.CONTROL + 'A')
# WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[2]/table/tbody/tr/td[1]/input'))).send_keys(Keys.DELETE)
# time.sleep(1.5)
# WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[2]/table/tbody/tr/td[1]/input'))).send_keys(data_inicio)
# time.sleep(1.5)
# WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[2]/table/tbody/tr/td[1]/input'))).send_keys(Keys.TAB)

WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[4]/table/tbody/tr/td[1]/input'))).click()
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.CONTROL + 'A')
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.DELETE)
time.sleep(1.5)
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(data_inicio)
time.sleep(1.5)
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.TAB)
time.sleep(1.5)
# WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vars"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[39]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.CONTROL + Keys.SHIFT + 'E')


WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[41]/td[4]/table/tbody/tr/td[1]/input'))).click()
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[41]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.CONTROL + 'A')
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[41]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.DELETE)
time.sleep(1.5)
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[41]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(data_inicio)
time.sleep(1.5)
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[41]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.TAB)
time.sleep(1.5)
WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/form/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[41]/td[4]/table/tbody/tr/td[1]/input'))).send_keys(Keys.CONTROL + Keys.SHIFT + 'E')

saindo_iframe(nav)

botao = WebDriverWait(nav, 99999).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[4]/span[2]')))
time.sleep(0.5)
botao.click()
time.sleep(0.5)

try:
    time.sleep(0.5)
    WebDriverWait(nav, 10).until(lambda nav: "hover" in botao.get_attribute("class"))
    time.sleep(1)
    botao.click()
except:
    pass

WebDriverWait(nav, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/table/tbody/tr/td[2]/div/div/div[2]'))).click()

botao = WebDriverWait(nav, 99999).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/span[2]')))
time.sleep(0.5)
botao.click()
time.sleep(0.5)

try:
    WebDriverWait(nav, 10).until(lambda nav: "hover" in botao.get_attribute("class"))
    time.sleep(1)
    botao.click()
except:
    pass


iframes(nav)

print("tentando achar botao de download")

WebDriverWait(nav, 99999).until(EC.element_to_be_clickable((By.ID, '_download_elt'))).click()
WebDriverWait(nav, 99999).until(EC.element_to_be_clickable((By.ID, '_download_elt'))).click()

time.sleep(1.5)

nav.close()

time.sleep(5)

latest_download_path = get_latest_download_path()
data = pd.read_csv(latest_download_path, sep=';', encoding='latin-1')

print("Tratando planilha...")

def remove_unwanted_chars(entry):
    return str(entry).replace('=', '').replace('"', '')

data = data.applymap(remove_unwanted_chars)
data.columns = data.columns.map(remove_unwanted_chars)

data['Baixa'] = data['Baixa'].shift(-1)
data['Movimentação'] = data['Movimentação'].shift(-1)
data['Tipo'] = data['Tipo'].shift(-1)
data['Número'] = data['Número'].shift(-1)
data['Qde Baixa'] = data['Qde Baixa'].shift(-1)
data['Op. Vinculada'] = data['Op. Vinculada'].shift(-1)

data['Movimentação'] = pd.to_datetime(data['Movimentação'],errors='ignore', format='%d/%m/%Y')#
data = data.sort_values(by='Movimentação', ascending=True)
data['Movimentação'] = pd.to_datetime(data['Movimentação'],errors='ignore', format='%d/%m/%Y').dt.strftime("%d/%m/%Y")

for i in range(len(data)):

    if data['Pessoa'][i] != 'NORTH-CROMO' and data['Número'][i] == 'nan':

        data = data.drop(index=i) 
        print(i)           

data = data.reset_index(drop=True)

for i in range(len(data)):

    if data['Classe'][i] == 'V ProdPrópria p Consumo' and data['Núcleo'][i] != 'Almox Devol Vendas':

        data = data.drop(index=i)       

# Aplicando a função em 'Total'

data['Qde Baixa'] = data['Qde Baixa'].fillna('0')
data['Qde Baixa'] = data['Qde Baixa'].apply(lambda x: float(x.replace(',' , '.')))

data['Chave ¹   Ch Criação ²_'] = data['Chave ¹   Ch Criação ²'].apply(lambda x: x.split()[2] if len(x.split()) > 2 else None)
#data['Movimentação'] = pd.to_datetime(data['Movimentação']).dt.strftime("%d/%m/%Y")

data['Recurso_'] = data['Recurso'].apply(lambda x: x.split()[0])

print("Tratamento finalizado...")

def create_column_classe(df):

    filename = 'service_account.json'    
    
    sheet_id = '1SCoRVsTgA9JDvxib5D1I8N718hFZjsWqo6sXMWloFos'
    worksheet1 = 'Relação dos Materiais para inspeção'

    sa = gspread.service_account(filename)
    sh = sa.open_by_key(sheet_id)

    wks1 = sh.worksheet(worksheet1)

    headers = wks1.row_values(1)

    base = wks1.get()
    base = pd.DataFrame(base)    
    
    base = base.set_axis(headers, axis=1)[1:]

    # df['Classe de Inspeção'] = 
    base_tratada = df.merge(base,how='left',left_on='Recurso_', right_on='Código')
    base_tratada['Classe_y'] = base_tratada['Classe_y'].fillna('Não Aplicável')
    base_tratada = base_tratada.drop(columns={'Código','Descrição'})

    return base_tratada

base_final = create_column_classe(data)

def inserir_gspread(base):

    # Autentique-se com a API do Google Sheets (configure o caminho para suas credenciais)
    gc = gspread.service_account(filename=r'service_account.json')
    #gc = gspread.service_account(filename='service_account_cemag.json')
    
    # Abra a planilha com base no ID
    planilha = gc.open_by_key("1SCoRVsTgA9JDvxib5D1I8N718hFZjsWqo6sXMWloFos")

    # Acessar a aba "BD_saldo_diario"
    aba = planilha.worksheet("Relatório de Pedidos")

    # Defina o intervalo (range) que você deseja apagar (por exemplo, A2:H5)
    range_to_clear = "A2:Z"
    
    # Obtém a lista de células no intervalo especificado
    cell_list = aba.range(range_to_clear)
    
    # Define o valor de todas as células no intervalo como uma string vazia ('')
    for cell in cell_list:
        cell.value = ""
    
    # Atualiza as células no intervalo com os valores vazios
    aba.update_cells(cell_list)
    
    base['Número'] = base['Número'].fillna('nan').apply(lambda x: (x.replace('.0','')))
    base['Unitário'] = base['Unitário'].apply(lambda x: float(x.replace(',','.')))
    base['Total'] = base['Total'].apply(lambda x: abs(float(x.replace(',','.'))))
    base['Qde Ped'] = base['Qde Ped'].apply(lambda x: float(x.replace(',','.')))
    base['Qde Atend'] = base['Qde Atend'].apply(lambda x: float(x.replace(',','.')))
    base['Qde Canc'] = base['Qde Canc'].apply(lambda x: float(x.replace(',','.')))
    base['Qde Pend'] = base['Qde Pend'].apply(lambda x: float(x.replace(',','.')))
    base = base.fillna('')
    base = base.replace('nan','')
    
    # base['Movimentação'] = pd.to_datetime(base['Movimentação'],format="%d/%m/%Y")
    df_values = base.values.tolist()

    planilha.values_append("Relatório de Pedidos", {'valueInputOption': 'RAW'}, {'values': df_values})

    return 'sucess'

print("Inserindo no google sheets...")

inserir_gspread(base_final)

print("Dados inseridos com sucesso")