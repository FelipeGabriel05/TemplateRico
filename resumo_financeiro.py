import text
import pdfplumber
import nome_arquivo

def Resumo_financeiro():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        coluna_resumo = page.crop((300, 400, page.width, 700))    
        table_settings = {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",
            "explicit_vertical_lines": [299, 400, 520, 545, 557],
            "explicit_horizontal_lines": [450, 460, 470, 480, 490, 500, 
                    507, 517, 527, 535, 545, 552, 562,
                572, 582, 592, 600, 610, 619, 629, 639,
                649, 659]
        }
        table_resumo = coluna_resumo.extract_table(table_settings)
        
        obj_clearing = {
            "Valor_liquido_das_operacoes": {
                "Valor": table_resumo[2][2],
                "DC": table_resumo[2][3]
            },
            "Taxa de Liquidacao": {
                "Valor": table_resumo[3][2],
                "Dc": table_resumo[3][3]
            },
            "Taxa de Registro": {
                "Valor": table_resumo[4][2],
                "DC": table_resumo[4][3]
            },
            "Total CBLC": {
                "Valor": table_resumo[5][2],
                "DC": table_resumo[5][3]
            }
        }
        
        obj_bolsa = {
            "Taxa de Termos_Opcoes": {
                "Valor": table_resumo[7][2],
                "DC": table_resumo[7][3]
            },
            "Taxa_A_N_A": {
                "Valor": table_resumo[8][2],
                "DC": table_resumo[8][3]
            },
            "Emolumentos": {
                "Valor": table_resumo[9][2],
                "DC": table_resumo[9][3]
            },
            "Total_BOVESPA_SOMA": {
                "Valor": table_resumo[10][2],
                "DC": table_resumo[10][3]
            }
        }
        
        obj_resumo = { 
            "Taxa_Operacional": {
                "Valor": table_resumo[13][2],
                "DC": table_resumo[13][3]
            },
            "Execucao": {
                "Valor":   table_resumo[14][2],
                "DC": table_resumo[14][3]
            },
            "Taxa_de_custodia": {
                "Valor":  table_resumo[15][2],
                "DC": table_resumo[15][3]
            },
            "Impostos": {
                "Valor": table_resumo[16][2],
                "DC": table_resumo[16][3]
            },
            f"{table_resumo[17][0]}":  {
                "Valor": table_resumo[17][2],
                "DC": table_resumo[17][3]
            },
            "Outros": {
                "Valor": table_resumo[18][2],
                "DC": table_resumo[18][3]
            },
            "Total_custos_despesas": {
                "Valor": table_resumo[19][2],
                "DC": table_resumo[19][3]
            },
            f"{table_resumo[20][0]}":  {
                "Valor": table_resumo[20][2],
                "DC": table_resumo[20][3]
            },
            "Observacao":  f"{table_resumo[21][0]}{table_resumo[21][1]}",
        }
        
        obj = {
            "Clearing": obj_clearing,
            "Bolsa": obj_bolsa,
            "Custos": obj_resumo
        }
        return obj
