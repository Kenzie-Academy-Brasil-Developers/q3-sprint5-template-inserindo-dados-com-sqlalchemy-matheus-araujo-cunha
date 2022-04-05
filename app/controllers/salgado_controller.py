from flask import request, current_app
from app.models import SalgadoModel
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from werkzeug.exceptions import NotFound


def criar_salgado():
    data = request.get_json()

    salgado = SalgadoModel(**data)

    current_app.db.session.add(salgado)
    current_app.db.session.commit()

    return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 201


def criar_multiplos_salgados():
    data = request.get_json()

    lista_salgados = [SalgadoModel(**salgado) for salgado in data["salgados"]]

    current_app.db.session.add_all(lista_salgados)
    current_app.db.session.commit()

    print(lista_salgados)

    return {
        "salgados": [
            {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}
            for salgado in lista_salgados
        ]
    }, 201


def pegar_salgados():
    # primeira forma
    salgados = SalgadoModel.query.all()

    # segunda forma
    list_salgados = current_app.db.session.query(SalgadoModel).all()
    print("LISTA", list_salgados)

    serializer = [
        {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}
        for salgado in list_salgados
    ]

    return {"salgados": serializer}, 200


def pegar_salgado_por_id(id):

    ## primeira forma
    salgado = SalgadoModel.query.get(id)
    print(salgado)

    ## segunda forma
    new = current_app.db.session.query(SalgadoModel).get(id)
    print("NOVO", new.__dict__)

    return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 200


def primeiro_salgado():
    salgado = SalgadoModel.query.first()

    return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 200


def filtro_salgado_por_nome(nome: str):
    # utilizando filter
    salgados = SalgadoModel.query.filter(SalgadoModel.nome == nome).first()

    # utilizando filter_by
    salgado = SalgadoModel.query.filter_by(nome=nome).first()

    # serializer = [
    #    {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}
    #    for salgado in salgados
    # ]

    return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 200


def um_salgado(preco: float):
    # utilizando o one(), caso não haja o resultado esperado, irá estourar o erro
    # NoResultFound, diferente do one_or_none, que não estoura erro, porém retorna None.

    try:
        salgado = SalgadoModel.query.filter_by(preco=preco).one()
        return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 200
    except (NoResultFound):
        return {"error": "No result found"}, 404
    except MultipleResultsFound:
        return {"error": "Multiples Results"}, 400


def pegar_ou_404(id: int):
    try:
        salgado = SalgadoModel.query.get_or_404(
            id, description="Salgado não encontrado"
        )
    except NotFound as e:
        return {"error": e.description}, 404

    return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 200


def filtrar_ou_404(nome):
    try:
        salgado = SalgadoModel.query.filter_by(nome=nome).first_or_404(
            description="Salgado não encontrado"
        )

    except NotFound as e:
        ...

    return {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}, 200
