from geral.config import *

from classe import *



with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    
    db.create_all()

    print("Banco de dados e tabelas criadas")
