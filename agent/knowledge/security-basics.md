# Fundamentos de Segurança da Informação

Base de conhecimento com os conceitos essenciais de segurança: o que se protege, do que se protege, como medir o risco e quais princípios e práticas reduzem esse risco.

## 1. O que é segurança da informação

Segurança da informação é o conjunto de práticas, processos e tecnologias que protegem informações e sistemas contra acesso, uso, divulgação, alteração ou destruição não autorizados. Ela não elimina o risco por completo: o objetivo é **reduzi-lo a um nível aceitável** gastando o esforço onde ele mais importa.

Segurança envolve três dimensões ao mesmo tempo: **pessoas** (hábitos, treinamento), **processos** (regras, resposta a incidentes) e **tecnologia** (criptografia, firewalls, autenticação).

## 2. Conceitos centrais

| Termo | Definição | Exemplo |
|---|---|---|
| **Ativo** | Qualquer coisa de valor que precisa de proteção: dados, sistemas, serviços, pessoas, reputação. | Banco de dados de usuários |
| **Vulnerabilidade** | Fraqueza em um ativo, processo ou controle que pode ser explorada. | Consulta SQL montada com texto do usuário |
| **Ameaça** | Qualquer evento ou agente com potencial de causar dano a um ativo, explorando uma vulnerabilidade. | Um atacante, um malware, um erro humano, uma falha de energia |
| **Exploit** | Técnica ou código que aproveita uma vulnerabilidade específica. | Entrada que burla o login |
| **Risco** | Possibilidade de uma ameaça explorar uma vulnerabilidade e causar impacto a um ativo. | Vazamento de senhas de todos os usuários |
| **Impacto** | Tamanho do dano se o risco se concretizar (financeiro, legal, operacional, de reputação). | Multa, perda de clientes |
| **Controle** | Medida que previne, detecta ou corrige um problema (também chamado de contramedida). | Consultas parametrizadas, backup, MFA |
| **Incidente** | Evento em que a segurança foi de fato comprometida. | Vazamento confirmado de dados |

### Como os conceitos se relacionam

Uma **ameaça** só causa dano se existir uma **vulnerabilidade** para explorar. O **risco** nasce quando as duas coincidem sobre um **ativo** que importa. Os **controles** reduzem a vulnerabilidade, a probabilidade da ameaça ou o impacto.

Uma forma simples de pensar o risco, de modo qualitativo:

```
Risco = Probabilidade x Impacto
```

Um risco com probabilidade alta e impacto alto é prioridade. Um risco com probabilidade baixa e impacto baixo pode ser aceito.

### Tratamento do risco

Depois de avaliar um risco, há quatro respostas comuns:

- **Mitigar:** reduzir com controles (corrigir a falha, adicionar MFA).
- **Evitar:** eliminar a atividade que gera o risco (desligar um serviço desnecessário).
- **Transferir:** repassar parte do impacto (seguro, terceirização contratual).
- **Aceitar:** assumir conscientemente o risco residual, quando o custo de tratá-lo é maior que o benefício.

### Exemplo prático: sistema de login

- **Ativo:** tabela de usuários e senhas.
- **Vulnerabilidade:** SQL injection no formulário de login (CWE-89).
- **Ameaça:** pessoa mal-intencionada que envia entradas manipuladas.
- **Risco:** contornar a autenticação e acessar contas, com impacto alto.
- **Controles:** consultas parametrizadas, hash de senha com salt, limite de tentativas, monitoramento de logs.

## 3. A tríade CIA: confidencialidade, integridade e disponibilidade

A tríade CIA (do inglês *Confidentiality, Integrity, Availability*) é o modelo básico para avaliar o que precisa ser protegido.

### Confidencialidade

Garantir que a informação seja acessada **somente por quem tem autorização**.

- **Ameaças:** vazamento de dados, acesso indevido, espionagem de rede, engenharia social.
- **Controles:** criptografia, controle de acesso, autenticação forte (MFA), classificação da informação.

### Integridade

Garantir que a informação **não seja alterada** de forma indevida ou não detectada, ou seja, que continue correta e completa.

- **Ameaças:** modificação maliciosa de dados, corrupção de arquivos, erros de processamento.
- **Controles:** hashes e checksums, assinatura digital, controle de versão, logs de auditoria, validação de entrada.

### Disponibilidade

Garantir que sistemas e dados **estejam acessíveis quando necessários** para quem tem autorização.

- **Ameaças:** ataques de negação de serviço (DoS/DDoS), falha de hardware, ransomware, queda de energia ou de rede.
- **Controles:** backups testados, redundância, balanceamento de carga, plano de recuperação de desastres, monitoramento.

### Como usar a tríade

