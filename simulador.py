# ==============================================================================
# PROJETO: SIMULADOR DE AGENTE INTELIGENTE E ESTRUTURAÇÃO DE API
# DISCIPLINA: IA E PROMPT / FUNDAMENTOS DE AGENTES
# NOTA: Este código simula o empacotamento de chamadas de API e Guardrails 
#       sem necessitar de uma API Key ativa ou execução paga.
# ==============================================================================

import os

def exibir_cabecalho(titulo):
    """Função utilitária para organizar as etapas no console."""
    print("\n" + "="*60)
    print(f"  {titulo.upper()}")
    print("="*60)

# ------------------------------------------------------------------------------
# ETAPA 1: DEFINIÇÃO E MODELAGEM DO AGENTE INTELIGENTE
# ------------------------------------------------------------------------------
exibir_cabecalho("Etapa 1: Modelagem do Agente Inteligente")

print("Um Agente Inteligente é composto por: Ambiente, Objetivo e Ações.\n")

# Coleta dos pilares do agente
ambiente = input("1. Defina o AMBIENTE (Ex: Biblioteca da escola, Portaria): ")
objetivo = input("2. Defina o OBJETIVO (Ex: Tirar dúvidas sobre regras, Otimizar acesso): ")
acoes = input("3. Defina as AÇÕES (Ex: Responder dúvidas, Emitir alertas): ")

print("\n--> Mapeamento do Agente Concluído!")
print(f"    - Ambiente: {ambiente}")
print(f"    - Objetivo: {objetivo}")
print(f"    - Ações:    {acoes}")

# ------------------------------------------------------------------------------
# ETAPA 2: CONFIGURAÇÃO DE GUARDRAILS E SYSTEM PROMPT
# ------------------------------------------------------------------------------
exibir_cabecalho("Etapa 2: Definição de Guardrails (System Prompt)")

print("Configurando as regras mestre que o modelo de IA deverá respeitar.")
persona = input("Defina a PERSONA do agente (Ex: Tutor educacional, Fiscal formal): ")
regra_estrita = input("Defina a REGRA DE ESCÓPO (Ex: Responda apenas sobre o PDF do estatuto): ")

# Construção da instrução mestre (System Prompt)
system_prompt = f"""[SYSTEM PROMPT / INSTRUÇÃO MESTRE]
Você é um assistente virtual atuando como: {persona}.
SUAS REGRAS E GUARDRAILS:
1. {regra_estrita}
2. Se o usuário fizer uma pergunta fora deste tema, responda estritamente: 
   'Sinto muito, meu código de ética me permite falar apenas sobre o escopo definido.'
3. Mantenha um tom profissional, direto e formal.
"""

print("\n--> System Prompt gerado com sucesso!")

# ------------------------------------------------------------------------------
# ETAPA 3: SIMULAÇÃO DE ENTRADA DO USUÁRIO E MULTIMODALIDADE (F-STRING)
# ------------------------------------------------------------------------------
exibir_cabecalho("Etapa 3: Interação do Usuário e Preparação do Pacote")

pergunta_usuario = input("Digite uma pergunta para simular a dúvida do usuário: ")
anexo_simulado = input("Nome de um arquivo anexo para contexto (Ex: regras.pdf ou foto.png) [Opcional]: ")

# Montagem do pacote de dados usando f-strings (como seria enviado à API)
if anexo_simulado.strip():
    pacote_api = f"{system_prompt}\n[CONTEXTO ARQUIVO]: {anexo_simulado}\n\n[PERGUNTA DO USUÁRIO]: {pergunta_usuario}"
else:
    pacote_api = f"{system_prompt}\n\n[PERGUNTA DO USUÁRIO]: {pergunta_usuario}"

# ------------------------------------------------------------------------------
# ETAPA 4: EXIBIÇÃO DO PACOTE DE DADOS ENVIADO À API
# ------------------------------------------------------------------------------
exibir_cabecalho("Etapa 4: Inspeção do Envio para a API (Sem API Key)")

print("Abaixo está o payload exato que seria enviado para o servidor do Gemini via SDK:\n")
print(pacote_api)

print("\n" + "-"*60)
print("[AVISO DE EXECUÇÃO SIMULADA]:")
print("Como os estudantes não possuem uma GOOGLE_API_KEY ativa cadastrada nos")
print("Secrets do Colab, o código não realiza a chamada externa via 'client.models.generate_content()'.")
print("No entanto, o empacotamento do prompt e as restrições foram montados corretamente!")
print("-"*60)

# ------------------------------------------------------------------------------
# ETAPA 5: GERAÇÃO DO ARQUIVO README.MD PARA O GITHUB
# ------------------------------------------------------------------------------
exibir_cabecalho("Etapa 5: Documentação Técnica (README.md)")

readme_conteudo = f"""# Projeto: Agente Inteligente - {persona}

## 📌 Descrição
Este projeto é um Agente Inteligente projetado para atuar no seguinte ambiente:
* **Ambiente:** {ambiente}
* **Objetivo:** {objetivo}
* **Ações:** {acoes}

## 🛡️ Guardrails e Segurança
O sistema conta com restrições rígidas no *System Prompt* para evitar alucinações:
> "{regra_estrita}"

## ⚠️ Requisitos para Produção
Para rodar este script em um ambiente real com respostas geradas por IA:
1. Crie uma conta no **Google AI Studio** e gere uma chave de API (`API Key`).
2. No **Google Colab**, acesse o menu lateral **Secrets** (ícone de chave).
3. Adicione um novo segredo:
   * **Name:** `GOOGLE_API_KEY`
   * **Value:** *[Sua chave de API]*
   * Ative a opção **Notebook access**.
4. Instale a biblioteca oficial executando: `pip install google-genai`
"""

# Salva a documentação automaticamente em um arquivo local
nome_readme = "README.md"
with open(nome_readme, "w", encoding="utf-8") as f:
    f.write(readme_conteudo)

print(f"O arquivo '{nome_readme}' foi gerado com sucesso no diretório local!")
print("Os estudantes podem copiar o conteúdo desse arquivo e publicar em seus repositórios do GitHub.\n")
print("="*60)
print("  FIM DA DEMONSTRAÇÃO ")
print("="*60)
