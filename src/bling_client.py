"""Cliente HTTP mínimo para uma conta de teste do Bling.

Este módulo não implementa o fluxo OAuth completo. O token deve ser obtido
e renovado conforme a documentação oficial e fornecido por variável de ambiente.
"""

from __future__ import annotations

import os
from typing import Any

import requests


class BlingAPIError(RuntimeError):
    """Erro retornado pela API ou pela camada HTTP do Bling."""


class BlingClient:
    BASE_URL = "https://api.bling.com.br/Api/v3"

    def __init__(self, access_token: str | None = None, timeout: int = 30) -> None:
        token = access_token or os.getenv("BLING_ACCESS_TOKEN")
        if not token:
            raise ValueError("Defina BLING_ACCESS_TOKEN no ambiente.")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        })

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        path = endpoint.lstrip("/")
        url = f"{self.BASE_URL}/{path}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise BlingAPIError(f"Falha na chamada ao Bling: {exc}") from exc

        try:
            payload = response.json()
        except ValueError as exc:
            raise BlingAPIError("A API retornou uma resposta que não é JSON válido.") from exc

        if not isinstance(payload, dict):
            raise BlingAPIError("Formato inesperado na resposta da API.")
        return payload

    def listar_pedidos(self, *, pagina: int = 1, limite: int = 100) -> dict[str, Any]:
        if pagina < 1 or not 1 <= limite <= 100:
            raise ValueError("Use pagina >= 1 e limite entre 1 e 100.")
        return self.get("pedidos/vendas", {"pagina": pagina, "limite": limite})


if __name__ == "__main__":
    client = BlingClient()
    print(client.listar_pedidos())
