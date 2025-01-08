import mysql.connector

def conecta_no_banco_de_dados():
    # Conectar ao servidor MySQL
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')

    # Criar o cursor para interagir com o banco de dados
    cursor = cnx.cursor()

    # Verificar se o banco de dados 'aula06' existe
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "aula06";')
    num_results = cursor.fetchone()[0]

    # Fechar a conexão inicial
    cnx.close()

    # Se o banco de dados não existe, criá-lo
    if num_results == 0:
        # Conectar-se novamente ao servidor MySQL para criar o banco de dados
        cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')

        cursor = cnx.cursor()
        cursor.execute('CREATE DATABASE aula06;')
        cnx.commit()

        # Conectar-se ao banco de dados recém-criado
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='aula06'  # Especificar o banco de dados
        )

        cursor = cnx.cursor()

        # Criar a tabela de contatos
        cursor.execute('''
            CREATE TABLE contatos (
                id_contato INT AUTO_INCREMENT PRIMARY KEY, 
                nome VARCHAR(255) NOT NULL, 
                email VARCHAR(255) NOT NULL, 
                mensagem TEXT NOT NULL,
                situacao VARCHAR(50) NOT NULL
            );
        ''')

        # Criar a tabela de usuarios 
        cursor.execute('''
            CREATE TABLE usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                nome VARCHAR(255), 
                email VARCHAR(255), 
                senha VARCHAR(255), 
                perfil VARCHAR(255)
            );
        ''')

        # Criar a tabela de relacionamento entre usuários e contatos
        cursor.execute('''
            CREATE TABLE usuario_contato (
                usuario_id INT NOT NULL, 
                contato_id INT NOT NULL, 
                situacao VARCHAR(255) NOT NULL, 
                PRIMARY KEY (usuario_id, contato_id), 
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE, 
                FOREIGN KEY (contato_id) REFERENCES contatos(id_contato) ON DELETE CASCADE
            );
        ''')

        # Inserir dados iniciais na tabela 'usuarios'
        nome = "teste"
        email = "peres@peres.com"
        senha = "12345"
        sql = "INSERT INTO usuarios(nome, email,senha) VALUES (%s,%s,%s)"
        valores = (nome, email, senha)
        cursor.execute(sql, valores)
        cnx.commit()
     
        # Fechar a conexão
        cnx.close()
        
    try:
        # Conectar ao banco de dados 'aula06' existente
        bd = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='aula06'
        )
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        raise

    return bd