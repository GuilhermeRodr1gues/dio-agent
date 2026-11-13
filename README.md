# 🛡️ DIO Agent — Segurança e Análise de Vulnerabilidades

Fork do [DIO Agent](https://github.com/digitalinnovationone/dio-agent), o mentor de estudos com IA da [DIO](https://dio.me), com foco em **segurança da informação**. Este projeto adiciona ao agente uma skill de análise de vulnerabilidades, uma base de conhecimento de segurança e um exemplo de autenticação segura em Python.

## 🎯 O que foi adicionado

| Item | Caminho | Descrição |
| --- | --- | --- |
| Skill de análise de vulnerabilidades | `skills/vulnerability-analysis/` | Ensina o agente a revisar código em busca de falhas de segurança, de forma defensiva e didática |
| Base de conhecimento | `agent/knowledge/security-basics.md` | Fundamentos de segurança da informação: conceitos centrais (risco, tratamento do risco, exemplo de login), tríade CIA, princípios de segurança, boas práticas (contas e senhas, sistemas, desenvolvimento seguro, dados, pessoas, detecção e resposta), perguntas de revisão e fontes para aprofundar |
| Autenticação segura | `agent/app.py` | Cadastro e login de usuários com senha protegida |
| Registro da skill | `AGENTS.md` | Nova linha na tabela de skills, para o agente acioná-la sozinho |

## 🔍 Skill: vulnerability-analysis

O agente aciona esta skill quando o estudante pergunta sobre vulnerabilidades, riscos ou falhas de segurança, ou pede um *code review* de segurança.

**Princípio:** aprender a pensar como defensor. A skill é estritamente defensiva: explica o risco de forma conceitual, sem escrever exploits nem ajudar a atacar sistemas de terceiros.

**O que ela analisa, nesta ordem:**

1. Entrada do usuário que chega a consultas, comandos, caminhos de arquivo ou HTML sem tratamento
2. Autenticação e senhas (texto puro, hash fraco, falta de limite de tentativas)
3. Segredos fixos no código (senhas, chaves, tokens)
4. Tratamento de erros que expõe informações sensíveis
5. Bugs que não são de segurança, listados à parte

**Formato de cada achado:** título e local, severidade, como o risco funciona, impacto, referências (CWE, OWASP Top 10 e MITRE ATT&CK) e correção.

**Modos de ajuda:**

- **Diagnóstico (padrão):** lista os achados sem reescrever o código
- **Correção:** mostra a correção com comentários explicando cada mudança
- **Aprendizado:** guia o estudante com uma escada de dicas (conceito → direção → estratégia → pseudocódigo → comentário no código), sem entregar a resposta pronta

Ao final, o agente pede que o estudante explique com as próprias palavras por que o código antigo era vulnerável e por que o novo não é.

## 🔐 Autenticação segura (`agent/app.py`)

Exemplo de login que corrige falhas comuns de segurança:

- **Hash de senha com sal:** PBKDF2-HMAC-SHA256 com 100.000 iterações e sal aleatório de 16 bytes (`os.urandom`), então senhas iguais geram hashes diferentes
- **Consultas parametrizadas:** o SQLite recebe os valores separados da consulta (`?`), o que previne SQL injection
- **Senha nunca em texto puro:** o banco guarda apenas `sal$hash`, ambos em Base64
- **Mensagem única de falha:** usuário inexistente e senha errada retornam a mesma resposta, sem revelar se o usuário existe
- **Conexão sempre fechada:** uso de `try/finally`

### Funções

| Função | O que faz |
| --- | --- |
| `registar_usuario(user, password)` | Cria o usuário, salvando a senha como `sal$hash` |
| `auth_login(user, password)` | Valida o login e retorna `"Acess done!"` ou `"Acess denied!"` |

### Exemplo de uso

O código espera um banco `banco_de_dados.db` com uma tabela `usuarios` que tenha as colunas `username` e `password`:

```python
import sqlite3
from app import registar_usuario, auth_login

con = sqlite3.connect("banco_de_dados.db")
con.execute("CREATE TABLE IF NOT EXISTS usuarios (username TEXT UNIQUE, password TEXT)")
con.close()

registar_usuario("ana", "senha-forte-123")
print(auth_login("ana", "senha-forte-123"))  # Acess done!
print(auth_login("ana", "senha-errada"))     # Acess denied!
```

Execute a partir da pasta `agent/`.

## 🚀 Como usar o agente

1. Instale um harness compatível (Google Antigravity, Claude Code, Codex, OpenCode ou Hermes).
2. Clone o projeto:

   ```bash
   git clone https://github.com/GuilhermeRodr1gues/dio-agent.git
   ```

3. Abra no harness a pasta que contém o `AGENTS.md`.
4. Converse naturalmente. Exemplos de pedidos que acionam a nova skill:
   - "Analise este código e me diga se tem vulnerabilidades."
   - "Esse login está seguro?"
   - "Como corrijo SQL injection neste trecho?"

## 🗂️ Estrutura (partes alteradas)

```
dio-agent/
├── AGENTS.md                         + skill vulnerability-analysis registrada
├── agent/
│   ├── app.py                        + autenticação segura com SQLite
│   └── knowledge/
│       └── security-basics.md        + fundamentos de segurança
└── skills/
    └── vulnerability-analysis/
        ├── README.MD                 + objetivo e fluxo da skill
        └── SKILL.md                  + instruções completas para o agente
```

## 🙏 Créditos

Projeto original criado pela [DIO](https://dio.me): [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent).