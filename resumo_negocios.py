import pdfplumber
import nome_arquivo
import text

def Resumo_Negocios():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        
        coluna_resumo = page.crop((20, 400, 300, 540))
        resumo_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [34, 270],
            "explicit_horizontal_lines": [450, 460, 470, 480, 490, 500, 507,
                                            516, 526, 536]
        }
        table_resumo = coluna_resumo.extract_table(resumo_settings)
        
        coluna_especificacao = page.crop((20, 555, 300, 600))
        especificacao_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [555, 565, 590, 598]
        }
        table_especificacao = coluna_especificacao.extract_table(especificacao_settings)
        
        obj_resumo = {
            "Debentures": table_resumo[1][2],
            "Vendas_a_Vista": table_resumo[2][2],
            "Compras_a_vista": table_resumo[3][2],
            "Opcoes_compras": table_resumo[4][2],
            "Opcoes_vendas": table_resumo[5][2],
            "Operacoes_a_termo": table_resumo[6][2],
            "Valor_operecoes_Ctitulo": table_resumo[7][2],
            "Valor_Das_Operacoes": table_resumo[8][2],
            "Especificacoes_diversas": table_especificacao[2][1]
        }
        return obj_resumo
    
def Observacoes():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        row = text.Pegar_Texto(0)
        
        coluna_obs = page.crop((20, 640, 300, 745))    
        obs_settings= {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",    
            "horizontal_strategy": "text",
            "explicit_horizontal_lines": [650, 680, 680, 694, 710, 720, 740],
            "explicit_vertical_lines": [148, 210, 280]
        }
        
        table_obs = coluna_obs.extract_table(obs_settings)
        obj_obs = {
            "Tipo_titulo": table_obs[0][1],
            "Dados_A": table_obs[0][2],
            "Dados_T": table_obs[0][3],
            "Informacao_Corretora": table_obs[2][1],
            "Dados_C": table_obs[2][2],
            "Dados_I": table_obs[2][3],
            "Negocio": table_obs[4][1],
            "Dados_P": table_obs[4][2],
            "Dados_Liquidacao": table_obs[6][1],
            "Dados_H": table_obs[6][2],
            "Dados_D": table_obs[8][1],
            "Dados_X": table_obs[8][2],
            "Dados_F": table_obs[11][1],
            "Dados_Y": table_obs[11][2],
            "Dados_B": table_obs[13][1],
            "Dados_L": table_obs[13][2],
            "Informação_adicional": row[-1]
        }
        return obj_obs