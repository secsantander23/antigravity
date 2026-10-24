# Diretrizes do Agente (AGENTS.md)

Este documento estabelece as regras e padrões de trabalho para o assistente de IA neste projeto. Todas as instruções abaixo têm prioridade máxima e devem ser seguidas rigorosamente.

---

## 1. Como Trabalhar Comigo (Comunicação e Fluxo)
- **Linguagem acessível:** Responda sempre em português simples e didático (sou iniciante na área).
- **Foco estrito:** Execute exclusivamente a etapa solicitada, sem avançar para etapas posteriores por conta própria.
- **Autorização prévia para código:** Antes de rodar qualquer código ou comando, explique detalhadamente o que ele faz e aguarde minha confirmação explícita (enviando `"pode executar"` ou `"execut plan"`).
- **Fechamento padrão de cada etapa:** No final de cada resposta, informe sempre de maneira estruturada:
  1. **O que mudou:** resumo do que foi criado ou modificado.
  2. **Como eu confiro:** instruções claras de como inspecionar o resultado.
  3. **Qual é o próximo passo:** recomendação da ação a seguir.

---

## 2. Organização de Arquivos e Ambiente
- **Dados de entrada (`dados/`):** Todos os dados originais residem na pasta `dados/`. **Nunca altere, sobrescreva ou delete** esses arquivos.
- **Saídas e entregáveis (`resultados/`):** Grave tudo o que for gerado (relatórios `.md`, gráficos `.png`, análises, tabelas e modelos) exclusivamente dentro da pasta `resultados/`.
- **Ambiente virtual Python:** Utilize sempre o interpretador da pasta `.venv` (no Windows: `.\.venv\Scripts\python`).
- **Skills do projeto (`.agents/skills/`):** As habilidades customizadas ficam em `.agents/skills`. Sempre que uma skill for mencionada, leia atentamente o arquivo `SKILL.md` correspondente antes de executar a tarefa.

---

## 3. Honestidade e Rigor Técnico
- **Cálculos matemáticos:** Faça todas as contas e análises via código Python; nunca estime valores de cabeça nem faça aproximações subjetivas.
- **Veracidade dos dados:** Jamais invente métricas, dados estatísticos, resultados de testes ou chamadas de ferramentas.
- **Protocolo MCP:** Quando for solicitado o uso de MCP, utilize a ferramenta MCP adequada e informe explicitamente no chat o nome da ferramenta invocada.

---

## 4. Boas Práticas de Machine Learning
- **Prevenção de vazamento (Data Leakage):** Nunca utilize a coluna alvo (`Churn`) nem identificadores únicos (como `customerID`) como variáveis de entrada (features) dos modelos.
- **Ajuste de pré-processamento:** Qualquer transformação, escala ou imputação deve ser ajustada (`fit`) exclusivamente nos dados de **treino**, aplicando apenas a transformação (`transform`) na validação e no teste.
- **Critério de decisão:** Selecione e compare modelos com base nas métricas do conjunto de **validação**. O conjunto de **teste final** deve ser avaliado uma única vez ao término de todo o processo.
