# Relatorio de Selecao de Fornecedores (Decision Matrix)

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
| 1 | **Delta** | R$ 110.00 (7.73) | 4 dias (10.00) | 0.5% (10.00) | 9.5 (10.00) | **9.32** |
| 2 | **Beta** | R$ 100.00 (8.50) | 5 dias (8.00) | 1.0% (5.00) | 9.0 (9.47) | **7.54** |
| 3 | **Alfa** | R$ 90.00 (9.44) | 8 dias (5.00) | 2.0% (2.50) | 8.0 (8.42) | **6.27** |
| 4 | **Gama** | R$ 85.00 (10.00) | 12 dias (3.33) | 4.0% (1.25) | 6.0 (6.32) | **5.30** |


---

## Recomendacao Final

O fornecedor recomendado e o **Delta** com pontuacao final de **9.32 / 10.00**.

### Justificativa e Trade-offs
1. **Pontos Fortes do Vencedor (Delta):**
   - **Menor taxa de defeitos:** apenas 0.5%, garantindo alta qualidade.
   - **Menor prazo de entrega:** apenas 4 dias para entrega.
   - **Melhor suporte:** nota 9.5 de avaliacao pos-venda.
2. **Trade-off aceito:**
   - Possui o preco unitario mais alto (R$ 110.00), porem o ganho substancial em pontualidade, suporte e baixissima taxa de retrabalho/defeitos compensa amplamente o custo.

---

## Galeria de Graficos Gerados
Todos os graficos foram gerados em alta resolucao (300 DPI) na pasta `resultados/`:
1. `resultados/analise_fornecedores.png`: Grafico principal de barras empilhadas mostrando o peso de cada criterio na nota final.
2. `resultados/comparativo_metricas.png`: Painel 2x2 com as metricas reais de cada fornecedor.
3. `resultados/radar_fornecedores.png`: Grafico radar comparando a amplitude de cada fornecedor em todas as dimensoes.
4. `resultados/tradeoff_preco_desempenho.png`: Dispersao de Preco vs Desempenho Global.
