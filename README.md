# 🚀 Laboratório Antigravity: Agentes de IA & Engenharia de Dados

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Data Analysis](https://img.shields.io/badge/pandas-data--analysis-150458.svg)](https://pandas.pydata.org/)
[![Visualization](https://img.shields.io/badge/matplotlib-publication--quality-11557c.svg)](https://matplotlib.org/)
[![Agent Skills](https://img.shields.io/badge/antigravity-agent--skills-00A67E.svg)](https://github.com/secsantander23/antigravity)

Bem-vindo ao repositório do **Laboratório Antigravity**! Este projeto é um ambiente prático e estruturado de desenvolvimento assistido por Inteligência Artificial e Engenharia de Software. Aqui demonstramos fluxos completos de calibração matemática, análise multicritério de decisão, auditoria rigorosa de qualidade de dados e um catálogo inovador de **Skills para Agentes de Código**.

---

## 📁 Estrutura do Repositório

```text
aula-antigravity/
├── .agents/
│   └── skills/                       # Habilidades operacionais do agente de IA
│       ├── anti-hallucination-audit/ # Auditoria de métodos e bibliotecas antes da execução
│       ├── cost-token-optimizer/     # Compressão de código via AST para economia de tokens
│       ├── architecture-onboarding/  # Mapeamento visual e diagramas de fluxo do repositório
│       ├── dataset-leakage-guard/    # Bloqueio de vazamento de dados em Machine Learning
│       ├── decision-matrix/          # Matriz de decisão ponderada multicritério
│       ├── chart-image/              # Diretrizes de geração de gráficos de alta qualidade
│       ├── conferir-csv/             # Auditoria de integridade de arquivos tabulares
│       └── README.md                 # Catálogo e vitrine das skills em destaque
├── dados/                            # Dados originais e imutáveis (somente leitura)
│   ├── fornecedores.csv              # Dados base para seleção de fornecedores
│   └── forne2.csv                    # Base para testes de auditoria e detecção de anomalias
├── resultados/                       # Todos os entregáveis e artefatos gerados
│   ├── analise_fornecedores.png      # Gráfico de barras empilhadas por critério
│   ├── comparativo_metricas.png      # Painel 2x2 com os dados reais dos fornecedores
│   ├── radar_fornecedores.png        # Gráfico radar de amplitude e equilíbrio competitivo
│   ├── tradeoff_preco_desempenho.png # Dispersão entre custo e desempenho
│   ├── grafico_termometro.png        # Curva de resposta do sensor (4-20 mA)
│   ├── relatorio_fornecedores.md     # Relatório formal da Decision Matrix
│   ├── qualidade.md                  # Relatório de auditoria de dados nulos
│   └── comparativo_bases.md          # Auditoria comparativa célula a célula
├── AGENTS.md                         # Diretrizes de governança e comportamento do agente
├── termometro.py                     # Calibração linear de sensor de temperatura
├── fornecedores.py                   # Motor da Matriz de Decisão e gerador dos gráficos
├── conferir_dados.py                 # Script de validação e auditoria de CSV
├── comparar_bases.py                 # Comparador célula a célula entre datasets
├── .gitignore                        # Proteção de ambiente virtual e arquivos temporários
└── README.md                         # Este documento
```

---

## 🌟 Módulos e Exercícios Desenvolvidos

### 1. 🌡️ Calibração de Sensor Térmico (`termometro.py`)
- **Objetivo:** Modelar a curva de resposta de um transmissor de temperatura industrial padrão **4 a 20 mA** para a faixa de **0 a 100 °C**.
- **Equação da Reta:** Encontra matematicamente a relação $y = a \cdot x + b$ a partir dos pontos $(0, 4)$ e $(100, 20)$.
- **Classificação e Avisos:** Valida se a temperatura e a corrente estão dentro da faixa de operação e classifica a temperatura em Baixa ($\le 30^\circ\text{C}$), Média ($30\text{--}60^\circ\text{C}$) ou Alta ($> 60^\circ\text{C}$).
- **Saída:** Gráfico salvo em `resultados/grafico_termometro.png`.

### 2. ⚖️ Matriz de Decisão de Fornecedores (`fornecedores.py`)
- **Metodologia:** Aplicação estrita da skill `decision-matrix`.
- **Critérios Ponderados:** Preço Unitário (30%), Qualidade/Defeitos (30%), Prazo de Entrega (20%) e Suporte Técnico (20%).
- **Normalização Matemática:** Conversão de métricas em escala de 1 a 10 (onde valores menores são melhores para custo, prazo e defeito; e valores maiores são melhores para suporte).
- **Vencedor:** Fornecedor **Delta** (Nota final: **9.32 / 10.00**), justificando o investimento adicional em preço pela excelência em prazo, suporte e menor taxa de defeitos.
- **Visualizações (300 DPI):**
  - Barras empilhadas com contribuição de cada critério.
  - Painel 2x2 comparando métricas reais.
  - Gráfico radar de perfil competitivo.
  - Análise de trade-off de custo versus pontuação geral.

### 3. 🔍 Auditoria e Qualidade de Dados (`conferir_dados.py` & `comparar_bases.py`)
- **Detecção de Anomalias:** Aplicação da skill `conferir-csv` para identificar valores nulos e alterações espúrias na base `forne2.csv`.
- **Divergências Identificadas:**
  - Fornecedor **Beta**: nota de suporte ausente (apagada).
  - Fornecedor **Gama**: taxa de defeitos alterada de 4% para 6%.
  - Fornecedor **Delta**: preço unitário ausente (apagado).
- **Relatórios Gerados:** Documentados com evidências numéricas em `resultados/qualidade.md` e `resultados/comparativo_bases.md`.

---

## 🔥 Catálogo de Skills para Agentes (Trending no GitHub)

Localizadas na pasta `.agents/skills/`, estas habilidades foram desenhadas para resolver os maiores desafios de quem desenvolve com agentes de IA:

1. **🛡️ `anti-hallucination-audit`:** Inspeciona o ambiente local antes da execução, checando se imports, métodos e parâmetros existem de fato na versão instalada para eliminar 100% das alucinações.
2. **⚡ `cost-token-optimizer`:** Analisa arquivos grandes via AST e gera esqueletos semânticos enxutos, reduzindo o consumo de tokens em até 70% sem perder o contexto arquitetural.
3. **🗺️ `architecture-onboarding`:** Cria guias interativos com diagramas Mermaid, mapeando pontos de entrada, jornada de dados e pegadinhas para acelerar a entrada de novos desenvolvedores em qualquer repositório.
4. **🔬 `dataset-leakage-guard`:** Audita pipelines de Machine Learning para garantir separação absoluta entre treino/validação/teste e evitar vazamento de target e contaminação em scalers.

---

## 🛠️ Como Executar Localmente

### Pré-requisitos
- Python 3.10 ou superior
- Git instalado

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/secsantander23/antigravity.git
   cd antigravity
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # No Windows:
   python -m venv .venv
   .\.venv\Scripts\activate

   # No Linux/macOS:
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as bibliotecas necessárias:**
   ```bash
   pip install pandas matplotlib numpy
   ```

4. **Execute qualquer um dos módulos:**
   ```bash
   # Calibração do termômetro:
   python termometro.py

   # Seleção de fornecedores e geração de gráficos:
   python fornecedores.py

   # Auditoria de qualidade de dados:
   python conferir_dados.py

   # Comparação detalhada entre bases:
   python comparar_bases.py
   ```

---

## 📜 Governança e Regras do Agente (`AGENTS.md`)
O arquivo [AGENTS.md](AGENTS.md) estabelece o contrato de trabalho rigoroso com a IA:
- **Imutabilidade de `dados/`:** Os arquivos originais de entrada jamais são modificados.
- **Centralização em `resultados/`:** Todos os gráficos, relatórios e modelos gerados residem exclusivamente nesta pasta.
- **Rigor Técnico:** Proibição de inventar métricas ou fazer contas "de cabeça"; tudo é calculado e verificado via código.
- **Prevenção de Vazamento:** Isolamento rigoroso entre treino, validação e teste para projetos preditivos.

---
*Desenvolvido no âmbito do Laboratório Prático de Agentes Autônomos e Inteligência Artificial.*

