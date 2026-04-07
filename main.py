from models import Session,  Curso, Aluno 


# Criar as funções do Crud  
# Cadastrar  curso. 

# Cadastrar um aluno no curso. 

def cadastrar_curso():
    with Session() as session:
        try:
            nome_curso = input("Digite o nome do curso:").capitalize()
            carga_horaria = int(input("Digite a carga horaria desse curso:"))
            descrição = input("Digite a descrição do curso:").capitalize()
            #criar o Objeto 
            curso = Curso(nome=nome_curso , carga_horaria=carga_horaria, descrição=descrição)
            #adicionar no banco 
            session.add(curso)
            session.commit()
            
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")
cadastrar_curso()

