import sqlite3

def conectar_db():
    return sqlite3.connect("contatos.db")

def criar_tabela():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_contato(nome, email, telefone):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO contatos (nome, email, telefone)
        VALUES (?, ?, ?)
    """, (nome, email, telefone))
    conexao.commit()
    conexao.close()
    print("Contato adicionado com sucesso!")

def listar_contatos():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conexao.close()
    
    if contatos:
        print("Lista de Contatos:")
        for contato in contatos:
            print(f"ID: {contato[0]} - Nome: {contato[1]} - Email: {contato[2]} - Telefone: {contato[3]}")
    else:
        print("Nenhum contato encontrado.")

def atualizar_contato(id_contato, novo_nome, novo_email, novo_telefone):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE contatos
        SET nome = ?, email = ?, telefone = ?
        WHERE id = ?
    """, (novo_nome, novo_email, novo_telefone, id_contato))
    conexao.commit()
    conexao.close()
    print("Contato atualizado com sucesso!")

def excluir_contato(id_contato):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    conexao.commit()
    conexao.close()
    print("Contato excluído com sucesso!")

def menu():
    criar_tabela()
    
    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            email = input("Digite o email do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(nome, email, telefone)
        
        elif opcao == "2":
            listar_contatos()
        
        elif opcao == "3":
            id_contato = int(input("Digite o ID do contato a ser atualizado: "))
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo email: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_contato(id_contato, novo_nome, novo_email, novo_telefone)
        
        elif opcao == "4":
            id_contato = int(input("Digite o ID do contato a ser excluído: "))
            excluir_contato(id_contato)
        
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

#:V