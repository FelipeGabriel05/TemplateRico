import pdfplumber
import nome_arquivo

def Negocios():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        
        bloco_registros = page.crop((20, 240, page.width, 450))
        tabela_registros = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [33, 45, 88, 104, 162,
                                        184.5, 300, 350, 400, 450, 548, 555]
        }
        
        table_negocios = bloco_registros.extract_table(tabela_registros)
        total_negocios = {}
        contagem = 1
        while contagem <= len(table_negocios) - 1:
            obj_negocios = {
                "Q": table_negocios[contagem][0],
                "Negociacao": table_negocios[contagem][1],
                "C/V": table_negocios[contagem][2],
                "Tipo_Mercado": table_negocios[contagem][3],
                "Prazo": table_negocios[contagem][4],
                "Especificacao_do_Titulo": table_negocios[contagem][5],
                "OBS": table_negocios[contagem][6],
                "Quantidade": table_negocios[contagem][7],
                "Preco_Ajuste": table_negocios[contagem][8],
                "Valor_Operacao_Ajuste": table_negocios[contagem][9],
                "D_C": table_negocios[contagem][10]
            }
            total_negocios[f"negocio_{contagem}"] = obj_negocios
            contagem += 1
            return total_negocios
