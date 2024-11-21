import pandas as pd

def pipeline(caminho_do_csv: str, caminho_salvar: str):
    '''
        Esse código lê o arquivo, acrescenta coluna e salva outro csv.
    '''
    df = ler_csv(caminho_do_csv)
    df = calcular_vendas_categoria(df)
    salvando_em_csv(df,caminho_salvar)

def ler_csv(caminho_do_csv: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_do_csv)
    return df

def calcular_vendas_categoria(df: pd.DataFrame) -> pd.DataFrame:
    df["tota_vendas"] = df["Quantidade"]*df["Venda"]
    return df

def salvando_em_csv(df: pd.DataFrame, caminho_salvar: str):
    print('Arquivo salvo!')
    df.to_csv(caminho_salvar)


'''
df = ler_csv('data/vendas.csv')
df = calcular_vendas_categoria(df)
salvando_em_csv(df,'data/novo_vendas.csv')
'''