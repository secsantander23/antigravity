---
name: dataset-leakage-guard
description: Audita pipelines de dados e Machine Learning antes do treinamento para detectar e bloquear vazamento de dados (Data Leakage), contaminação entre treino e teste e target leakage.
---

# Dataset Leakage Guard (Guardião Anti-Vazamento de Dados)

## Visão Geral
O vazamento de dados (*Data Leakage*) é a falha silenciosa mais perigosa em Ciência de Dados: o modelo atinge métricas quase perfeitas durante o desenvolvimento, mas quebra completamente quando vai para a produção. Esta skill realiza uma auditoria rigorosa de código e variáveis antes que qualquer modelo de Machine Learning seja treinado.

---

## Quando Utilizar
- Antes de rodar etapas de treino de modelos preditivos (como churn, fraude, regressão ou classificação).
- Ao realizar pré-processamento de dados (escalonamento, imputação, codificação de categorias).
- Sempre que a acurácia ou AUC do modelo parecer "boa demais para ser verdade" (>95%).

---

## Os 4 Pilares de Auditoria Anti-Leakage

### 1. Vazamento do Alvo (Target Leakage)
- Verifica se a coluna alvo (ex.: `Churn`, `Fraude`) ou qualquer coluna derivada do futuro foi deixada acidentalmente dentro da matriz de entrada `X`.
- Detecta identificadores únicos (como `customerID`, `id_transacao`) que podem decorar dados sem generalizar.

### 2. Contaminação no Pré-Processamento (Fit/Transform Isolation)
- **Regra de Ouro:** Métodos de ajuste como `scaler.fit()`, `imputer.fit()` ou `encoder.fit()` **devem ser executados exclusivamente nos dados de treino**.
- Detecta chamadas proibidas de `fit_transform()` executadas no dataset completo antes da divisão de treino e teste.

### 3. Vazamento Temporal (Time-Series & Cutoff Leakage)
- Em dados com carimbo de tempo, valida se o split foi feito por linha do tempo (passado para treino, futuro para teste) em vez de um sorteio aleatório (`random train_test_split`).

### 4. Isolamento do Conjunto de Teste Final
- Garante que o conjunto de teste permaneça intocado e seja avaliado **uma única vez** no fechamento do projeto, evitando overfitting por tentativa e erro.

---

## Checklist de Liberação da Skill

```
Checklist de Segurança ML:
- [ ] O alvo (Target) foi 100% removido das features de entrada?
- [ ] Identificadores únicos foram excluídos?
- [ ] Todos os scalers/encoders foram ajustados (fit) APENAS no treino?
- [ ] O conjunto de validação foi usado para comparar os modelos?
- [ ] O conjunto de teste permaneça preservado para a validação final?
```

