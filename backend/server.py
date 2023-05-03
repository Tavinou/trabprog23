from flask import Flask, jsonify, request
from flask_cors import CORS
from classe import *


with app.app_context():

    @app.route("/")
    def ola():
        return "backend fununciando"

    @app.route("/incluir_aluno", methods=['POST'])
    def incluir():

        dados = request.get_json()
        try:
            nova = Pessoa(**dados)

            db.session.add(nova)
            db.session.commit()

            return jsonify({"resultado": "ok"})
        except Exception as e:

            return jsonify({"resultado": "erro", "detalhes": str(e)})

    @app.route("/listar_alunos")
    def listar():
       
        dados = db.session.query(Pessoa).all()
    
        
        lista_jsons = [x.json() for x in dados]

        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_jsons})
        return jsonify(meujson)
        

    app.run(debug=True)
