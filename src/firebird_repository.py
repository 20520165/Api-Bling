"""Exemplo didático de persistência no Firebird usando parâmetros."""

from __future__ import annotations

import os
from typing import Any

from firebird.driver import connect


def conectar():
    database = os.getenv("FIREBIRD_DATABASE")
    user = os.getenv("FIREBIRD_USER")
    password = os.getenv("FIREBIRD_PASSWORD")

    if not all((database, user, password)):
        raise ValueError(
            "Defina FIREBIRD_DATABASE, FIREBIRD_USER e FIREBIRD_PASSWORD."
        )

    return connect(database, user=user, password=password)


def inserir_pedido_exemplo(
    numero: int,
    cliente: str,
    total: float,
) -> None:
    """Insere um registro em uma tabela de demonstração já criada.

    Schema esperado:
      CREATE TABLE PEDIDOS_DEMO (
        NUMERO INTEGER NOT NULL PRIMARY KEY,
        CLIENTE VARCHAR(120) NOT NULL,
        TOTAL DECIMAL(12, 2) NOT NULL
      )
    """
    sql = """
        INSERT INTO PEDIDOS_DEMO (NUMERO, CLIENTE, TOTAL)
        VALUES (?, ?, ?)
    """

    with conectar() as con:
        with con.cursor() as cur:
            cur.execute(sql, (numero, cliente, total))
        con.commit()
