from flask import Blueprint
from app.controllers import salgado_controller

bp_salgados = Blueprint("bp_salgados", __name__, url_prefix="/salgados")

bp_salgados.post("")(salgado_controller.criar_salgado)
bp_salgados.post("/multiplos")(salgado_controller.criar_multiplos_salgados)
bp_salgados.get("")(salgado_controller.pegar_salgados)
bp_salgados.get("/<int:id>")(salgado_controller.pegar_salgado_por_id)
bp_salgados.get("/primeiro")(salgado_controller.primeiro_salgado)
bp_salgados.get("/<nome>")(salgado_controller.filtro_salgado_por_nome)
bp_salgados.get("/<float:preco>")(salgado_controller.um_salgado)
bp_salgados.get("/404/<int:id>")(salgado_controller.pegar_ou_404)
