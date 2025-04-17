import csv
import pandas as pd
import re
import os

def detectar_delimiter(caminho_csv, sample_size=2048):
    """
    Detecta automaticamente o delimitador do CSV (vírgula, ponto‑e‑vírgula, tab ou pipe).
    """
    with open(caminho_csv, 'r', encoding='utf-8', errors='ignore') as f:
        sample = f.read(sample_size)
    try:
        return csv.Sniffer().sniff(sample, delimiters=[',',';','\t','|']).delimiter
    except csv.Error:
        return max([',',';','\t','|'], key=sample.count)

def normalizar_header(colunas):
    """
    Mapeia nomes originais para ['Data','Valor','Descricao'].
    Usa palavras‑chave e ignora acentos.
    """
    m = {}
    for col in colunas:
        low = col.lower()
        # remove acentos básicos
        low = re.sub(r'[áàãâä]', 'a', low)
        low = re.sub(r'[éèêë]', 'e', low)
        low = re.sub(r'[íìîï]', 'i', low)
        low = re.sub(r'[óòõôö]', 'o', low)
        low = re.sub(r'[úùûü]', 'u', low)
        if 'data' in low:
            m[col] = 'Data'
        elif 'valor' in low or 'vlr' in low:
            m[col] = 'Valor'
        elif 'descri' in low or 'hist' in low:
            m[col] = 'Descricao'
    return m

def ler_csv_organizado(caminho_csv):
    """
    Lê qualquer CSV, detecta separador e cabeçalho, e retorna DataFrame
    com colunas ['Data','Valor','Descricao'].
    """
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")

    sep = detectar_delimiter(caminho_csv)
    df = pd.read_csv(caminho_csv, sep=sep, dtype=str, engine='python')

    # tenta mapear header existente
    mapping = normalizar_header(df.columns)
    preciso = {'Data','Valor','Descricao'}
    if set(mapping.values()) >= preciso:
        df = df.rename(columns=mapping)[['Data','Valor','Descricao']]
    else:
        # fallback: assume as 3 primeiras colunas
        df = df.iloc[:, :3]
        df.columns = ['Data','Valor','Descricao']

    # converte tipos
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')
    v = df['Valor'].astype(str).str.replace(r'\.', '', regex=True).str.replace(',', '.', regex=False)
    df['Valor'] = pd.to_numeric(v, errors='coerce')
    df.dropna(subset=['Data','Valor'], inplace=True)

    return df

def filtrar_periodo(df, inicio, fim):
    """
    Filtra o DataFrame entre duas datas (strings 'dd/mm/yyyy').
    """
    d0 = pd.to_datetime(inicio, dayfirst=True)
    d1 = pd.to_datetime(fim,    dayfirst=True)
    return df[(df['Data'] >= d0) & (df['Data'] <= d1)].copy()

if __name__ == "__main__":
    arquivo = r"C:\Users\User\Downloads\controle\con0325.csv"
    df = ler_csv_organizado(arquivo)

    # Entrada interativa do período
    print("Informe o período que deseja filtrar:")
    inicio = input("  Data início (dd/mm/yyyy): ").strip()
    fim    = input("  Data   fim  (dd/mm/yyyy): ").strip()

    df_periodo = filtrar_periodo(df, inicio, fim)

    # Exibe resultados
    print(f"\n🔍 Transações de {inicio} a {fim}:")
    print(df_periodo.to_string(index=False, columns=['Data','Valor','Descricao']))

    total = df_periodo['Valor'].sum()
    print(f"\n📊 Total no período: R$ {total:.2f}")

