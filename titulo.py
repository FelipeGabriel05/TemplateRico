import pdfplumber
import nome_arquivo
import text

def Titulo():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_Texto(0)
        
        linha_titulo = row[2].split()
        object_titulo = {
            'tipo_nota': row[0],
            'Nr_nota': linha_titulo[0],
            'Folha': linha_titulo[1],
            'Data_pregao': linha_titulo[2]
        }
        return object_titulo
    
def Corretora():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_Texto(0)
        page = pdf.pages[0]
        
        linha_telefonica =  row[5].split()
        informacoes_cabecalho1 = row[6].split()
        informacoes_cabecalho2 = row[7].split()
        informacoes_cabecalho3 = row[8].split()
        
        coluna_carta = page.crop((380, 118, page.width, 125))
        carta_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [390, 433, 563],
            "explicit_horizontal_lines": [124, 118]
        }
        carta = coluna_carta.extract_table(carta_settings)
        
        coluna_email = page.crop((390, 125, page.width, 138))
        email_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [390, 440, 563],
            "explicit_horizontal_lines": [131, 125]
        }
        emailOuvidoria = coluna_email.extract_table(email_settings)
        
        object_cabecalho = {
            "modelo": row[3],
            "endereco": row[4],
            "telefone": linha_telefonica[1],
            "Fax": f"{linha_telefonica[3]} {linha_telefonica[4]} {linha_telefonica[5]}",
            "Internet": informacoes_cabecalho1[1],
            "SAC": informacoes_cabecalho1[3],
            "email": informacoes_cabecalho1[5],
            "CNPJ": informacoes_cabecalho2[1],
            "Ouvidoria": informacoes_cabecalho3[2],
            "Carta_Patente": carta[0][2],
            "Email_Ouvidoria": emailOuvidoria[0][1]
        }
        return object_cabecalho

def Cliente():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_Texto(0)
        page = pdf.pages[0]
        
        num_cliente = row[10].split()
        coluna_info = page.crop((110, 151, 425, 180))
        info_cliente_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [132, 335, 348, 420],
            "explicit_horizontal_lines": [148, 155, 165, 175]
        }
        info_cliente = coluna_info.extract_table(info_cliente_settings)
        
        coluna_info2 = page.crop((420, 141, page.width, 180))
        cliente_settings2 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [520],
            "explicit_horizontal_lines": [150, 160, 166, 176]
        }
        info_cliente2 = coluna_info2.extract_table(cliente_settings2)

        obj_cliente = {
            "Cliente": num_cliente[0],
            "Nome_Cliente": info_cliente[0][1],
            "Endereco_CLiente": f"{info_cliente[1][1]} {info_cliente[2][1]}",
            "Telefone_CLiente": info_cliente[1][3],
            "CPF_CNPJ_CVM_COB": info_cliente2[0][0],
            "Codigo_cliente": info_cliente2[2][0],
            "Acessor": info_cliente2[2][1]
        }
        return obj_cliente
