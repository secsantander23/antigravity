# Relatório de Qualidade de Dados (Skill conferir-csv)

## 1. Identificação do Arquivo
- **Arquivo:** `dados/forne2.csv`
- **Total de linhas:** 4
- **Total de colunas:** 5
- **Linhas duplicadas:** 0

---

## 2. Problemas Encontrados e Evidências
Foram identificados **valores ausentes (nulos)** na base:

| Coluna | Tipo de Dado | Valores Ausentes | Percentual Ausente |
|---|---|---|---|
| `fornecedor` | object (texto) | 0 | 0.0% |
| `preco_unitario` | float64 (numérico) | 1 | 25.0% |
| `prazo_dias` | int64 (numérico) | 0 | 0.0% |
| `defeitos_pct` | float64 (numérico) | 0 | 0.0% |
| `suporte_nota` | float64 (numérico) | 1 | 25.0% |

### Ocorrências específicas:
- **Fornecedor Beta** (linha 3 do arquivo): campo `suporte_nota` está vazio / nulo.
- **Fornecedor Delta** (linha 5 do arquivo): campo `preco_unitario` está vazio / nulo.

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
