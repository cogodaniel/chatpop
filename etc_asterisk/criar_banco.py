import pymysql
from pymysql.err import OperationalError, ProgrammingError

# Configurações do MySQL
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ch@tp0p#11',  # <- Substitua pela sua senha real
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

DB_NAME = 'chatpop'

# Dicionário com as tabelas
TABLES = {}

TABLES['chatpop_sistema'] = (
    """
    CREATE TABLE IF NOT EXISTS chatpop_sistema (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)

TABLES['chatpop_usuarios'] = (
    """
    CREATE TABLE IF NOT EXISTS chatpop_usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        sala VARCHAR(10),
        mudo BOOLEAN DEFAULT 0,
        mudo_superisor BOOLEAN DEFAULT 0
    )
    """
)

TABLES['bloqueio'] = (
    """
    CREATE TABLE IF NOT EXISTS bloqueio (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)

TABLES['mudo_usuario'] = (
    """
    CREATE TABLE IF NOT EXISTS mudo_usuario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)

TABLES['mudo_supervisor'] = (
    """
    CREATE TABLE IF NOT EXISTS mudo_supervisor (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)

TABLES['sala_geral'] = (
    """
    CREATE TABLE IF NOT EXISTS sala_geral (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        num_sala VARCHAR(10),
        canal VARCHAR(50),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)


TABLES['saudacao'] = (
    """
    CREATE TABLE IF NOT EXISTS saudacao (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero VARCHAR(50),
        pin VARCHAR(10),
        saudacao VARCHAR(50)
    )
    """
)

TABLES['torpedo'] = (
    """
    CREATE TABLE IF NOT EXISTS torpedo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero_origem VARCHAR(50),
        pin_origem VARCHAR(10),
        numero_destino VARCHAR(50),
        pin_destino VARCHAR(10),
        caminho_torpedo VARCHAR(255),
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)



try:
    # Conecta sem banco para criar o banco inicialmente
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Banco de dados '{DB_NAME}' verificado ou criado.")
    cursor.close()
    conn.close()

    # Conecta ao banco recém-criado
    config_with_db = config.copy()
    config_with_db['database'] = DB_NAME

    conn = pymysql.connect(**config_with_db)
    cursor = conn.cursor()

    for table_name, ddl in TABLES.items():
        try:
            cursor.execute(ddl)
            print(f"Tabela '{table_name}' criada ou já existente.")
        except ProgrammingError as err:
            print(f"Erro ao criar tabela {table_name}: {err}")

    cursor.close()
    conn.close()
    print("✅ Banco e tabelas prontos.")

except OperationalError as err:
    print(f"Erro de conexão: {err}")

