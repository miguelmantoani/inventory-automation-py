import pandas as pd
import os
from datetime import datetime

# --- PASSO 1: CRIAR DADOS DE EXEMPLO (Só para teste) ---
# Se o arquivo já existir, não criamos de novo.
def criar_planilha_exemplo():
    if not os.path.exists('estoque.xlsx'):
        dados = {
            'Produto': ['Teclado Mecânico', 'Mouse Gamer', 'Monitor 24"', 'Cabo HDMI', 'Webcam 1080p'],
            'Quantidade_Atual': [5, 12, 2, 50, 4],
            'Estoque_Minimo': [10, 5, 5, 20, 10],
            'Preco_Unitario': [250.00, 120.00, 800.00, 25.00, 150.00]
        }
        df = pd.DataFrame(dados)
        df.to_excel('estoque.xlsx', index=False)
        print("✅ Planilha 'estoque.xlsx' criada com sucesso para testes.")
    else:
        print("ℹ️ Planilha 'estoque.xlsx' já existe.")

# --- PASSO 2: LÓGICA DE AUTOMACAO ---
def processar_estoque():
    print("🔄 Lendo planilha de estoque...")
    
    # Lê o arquivo Excel
    try:
        df = pd.read_excel('estoque.xlsx')
    except FileNotFoundError:
        print("❌ Erro: O arquivo 'estoque.xlsx' não foi encontrado.")
        return

    # Filtra: Onde a Quantidade Atual é MENOR que o Mínimo
    compras_necessarias = df[df['Quantidade_Atual'] < df['Estoque_Minimo']]

    if compras_necessarias.empty:
        print("✅ Tudo certo! Nenhum produto precisa de reposição.")
    else:
        print(f"⚠️ Atenção: {len(compras_necessarias)} produtos precisam de reposição.")
        gerar_relatorio(compras_necessarias)

# --- PASSO 3: GERAR RELATÓRIO (TXT) ---
def gerar_relatorio(df_compras):
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    nome_arquivo = "lista_de_compras.txt"
    
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"RELATÓRIO DE COMPRAS - {data_hoje}\n")
        f.write("="*40 + "\n\n")
        
        for index, row in df_compras.iterrows():
            qtd_comprar = row['Estoque_Minimo'] - row['Quantidade_Atual']
            custo_estimado = qtd_comprar * row['Preco_Unitario']
            
            f.write(f"PRODUTO: {row['Produto']}\n")
            f.write(f"  - Estoque Atual: {row['Quantidade_Atual']}\n")
            f.write(f"  - Mínimo Exigido: {row['Estoque_Minimo']}\n")
            f.write(f"  - Sugestão de Compra: {qtd_comprar} unidades\n")
            f.write(f"  - Custo Estimado: R$ {custo_estimado:.2f}\n")
            f.write("-" * 20 + "\n")
            
    print(f"📄 Relatório gerado com sucesso: {nome_arquivo}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    criar_planilha_exemplo() # Cria o excel se não existir
    processar_estoque()      # Roda a automação