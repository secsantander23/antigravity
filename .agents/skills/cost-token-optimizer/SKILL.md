---
name: cost-token-optimizer
description: Analisa e comprime arquivos de código e contextos enviados a LLMs, gerando esqueletos semânticos via AST e reduzindo em até 70% o consumo de tokens e custos de API.
---

# Cost & Token Optimizer (Otimizador de Tokens e Custos)

## Visão Geral
Em fluxos com agentes de inteligência artificial, alimentar o modelo com arquivos inteiros de 1.000+ linhas desperdiça tokens, estoura a janela de contexto e gera custos desnecessários em APIs. Esta skill transforma arquivos complexos em resumos estruturais (esqueletos de tipos, assinaturas, docstrings e interfaces essenciais) permitindo que o modelo entenda a arquitetura sem ler detalhes de implementação irrelevantes.

---

## Quando Utilizar
- Antes de pedir para a IA ler múltiplos arquivos de uma só vez.
- Ao planejar refatorações em repositórios grandes.
- Para manter o prompt enxuto e evitar que o agente "esqueça" instruções anteriores devido ao excesso de contexto.

---

## Regras de Compressão Semântica

1. **Esqueleto de Classes e Funções:**
   - Preserve: nomes de classes, heranças, assinaturas de métodos (com `type hints`) e a primeira linha da docstring.
   - Substitua o corpo de implementação não relevante por `...` ou `# [implementação interna]`.

2. **Remoção de Ruído:**
   - Elimine comentários redundantes e linhas em branco repetidas.
   - Ignore arquivos de build, logs, lockfiles gigantes (`package-lock.json`, `poetry.lock`) e dados brutos desnecessários.

3. **Mapeamento de Dependências Externas:**
   - Mostre apenas quais módulos externos são importados, sem detalhar o código de terceiros.

---

## Exemplo Prático de Redução

### Antes (Código Bruto - 450 tokens):
```python
class ProcessadorPagamento:
    """Classe responsável pelo processamento financeiro completo de transações."""

    def __init__(self, chave_api: str, ambiente: str = "sandbox"):
        # Inicializa a conexão com o gateway de pagamento externo
        self.chave_api = chave_api
        self.ambiente = ambiente
        self.sessao = self._criar_sessao_http()

    def autorizar(self, cartao: str, valor: float) -> bool:
        # Validação complexa de algoritmo de Luhn com 80 linhas
        # Verificação de antifraude e chamadas de rede com retry
        return True
```

### Depois (Esqueleto Comprimido - 95 tokens | Economia de ~79%):
```python
class ProcessadorPagamento:
    """Processamento financeiro de transações."""
    def __init__(self, chave_api: str, ambiente: str = "sandbox"): ...
    def autorizar(self, cartao: str, valor: float) -> bool: ...
```

---

## Métricas de Sucesso da Otimização
- **Redução de Tokens:** Cálculo da porcentagem economizada.
- **Preservação de Contexto:** Garantia de que classes, tipos e contratos de API permanecem 100% claros para o modelo.

