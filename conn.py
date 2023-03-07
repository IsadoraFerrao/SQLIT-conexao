import sqlite3

conexao = sqlite3.connect('db')
cursor = conexao.cursor()

def criar_tabela():
    nome_table = input('Digite o nome da sua tabela: ')
    tabela_nome = [nome_table]
    cont = 1
    aux = 2
    while cont != aux:
        atributo_nome_01 = input(f'Digite o nome do seu ID: ')
        atributo_nome_02 = input(f'Digite o nome do seu atributo principal: ')
        atributo_nome_03 = input(f'Digite o nome do seu atributo auxiliar: ')
        cont +=1
            
    sql_create_table = f'CREATE TABLE IF NOT EXISTS {nome_table} ({atributo_nome_01} INTEGER NOT NULL, {atributo_nome_02} VARCHAR (100), {atributo_nome_03} VARCHAR(100))'
    cursor.execute(sql_create_table)      
    print('Tabela criada com sucesso!!!\n')
    menu()          
  
def inserir_dados():
    cont = 0
    while cont < 3:
        atributo_01 = input('Insira o valor do atributo {cont}: ')
        dados = [atributo_01]
        cont +=1
    sql_inserir = 'INSERT INTO '

def sair():
    print('\n Obrigado por usar o programa!!\n')
    exit()
    
def menu():  
    cont = 0
    while cont != 1:
        opt = input('Digite a opção desejada: \n1-Criar tabela\n2-Inserir dados\n3-Editar dados\n4-Excluir usuário\n--->')
        if opt == '1':
            criar_tabela()
        elif opt == '2':
            inserir_dados()
        else:
            sair()
        
menu() # inicio do sistema

conexao.commit()
conexao.close