# 🛡️ DIO Agent — Security & Vulnerability Analysis

Fork of DIO Agent, DIO's AI-powered study mentor, with a focus on information security. This project adds a vulnerability analysis skill, a security knowledge base, and a secure authentication example in Python.

## 🎯 What was added

| Item | Path | Description |
|---|---|---|
| Vulnerability analysis skill | `skills/vulnerability-analysis/` | Teaches the agent to review code for security flaws, in a defensive and educational way |
| Knowledge base | `agent/knowledge/security-basics.md` | Information security fundamentals: core concepts (risk, risk treatment, login example), the CIA triad, security principles, best practices (accounts and passwords, systems, secure development, data, people, detection and response), review questions, and further reading |
| Secure authentication | `agent/app.py` | User registration and login with properly protected passwords |
| Skill registration | `AGENTS.md` | New entry in the skills table, so the agent can trigger it on its own |

## 🔍 Skill: vulnerability-analysis

The agent triggers this skill when the student asks about vulnerabilities, risks, or security flaws, or requests a security code review.

**Principle: learn to think like a defender.** The skill is strictly defensive: it explains the risk conceptually, without writing exploits or helping attack third-party systems.

What it analyzes, in this order:

1. User input that reaches queries, commands, file paths, or HTML without sanitization
2. Authentication and passwords (plain text, weak hashing, no attempt limit)
3. Hardcoded secrets in the code (passwords, keys, tokens)
4. Error handling that exposes sensitive information
5. Non-security bugs, listed separately

Each finding's format: title and location, severity, how the risk works, impact, references (CWE, OWASP Top 10, and MITRE ATT&CK), and fix.

**Help modes:**

- **Diagnosis (default):** lists findings without rewriting the code
- **Fix:** shows the correction with comments explaining each change
- **Learning:** guides the student through a hint ladder (concept → direction → strategy → pseudocode → inline comment), without giving away the full answer

At the end, the agent asks the student to explain, in their own words, why the old code was vulnerable and why the new one isn't.

## 🔐 Secure authentication (`agent/app.py`)

A login example that fixes common security flaws:

- **Salted password hashing:** PBKDF2-HMAC-SHA256 with 100,000 iterations and a random 16-byte salt (`os.urandom`), so identical passwords produce different hashes
- **Parameterized queries:** SQLite receives values separately from the query (`?`), which prevents SQL injection
- **Password never stored in plain text:** the database only stores `salt$hash`, both Base64-encoded
- **Single failure message:** a nonexistent user and a wrong password return the same response, without revealing whether the user exists
- **Connection always closed:** using `try/finally`

**Functions**

| Function | What it does |
|---|---|
| `registar_usuario(user, password)` | Creates the user, storing the password as `salt$hash` |
| `auth_login(user, password)` | Validates the login and returns `"Access granted!"` or `"Access denied!"` |

**Usage example**

The code expects a `banco_de_dados.db` database with a `usuarios` table containing `username` and `password` columns:

```python
import sqlite3
from app import registar_usuario, auth_login

con = sqlite3.connect("banco_de_dados.db")
con.execute("CREATE TABLE IF NOT EXISTS usuarios (username TEXT UNIQUE, password TEXT)")
con.close()

registar_usuario("ana", "strong-password-123")
print(auth_login("ana", "strong-password-123"))  # Access granted!
print(auth_login("ana", "wrong-password"))        # Access denied!
```

Run it from the `agent/` folder.

## 🚀 How to use the agent

1. Install a compatible harness (Google Antigravity, Claude Code, Codex, OpenCode, or Hermes).
2. Clone the project:
   ```bash
   git clone https://github.com/GuilhermeRodr1gues/dio-agent.git
   ```
3. Open the folder containing `AGENTS.md` in the harness.
4. Talk to it naturally. Example prompts that trigger the new skill:
   - "Analyze this code and tell me if it has vulnerabilities."
   - "Is this login secure?"
   - "How do I fix SQL injection in this snippet?"

## 🗂️ Structure (changed parts)

```
dio-agent/
├── AGENTS.md                         + vulnerability-analysis skill registered
├── agent/
│   ├── app.py                        + secure authentication with SQLite
│   └── knowledge/
│       └── security-basics.md        + security fundamentals
└── skills/
    └── vulnerability-analysis/
        ├── README.MD                 + skill goal and flow
        └── SKILL.md                  + full instructions for the agent
```

## 🙏 Credits

Original project created by DIO: [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent).
