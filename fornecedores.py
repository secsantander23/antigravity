import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregamento dos dados
caminho_dados = os.path.join("dados", "fornecedores.csv")
df = pd.read_csv(caminho_dados)

# 2. Definição dos critérios e pesos (total = 100%)
# Metodologia da skill decision-matrix
pesos = {
    "preco": 0.30,
    "prazo": 0.20,
    "defeitos": 0.30,
    "suporte": 0.20
}

# 3. Normalização das notas (escala de 1 a 10)
# Menor é melhor: Preço, Prazo, Defeitos
# Maior é melhor: Suporte
min_preco = df["preco_unitario"].min()
min_prazo = df["prazo_dias"].min()
min_defeitos = df["defeitos_pct"].min()
max_suporte = df["suporte_nota"].max()

df["nota_preco"] = 10 * (min_preco / df["preco_unitario"])
df["nota_prazo"] = 10 * (min_prazo / df["prazo_dias"])
df["nota_defeitos"] = 10 * (min_defeitos / df["defeitos_pct"])
df["nota_suporte"] = 10 * (df["suporte_nota"] / max_suporte)

# Contribuição ponderada de cada critério
df["contribuicao_preco"] = df["nota_preco"] * pesos["preco"]
df["contribuicao_prazo"] = df["nota_prazo"] * pesos["prazo"]
df["contribuicao_defeitos"] = df["nota_defeitos"] * pesos["defeitos"]
df["contribuicao_suporte"] = df["nota_suporte"] * pesos["suporte"]

# Pontuação total
df["pontuacao_total"] = (
    df["contribuicao_preco"] +
    df["contribuicao_prazo"] +
    df["contribuicao_defeitos"] +
    df["contribuicao_suporte"]
)

# Ordenação do melhor para o pior
df = df.sort_values(by="pontuacao_total", ascending=False).reset_index(drop=True)
df["ranking"] = df.index + 1
melhor = df.iloc[0]

# Garante a existência da pasta resultados/
os.makedirs("resultados", exist_ok=True)

# ----------------------------------------------------
# GRAFICO 1: Barras Empilhadas Aprimorado (analise_fornecedores.png)
# ----------------------------------------------------
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

fornecedores = df["fornecedor"].tolist()
y_pos = np.arange(len(fornecedores))

# Cores suaves e profissionais para cada critério
c_preco = "#3498db"     # Azul
c_prazo = "#9b59b6"     # Roxo
c_defeitos = "#2ecc71"  # Verde
c_suporte = "#f39c12"   # Laranja

# Barras horizontais empilhadas
p1 = ax.barh(y_pos, df["contribuicao_preco"], color=c_preco, label="Preco (30%)", height=0.55)
p2 = ax.barh(y_pos, df["contribuicao_prazo"], left=df["contribuicao_preco"], color=c_prazo, label="Prazo (20%)", height=0.55)
p3 = ax.barh(y_pos, df["contribuicao_defeitos"], left=df["contribuicao_preco"] + df["contribuicao_prazo"], color=c_defeitos, label="Qualidade/Defeitos (30%)", height=0.55)
p4 = ax.barh(y_pos, df["contribuicao_suporte"], left=df["contribuicao_preco"] + df["contribuicao_prazo"] + df["contribuicao_defeitos"], color=c_suporte, label="Suporte (20%)", height=0.55)

# Rótulo com pontuação total no final de cada barra
for i, total in enumerate(df["pontuacao_total"]):
    destaque = " [VENCEDOR]" if i == 0 else ""
    ax.text(total + 0.15, i, f"{total:.2f}{destaque}", va="center", ha="left", fontweight="bold", fontsize=11, color="#2c3e50")

ax.set_yticks(y_pos)
ax.set_yticklabels(fornecedores, fontsize=12, fontweight="bold")
ax.invert_yaxis()  # Melhor colocado no topo
ax.set_xlim(0, 11)
ax.set_xlabel("Pontuacao Total Ponderada (0 a 10)", fontsize=12, fontweight="bold")
ax.set_title("Analise de Fornecedores: Pontuacao Ponderada por Criterio", fontsize=14, fontweight="bold", pad=15)
ax.legend(loc="lower right", frameon=True, fontsize=10)
ax.grid(axis="x", linestyle="--", alpha=0.6)

caminho_g1 = os.path.join("resultados", "analise_fornecedores.png")
plt.tight_layout()
plt.savefig(caminho_g1, dpi=300)
plt.close()

# ----------------------------------------------------
# GRAFICO 2: Comparativo das Metricas Reais (comparativo_metricas.png)
# ----------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(11, 8), dpi=300)
df_plot = df.sort_values(by="fornecedor")

