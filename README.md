# 🤖 Automação Web com Browser-Use

Este projeto é um experimento de criação de um agente autônomo capaz de controlar um navegador web para realizar pesquisas e extrair informações usando a biblioteca `browser-use`.

> ⚠️ **AVISO CRÍTICO DE COMPATIBILIDADE (LEIA ANTES DE RODAR)** ⚠️
> 
> **Este projeto NÃO funciona com os modelos do Google (Gemini).** > 
> A biblioteca `browser-use` foi arquitetada de forma estrita para consumir a funcionalidade de *Structured Outputs* (Saídas Estruturadas em JSON) da **OpenAI** e da **Anthropic**. 
> 
> Para que o agente consiga operar o navegador sem falhar, é **OBRIGATÓRIO** utilizar:
> * **OpenAI:** `gpt-4o` ou `gpt-4o-mini`
> * **Anthropic:** `claude-3-5-sonnet`

## 🐛 O Problema com o Gemini (Erro `items`)
Tentativas de utilizar a API do Google (via `langchain-google-genai` com modelos como `gemini-2.5-pro` ou `gemini-2.0-flash`) resultarão no erro crônico:
`Result failed X/6 times: items`

**Por que isso acontece?**
A biblioteca exige que a Inteligência Artificial leia o código HTML da página e responda **exclusivamente** com um objeto JSON perfeito contendo uma lista de ações chamada `items`. Atualmente, a integração do Gemini se perde na formatação complexa exigida pelo prompt interno da biblioteca, retornando texto puro ou Markdown em vez do JSON estrito. Quando o *parser* da biblioteca não encontra a chave `items`, o agente entra em loop de falha e aborta a operação.

---

## 🛠️ Como rodar o projeto corretamente

Se você deseja ver o agente funcionando, precisará configurar uma chave de API compatível.

### 1. Pré-requisitos
Certifique-se de ter o gerenciador de pacotes `uv` instalado e instale as dependências:

```bash
uv add browser-use python-dotenv langchain-openai
