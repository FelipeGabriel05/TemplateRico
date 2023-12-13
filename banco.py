import nome_arquivo
import pdfplumber

def Banco():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        coluna_banco1 = page.crop((20, 180, page.width, 200))
        banco1_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [231, 320, 420, 533, 560],
            "explicit_horizontal_lines": [180, 186, 194]
        }
        banco1 = coluna_banco1.extract_table(banco1_settings)
        
        coluna_banco2 = page.crop((20, 200, page.width, 220))
        banco2_settings = {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",
            "explicit_horizontal_lines": [200, 205, 215],
            "explicit_vertical_lines": [33, 60, 140, 230, 320, 422, 530, 560]
        }
        
        banco2 = coluna_banco2.extract_table(banco2_settings)
        obj_banco = {
            "Participante_Destino_do_Repasse": banco1[1][1],
            "Cliente": banco1[1][2],
            "Valor": banco1[1][3],
            "Custodiante": banco1[1][4],
            "C_I": banco1[1][5],
            "Banco": banco2[1][1],
            "Agencia": banco2[1][2],
            "Conta_Corrente": banco2[1][3],
            "Acionista": banco2[1][4],
            "Administrador": banco2[1][5],
            "Complemento_Nome": banco2[1][6],
            "P_Vine": banco2[1][8]
        }
        return obj_banco