# Subplot 1: Preço
axes[0, 0].bar(df_plot["fornecedor"], df_plot["preco_unitario"], color="#3498db", edgecolor="black")
axes[0, 0].set_title("Preco Unitario (R$) - Menor e melhor", fontweight="bold")
axes[0, 0].set_ylabel("R$")
for bar in axes[0, 0].patches:
    axes[0, 0].annotate(f"R${bar.get_height():.0f}", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        ha="center", va="bottom", fontsize=10, fontweight="bold")

# Subplot 2: Prazo
axes[0, 1].bar(df_plot["fornecedor"], df_plot["prazo_dias"], color="#9b59b6", edgecolor="black")
axes[0, 1].set_title("Prazo de Entrega (Dias) - Menor e melhor", fontweight="bold")
axes[0, 1].set_ylabel("Dias")
for bar in axes[0, 1].patches:
    axes[0, 1].annotate(f"{bar.get_height():.0f}d", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        ha="center", va="bottom", fontsize=10, fontweight="bold")

# Subplot 3: Defeitos
axes[1, 0].bar(df_plot["fornecedor"], df_plot["defeitos_pct"], color="#e74c3c", edgecolor="black")
axes[1, 0].set_title("Taxa de Defeitos (%) - Menor e melhor", fontweight="bold")
axes[1, 0].set_ylabel("%")
for bar in axes[1, 0].patches:
    axes[1, 0].annotate(f"{bar.get_height():.1f}%", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        ha="center", va="bottom", fontsize=10, fontweight="bold")

# Subplot 4: Suporte
axes[1, 1].bar(df_plot["fornecedor"], df_plot["suporte_nota"], color="#2ecc71", edgecolor="black")
axes[1, 1].set_title("Nota do Suporte (0 a 10) - Maior e melhor", fontweight="bold")
axes[1, 1].set_ylabel("Nota")
for bar in axes[1, 1].patches:
    axes[1, 1].annotate(f"{bar.get_height():.1f}", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        ha="center", va="bottom", fontsize=10, fontweight="bold")

for ax_i in axes.flat:
    ax_i.grid(axis="y", linestyle="--", alpha=0.5)

fig.suptitle("Comparativo dos Dados Brutos por Criterio", fontsize=15, fontweight="bold")
plt.tight_layout()
caminho_g2 = os.path.join("resultados", "comparativo_metricas.png")
plt.savefig(caminho_g2, dpi=300)
plt.close()

# ----------------------------------------------------
# GRAFICO 3: Grafico Radar de Perfil (radar_fornecedores.png)
# ----------------------------------------------------
categorias = ["Preco", "Prazo", "Qualidade\n(Defeitos)", "Suporte"]
N = len(categorias)
angulos = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angulos += angulos[:1]  # Fechar o círculo do radar

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)
cores_radar = {"Delta": "#27ae60", "Beta": "#2980b9", "Alfa": "#e67e22", "Gama": "#c0392b"}

for _, row in df.iterrows():
    nome = row["fornecedor"]
    valores = [row["nota_preco"], row["nota_prazo"], row["nota_defeitos"], row["nota_suporte"]]
    valores += valores[:1]
    estilo_linha = "-" if nome == melhor["fornecedor"] else "--"
    largura = 3.0 if nome == melhor["fornecedor"] else 1.8
    ax.plot(angulos, valores, linewidth=largura, linestyle=estilo_linha, label=f"{nome} (Total: {row['pontuacao_total']:.2f})", color=cores_radar[nome])
    ax.fill(angulos, valores, color=cores_radar[nome], alpha=0.12 if nome == melhor["fornecedor"] else 0.05)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(categorias, fontsize=11, fontweight="bold")
ax.set_ylim(0, 10.5)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=9)
ax.set_title("Perfil Competitivo dos Fornecedores (Escala Normalizada 0-10)", fontsize=14, fontweight="bold", pad=25)
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1), frameon=True, fontsize=10)

plt.tight_layout()
caminho_g3 = os.path.join("resultados", "radar_fornecedores.png")
plt.savefig(caminho_g3, dpi=300)
plt.close()

# ----------------------------------------------------
# GRAFICO 4: Trade-off Preço vs Desempenho Global (tradeoff_preco_desempenho.png)
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)

for _, row in df.iterrows():
    cor = "#27ae60" if row["fornecedor"] == melhor["fornecedor"] else "#2980b9"
    tamanho = 280 if row["fornecedor"] == melhor["fornecedor"] else 160
    ax.scatter(row["preco_unitario"], row["pontuacao_total"], color=cor, s=tamanho, edgecolor="black", zorder=3)
    ax.annotate(f"{row['fornecedor']}\n({row['pontuacao_total']:.2f} pts | R$ {row['preco_unitario']:.0f})",
                (row["preco_unitario"], row["pontuacao_total"]),
                textcoords="offset points", xytext=(0, 10), ha="center", fontweight="bold", fontsize=10)