Para cada ativo, pergunte: o que acontece se alguém que não deveria **ler** isso (C), **alterar** isso (I) ou **não conseguir usar** isso (D)? A resposta mostra quais controles priorizar. Um prontuário médico pede muita confidencialidade; um sistema de pagamento pede muita integridade e disponibilidade.

### Propriedades relacionadas

- **Autenticidade:** confirmar que a origem da informação ou o usuário é quem diz ser.
- **Não repúdio:** impedir que alguém negue ter realizado uma ação (assinaturas digitais, logs confiáveis).
- **AAA:** autenticação (quem é você), autorização (o que pode fazer) e auditoria ou *accounting* (o que fez).

## 4. Princípios de segurança

Princípios de projeto que valem para qualquer sistema:

- **Menor privilégio:** cada usuário, processo ou serviço recebe só o acesso de que precisa, e só pelo tempo necessário.
- **Defesa em profundidade:** várias camadas de proteção, para que a falha de uma não exponha tudo.
- **Seguro por padrão:** a configuração inicial já deve ser a mais segura; abrir acessos exige uma decisão consciente.
- **Falhar de forma segura:** em caso de erro, o sistema deve negar acesso em vez de liberar.
- **Separação de funções:** tarefas críticas não ficam nas mãos de uma única pessoa ou componente.
- **Mediação completa:** toda tentativa de acesso é verificada, a cada vez, sem atalhos.
- **Simplicidade:** sistemas simples têm menos falhas e são mais fáceis de auditar.
- **Segurança não depende de segredo do projeto:** o sistema deve ser seguro mesmo que o atacante conheça o seu funcionamento; só as chaves e senhas precisam ser secretas (princípio de Kerckhoffs).
- **Confiança zero (*Zero Trust*):** nunca confiar automaticamente, nem na rede interna; verificar sempre identidade e contexto.

## 5. Boas práticas

### Contas e senhas

- Use senhas longas e únicas para cada serviço, guardadas em um gerenciador de senhas.
- Ative a **autenticação multifator (MFA)** sempre que possível.
- Nunca reutilize senhas nem as compartilhe.
- No código, guarde senhas apenas como **hash com salt** (bcrypt, argon2 ou PBKDF2), nunca em texto puro.

### Sistemas e atualizações

- Mantenha sistema operacional, aplicativos e bibliotecas **atualizados**.
- Remova o que não é usado (serviços, contas, portas abertas).
- Mantenha um **inventário** dos ativos, porque o que não se conhece não se protege.

### Desenvolvimento seguro

- **Valide toda entrada** do usuário e trate-a como não confiável.
- Use **consultas parametrizadas** contra SQL injection.
- Mantenha **segredos fora do código** (variáveis de ambiente, cofres de segredos) e fora do repositório.
- Retorne **mensagens de erro genéricas** ao usuário e registre os detalhes só nos logs.
- Revise dependências de terceiros e corrija as vulneráveis.

### Dados

- Use **criptografia em trânsito** (HTTPS/TLS) e **em repouso** quando o dado for sensível.
- Faça **backups** seguindo a regra 3-2-1: três cópias, em duas mídias diferentes, uma delas fora do local. **Teste a restauração**, porque backup que nunca foi restaurado é uma aposta.
- Colete e guarde só os dados necessários (minimização), em respeito à LGPD.

### Pessoas

- Treine contra **phishing** e engenharia social: desconfie de urgência, links inesperados e pedidos de senha.
- Estimule o hábito de **reportar** suspeitas sem medo de punição.

### Detecção e resposta

- Registre **logs** de eventos importantes e monitore-os.
- Tenha um **plano de resposta a incidentes**: quem age, como isola o problema, como comunica e como recupera.
- Faça revisões e testes de segurança periódicos, sempre com autorização.

## 6. Perguntas de revisão

1. Qual a diferença entre ameaça, vulnerabilidade e risco?
2. Dê um exemplo de ataque a cada pilar da tríade CIA e um controle que o reduz.
3. Por que "falhar de forma segura" importa em uma função de login?
4. Como o princípio do menor privilégio reduz o impacto de uma conta invadida?
5. Por que senhas devem ser guardadas como hash com salt e não criptografadas de forma reversível?

## 7. Fontes para aprofundar

- **OWASP Top 10** (owasp.org): principais riscos em aplicações web.
- **CWE** (cwe.mitre.org): catálogo de tipos de falhas de software.
- **MITRE ATT&CK** (attack.mitre.org): técnicas usadas por atacantes.
- **NIST Cybersecurity Framework** e **ISO/IEC 27001**: estruturas de gestão de segurança.
- **LGPD** (Lei nº 13.709/2018): proteção de dados pessoais no Brasil.