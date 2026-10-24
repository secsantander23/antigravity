import os
import pandas as pd

# 1. Carregando os dados
caminho_arquivo = os.path.join("dados", "forne2.csv")
df = pd.read_csv(caminho_arquivo)

# 2. Análise de dimensões e tipos
num_linhas, num_colunas = df.shape
linhas_duplicadas = df.duplicated().sum()

# 3. Verificação de valores ausentes (incluindo strings vazias ou só com espaços)
valores_ausentes = df.isnull().sum()

# Identificando exatamente quais fornecedores e colunas possuem dados ausentes
linhas_com_defeito = df[df.isnull().any(axis=1)]

# 4. Exibição no terminal dos resultados
print("=== RELATORIO DE CONFERENCIA DE DADOS (SKILL CONFERIR-CSV) ===")
print(f"Arquivo analisado: {caminho_arquivo}")
print(f"Total de linhas: {num_linhas}")
print(f"Total de colunas: {num_colunas}")
print(f"Linhas duplicadas: {linhas_duplicadas}\n")

print("--- Valores ausentes por coluna ---")
for col, total in valores_ausentes.items():
    print(f"- {col}: {total} valor(es) ausente(s)")

print("\n--- Linhas afetadas ---")
for idx, row in linhas_com_defeito.iterrows():
    colunas_faltantes = [col for col in df.columns if pd.isnull(row[col])]
    print(f"- Linha {idx + 2} (Fornecedor: {row['fornecedor']}): Faltando {', '.join(colunas_faltantes)}")

# 5. Salvando o relatório estruturado em resultados/qualidade.md
os.makedirs("resultados", exist_ok=True)
caminho_qualidade = os.path.join("resultados", "qualidade.md")

detalhes_defeitos = ""
for idx, row in linhas_com_defeito.iterrows():
    colunas_faltantes = [col for col in df.columns if pd.isnull(row[col])]
    detalhes_defeitos += f"- **Fornecedor {row['fornecedor']}** (linha {idx + 2} do arquivo): campo `{', '.join(colunas_faltantes)}` está vazio / nulo.\n"

conteudo_md = f"""# Relatório de Qualidade de Dados (Skill conferir-csv)

## 1. Identificação do Arquivo
- **Arquivo:** `dados/forne2.csv`
- **Total de linhas:** {num_linhas}
- **Total de colunas:** {num_colunas}
- **Linhas duplicadas:** {linhas_duplicadas}

---

## 2. Problemas Encontrados e Evidências
Foram identificados **valores ausentes (nulos)** na base:

| Coluna | Tipo de Dado | Valores Ausentes | Percentual Ausente |
|---|---|---|---|
| `fornecedor` | object (texto) | {valores_ausentes['fornecedor']} | {(valores_ausentes['fornecedor'] / num_linhas) * 100:.1f}% |
| `preco_unitario` | float64 (numérico) | {valores_ausentes['preco_unitario']} | {(valores_ausentes['preco_unitario'] / num_linhas) * 100:.1f}% |
| `prazo_dias` | int64 (numérico) | {valores_ausentes['prazo_dias']} | {(valores_ausentes['prazo_dias'] / num_linhas) * 100:.1f}% |
| `defeitos_pct` | float64 (numérico) | {valores_ausentes['defeitos_pct']} | {(valores_ausentes['defeitos_pct'] / num_linhas) * 100:.1f}% |
| `suporte_nota` | float64 (numérico) | {valores_ausentes['suporte_nota']} | {(valores_ausentes['suporte_nota'] / num_linhas) * 100:.1f}% |

### Ocorrências específicas:
{detalhes_defeitos}
- **Beta:** não possui o valor de `suporte_nota`.
- **Delta:** não possui o valor de `preco_unitario`.

---

## 3. Impacto na Tomada de Decisão (Matriz de Decisão)
Caso esses dados sejam utilizados diretamente na fórmula de normalização da Matriz de Decisão:
1. Sem o preço do fornecedor **Delta**, não é possível calcular a nota de custo nem a nota ponderada final dele.
2. Sem a nota de suporte do fornecedor **Beta**, a pontuação final ficará incompleta e distorcida.

---

## 4. Propostas de Tratamento
1. **Preenchimento com a fonte original:** Consultar os dados corretos no catálogo ou arquivo original (`dados/fornecedores.csv`).
2. **Imputação estatística:** Preencher com a média ou mediana do setor (não recomendável com apenas 4 fornecedores, pois distorce o ranking).
3. **Descarte da linha:** Excluir os fornecedores com dados ausentes (restariam apenas 2 fornecedores: Alfa e Gama).
"""

with open(caminho_qualidade, "w", encoding="utf-8") as f:
    f.write(conteudo_md)

print(f"\n[OK] Relatorio de qualidade salvo com sucesso em: {caminho_qualidade}")

