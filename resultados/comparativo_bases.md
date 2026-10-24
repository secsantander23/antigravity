# Relatório de Comparação entre Bases

Comparação célula a célula entre o arquivo original ([dados/fornecedores.csv](../dados/fornecedores.csv)) e a nova base ([dados/forne2.csv](../dados/forne2.csv)).

## Resumo das Divergências Encontradas

Foram detectados **3 erros** na base `forne2.csv`:

| Fornecedor | Coluna Afetada | Original (`fornecedores.csv`) | Novo (`forne2.csv`) | Tipo de Problema |
|---|---|---|---|---|
| **Beta** | `suporte_nota` | `9.0` | `Vazio / Nulo` | Valor Faltante (Nulo) |
| **Gama** | `defeitos_pct` | `4.0` | `6.0` | Valor Modificado/Incorreto |
| **Delta** | `preco_unitario` | `110` | `Vazio / Nulo` | Valor Faltante (Nulo) |


## Diagnóstico Detalhado por Fornecedor

1. **Alfa:**
   - **Status:** 100% íntegro e idêntico em todas as colunas.
2. **Beta:**
   - **Problema:** A nota de suporte foi apagada (ficou vazia). No original era `9.0`.
3. **Gama:**
   - **Problema:** A taxa de defeitos foi alterada de `4.0%` para `6.0%` (piora artificial da qualidade).
4. **Delta:**
   - **Problema:** O preço unitário foi apagado (ficou vazio). No original era `R$ 110.00`.

---
*Relatório gerado automaticamente por análise programática em Python.*
