# configurar o alembic 

# instalar a biblioteca 
# pip install sqlalchemy
# pip install alembic

# no terminal inicie o almebic 
# python -m init alembic 


# configurando a conexão com o db
# -------------------------------------------------


# Abra o arquivo alembique.init 
# o procure a linhas com essa informação:
# sqlalchemy.url = driver://user:pass@localhost/dbname
# altere para:
# sqlalchemy.url = sqlite:///escola.db



#  conectando o alembic ao sqlalchemy

# ------------------------------------------

# abra o arquivo 
# alembic/env.py 


# importe a Base no arquivo env,py
# from models import Base 
# Encontre a linha com:
# target_metadata = None 
# e altere para:
# target_metadata = Base.metadata 