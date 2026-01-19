# Desafio_Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python
Este é o momento de criar o seu portfólio! O objetivo deste desafio é replicar o projeto prático, explorando os conceitos de Ciência de Dados e Python. Crie seu repositório no GitHub e mostre ao mercado que você sabe construir soluções práticas 😎

## Visão Geral
Esse projeto simula um fluxo completo de **ETL (Extract, Transform, Load)** usando Python, dados mockados e IA generativa para criar mensagens personalizadas de marketing financeiro para clientes.

A API pública da SDW2023 está fora do ar, então o projeto foi ajustado para seguir o fluxo ETL sem depender dela, garantindo o aprendizado das etapas e mantendo o uso de IA.

---

## 🔍 O que esse projeto faz

### 1. Extract  
Como a API não está mais disponível, os dados são mockados diretamente no código.  
Cada cliente tem:
- Dados básicos  
- Conta  
- Cartão  
- Lista de "news" (vazia inicialmente)

### 2. Transform  
Para cada cliente, o projeto usa **OpenAI GPT‑4** para gerar mensagens personalizadas sobre a importância de investir.

Detalhes:
- Máximo de 100 caracteres  
- Tom motivacional e direto  
- Especialista em marketing bancário (prompt)

### 3. Load  
Como o backend real não está disponível, as informações são carregadas em:
- `usuarios_atualizados.json`  
- `usuarios_atualizados.csv`

Ambos são gerados automaticamente ao final da pipeline.

---

## 🧠 Tecnologias Usadas
- Python 3  
- OpenAI API (SDK moderno)  
- Pandas  
- JSON / CSV  
- Logging  

---

## 📂 Estrutura do Projeto
