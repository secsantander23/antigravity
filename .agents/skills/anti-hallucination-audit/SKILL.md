---
name: anti-hallucination-audit
description: Audita códigos e scripts gerados por IA antes da execução, verificando se bibliotecas, funções, parâmetros e imports realmente existem no ambiente local para eliminar 100% das alucinações.
---

# Anti-Hallucination Audit (Auditoria Anti-Alucinação)

## Visão Geral
Modelos de linguagem frequentemente "alucinam" métodos que parecem plausíveis, parâmetros inexistentes em bibliotecas populares (como Pandas, Scikit-Learn ou Matplotlib) ou caminhos de importação incorretos. Esta skill atua como uma barreira de segurança estrita antes de rodar qualquer código.

---

## Quando Utilizar
- Sempre que a IA gerar um bloco de código longo ou utilizar bibliotecas externas.
- Quando o usuário reportar erros do tipo `AttributeError: module has no attribute`, `TypeError: unexpected keyword argument` ou `ModuleNotFoundError`.
- Em pipelines críticos onde código não testado não pode falhar em produção.

---

## Fluxo de Auditoria (Workflow)

```
Checklist de Verificação Anti-Alucinação:
- [ ] Etapa 1: Mapear todos os imports e módulos externos
- [ ] Etapa 2: Inspecionar o ambiente local (.venv ou global)
- [ ] Etapa 3: Verificar assinaturas de funções e nomes de parâmetros
- [ ] Etapa 4: Validar caminhos de arquivos e datasets referenciados
- [ ] Etapa 5: Emitir o parecer de liberação ou plano de correção
```

### 1. Mapeamento de Dependências
Examine cada instrução `import` ou `from ... import ...`. Pergunte-se:
- Essa biblioteca está listada no `requirements.txt`, `pyproject.toml` ou instalada no `.venv`?
- O nome da biblioteca é real ou uma fusão fictícia de dois pacotes (ex.: `matchplotly`)?

### 2. Validação de Métodos e Atributos
Para cada chamada de API de biblioteca externa:
- O método pertence à versão da biblioteca instalada no ambiente local?
- O método foi descontinuado (deprecated) em versões recentes? (Ex.: `df.append()` removido no Pandas 2.0).

### 3. Validação de Argumentos e Tipos
- Os argumentos nomeados existem na assinatura oficial?
- Há suposição incorreta de retornos? (Ex.: esperar que uma função retorne uma tupla quando ela retorna um gerador).

---

## Formato do Relatório de Auditoria

Ao auditar um script, a skill emite:

| Componente | Status | Detalhes / Evidência |
|---|---|---|
| **Bibliotecas Importadas** | [OK / ALERTA] | Todos os pacotes existem no `.venv`. |
| **Métodos e Funções** | [OK / ALERTA] | Assinaturas compatíveis com a versão instalada. |
| **Caminhos de Arquivos** | [OK / ALERTA] | Arquivos de entrada existem em disco. |
| **Veredito Final** | **APROVADO / REPROVADO** | Risco de alucinação: 0%. |

