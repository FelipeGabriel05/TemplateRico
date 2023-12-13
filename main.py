import titulo
import banco
import negocios
import resumo_negocios
import resumo_financeiro

def Main():
    TemplateRico = {
        "Titulo": titulo.Titulo(),
        "Corretora": titulo.Corretora(),
        "Cliente": titulo.Cliente(),
        "Banco": banco.Banco(),
        "Negocios Realizados": negocios.Negocios(),
        "Resumo dos Negocios": resumo_negocios.Resumo_Negocios(),
        "Resumo Financeiro": resumo_financeiro.Resumo_financeiro(),
        "Observações": resumo_negocios.Observacoes()
    }
    print(TemplateRico)
    return TemplateRico
    
if __name__ == '__main__':
    Main()