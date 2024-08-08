from typing import Any

from src.services import investment_bank, transactions


def test_investment_bank(invest: Any) -> str:
    assert investment_bank("2021-12", transactions, 10) == invest