ax.set_title("Analise de Trade-off: Preco Unitario vs Pontuacao Geral", fontsize=13, fontweight="bold")
ax.set_xlabel("Preco Unitario (R$) - Menor custo a esquerda", fontsize=11)
ax.set_ylabel("Pontuacao Ponderada Final (0-10)", fontsize=11)
ax.grid(True, linestyle="--", alpha=0.6)
ax.set_ylim(4.5, 10.5)
ax.set_xlim(80, 115)

plt.tight_layout()
caminho_g4 = os.path.join("resultados", "tradeoff_preco_desempenho.png")
plt.savefig(caminho_g4, dpi=300)
plt.close()

# ----------------------------------------------------
# Atualização do Relatório Markdown
# ----------------------------------------------------
caminho_relatorio = os.path.join("resultados", "relatorio_fornecedores.md")

linhas_tabela = ""
for _, row in df.iterrows():
    linhas_tabela += (
        f"| {int(row['ranking'])} | **{row['fornecedor']}** | "
        f"R$ {row['preco_unitario']:.2f} ({row['nota_preco']:.2f}) | "
        f"{row['prazo_dias']} dias ({row['nota_prazo']:.2f}) | "
        f"{row['defeitos_pct']}% ({row['nota_defeitos']:.2f}) | "
        f"{row['suporte_nota']:.1f} ({row['nota_suporte']:.2f}) | "
        f"**{row['pontuacao_total']:.2f}** |\n"
    )

conteudo_relatorio = f"""# Relatorio de Selecao de Fornecedores (Decision Matrix)

## Contexto da Decisao
Avaliacao e selecao do melhor parceiro fornecedor com base nos dados historicos de `dados/fornecedores.csv`, aplicando a metodologia da skill **decision-matrix** e diretrizes de visualizacao da skill **chart-image**.

### Criterios e Pesos Definidos
- **Qualidade (Taxa de Defeitos):** 30% (menor e melhor)
- **Preco Unitario:** 30% (menor e melhor)
- **Prazo de Entrega:** 20% (menor e melhor)
- **Suporte Tecnico:** 20% (maior e melhor)

---

## Matriz de Decisao

| Posicao | Fornecedor | Preco (30%) | Prazo (20%) | Defeitos (30%) | Suporte (20%) | Pontuacao Total |
|---|---|---|---|---|---|---|
{linhas_tabela}

---

## Recomendacao Final

O fornecedor recomendado e o **{melhor['fornecedor']}** com pontuacao final de **{melhor['pontuacao_total']:.2f} / 10.00**.

### Justificativa e Trade-offs
1. **Pontos Fortes do Vencedor ({melhor['fornecedor']}):**
   - **Menor taxa de defeitos:** apenas {melhor['defeitos_pct']}%, garantindo alta qualidade.
   - **Menor prazo de entrega:** apenas {melhor['prazo_dias']} dias para entrega.
   - **Melhor suporte:** nota {melhor['suporte_nota']} de avaliacao pos-venda.
2. **Trade-off aceito:**
   - Possui o preco unitario mais alto (R$ {melhor['preco_unitario']:.2f}), porem o ganho substancial em pontualidade, suporte e baixissima taxa de retrabalho/defeitos compensa amplamente o custo.

---

## Galeria de Graficos Gerados
Todos os graficos foram gerados em alta resolucao (300 DPI) na pasta `resultados/`:
1. `resultados/analise_fornecedores.png`: Grafico principal de barras empilhadas mostrando o peso de cada criterio na nota final.
2. `resultados/comparativo_metricas.png`: Painel 2x2 com as metricas reais de cada fornecedor.
3. `resultados/radar_fornecedores.png`: Grafico radar comparando a amplitude de cada fornecedor em todas as dimensoes.
4. `resultados/tradeoff_preco_desempenho.png`: Dispersao de Preco vs Desempenho Global.
"""

with open(caminho_relatorio, "w", encoding="utf-8") as f:
    f.write(conteudo_relatorio)

print("=== PROCESSAMENTO CONCLUIDO COM SUCESSO ===")
print(f"1. Fornecedor Vencedor: {melhor['fornecedor']} ({melhor['pontuacao_total']:.2f} pontos)")
print(f"2. Grafico Principal: {caminho_g1}")
print(f"3. Metricas Brutas: {caminho_g2}")
print(f"4. Grafico Radar: {caminho_g3}")
print(f"5. Trade-off Preco/Desempenho: {caminho_g4}")
print(f"6. Relatorio Atualizado: {caminho_relatorio}")
