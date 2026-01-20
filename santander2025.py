import pandas as pd
import json
import logging
from openai import OpenAI

# ============================================================================
# CONFIGURAÇÃO DE LOGGING
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# CONFIGURAÇÃO INICIAL
# ============================================================================
openai_api_key = 'sua_api_key_aqui'  # Substitua pela sua chave
client = OpenAI(api_key=openai_api_key)

# ============================================================================
# EXTRACT - Dados mockados (alternativa 1, já que a API tá fora)
# ============================================================================
def extract_users():
    """
    Simula a extração de dados de usuários.
    Em produção, isso viria de uma API ou CSV.
    """
    users = [
        {
            'id': 1,
            'name': 'João Silva',
            'account': {
                'number': '00001-1',
                'agency': '0001',
                'balance': 1500.0,
                'limit': 5000.0
            },
            'card': {
                'number': '**** **** **** 1234',
                'limit': 3000.0
            },
            'news': []
        },
        {
            'id': 2,
            'name': 'Maria Santos',
            'account': {
                'number': '00002-2',
                'agency': '0001',
                'balance': 3200.0,
                'limit': 8000.0
            },
            'card': {
                'number': '**** **** **** 5678',
                'limit': 5000.0
            },
            'news': []
        },
        {
            'id': 3,
            'name': 'Pedro Costa',
            'account': {
                'number': '00003-3',
                'agency': '0001',
                'balance': 890.0,
                'limit': 3000.0
            },
            'card': {
                'number': '**** **** **** 9012',
                'limit': 2000.0
            },
            'news': []
        }
    ]

    logger.info(f"✓ {len(users)} usuários extraídos com sucesso")
    return users

# ============================================================================
# TRANSFORM - Gera mensagens com IA
# ============================================================================
def generate_ai_news(user):
    """
    Usa GPT-4 pra gerar uma mensagem personalizada sobre investimentos.
    """
    try:
        logger.info(f"Gerando mensagem para {user['name']}...")

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em marketing bancário. Crie mensagens motivacionais e personalizadas sobre investimentos."
                },
                {
                    "role": "user",
                    "content": f"Crie uma mensagem personalizada para {user['name']} sobre a importância dos investimentos. Máximo 100 caracteres. Seja direto e motivador."
                }
            ],
            max_tokens=50,
            temperature=0.7
        )

        message = completion.choices[0].message.content.strip('\"')
        logger.info(f"✓ Mensagem gerada para {user['name']}")
        return message

    except Exception as e:
        logger.error(f"✗ Erro ao gerar mensagem para {user['name']}: {e}")
        # Fallback: mensagem padrão
        return f"{user['name']}, invista no seu futuro! Comece hoje mesmo."

def transform_users(users):
    """
    Transforma os dados dos usuários adicionando mensagens de IA.
    """
    logger.info("Iniciando transformação dos dados...")

    for user in users:
        news_message = generate_ai_news(user)

        user['news'].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news_message
        })

    logger.info(f"✓ Transformação concluída para {len(users)} usuários")
    return users

# ============================================================================
# LOAD - Salva os dados localmente (já que a API tá fora)
# ============================================================================
def load_users_to_file(users, filename='usuarios_atualizados.json'):
    """
    Salva os dados dos usuários em um arquivo JSON.
    Em produção, isso seria um PUT na API.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

        logger.info(f"✓ Dados salvos em '{filename}'")
        return True

    except Exception as e:
        logger.error(f"✗ Erro ao salvar dados: {e}")
        return False

def load_users_to_csv(users, filename='usuarios_atualizados.csv'):
    """
    Alternativa: salva em CSV também.
    """
    try:
        # Prepara os dados pra CSV
        data_for_csv = []
        for user in users:
            news_text = user['news'][0]['description'] if user['news'] else 'Sem mensagem'
            data_for_csv.append({
                'ID': user['id'],
                'Nome': user['name'],
                'Saldo': user['account']['balance'],
                'Limite': user['account']['limit'],
                'Mensagem': news_text
            })

        df = pd.DataFrame(data_for_csv)
        df.to_csv(filename, index=False, encoding='utf-8')

        logger.info(f"✓ Dados salvos em '{filename}'")
        return True

    except Exception as e:
        logger.error(f"✗ Erro ao salvar CSV: {e}")
        return False

# ============================================================================
# PIPELINE ETL COMPLETO
# ============================================================================
def run_etl_pipeline():
    """
    Executa o pipeline ETL completo.
    """
    logger.info("=" * 60)
    logger.info("INICIANDO PIPELINE ETL")
    logger.info("=" * 60)

    try:
        # Extract
        logger.info("\n[1/3] EXTRACT - Extraindo dados...")
        users = extract_users()

        # Transform
        logger.info("\n[2/3] TRANSFORM - Transformando dados com IA...")
        users = transform_users(users)

        # Load
        logger.info("\n[3/3] LOAD - Carregando dados...")
        load_users_to_file(users)
        load_users_to_csv(users)

        logger.info("\n" + "=" * 60)
        logger.info("✓ PIPELINE CONCLUÍDO COM SUCESSO!")
        logger.info("=" * 60)

        # Exibe resumo
        print("\n📊 RESUMO DOS DADOS PROCESSADOS:\n")
        for user in users:
            print(f"👤 {user['name']}")
            print(f"   Saldo: R$ {user['account']['balance']:.2f}")
            print(f"   Mensagem: {user['news'][0]['description']}")
            print()

        return users

    except Exception as e:
        logger.error(f"✗ Erro no pipeline: {e}")
        return None

# ============================================================================
# EXECUÇÃO
# ============================================================================
if __name__ == "__main__":
    users = run_etl_pipeline()