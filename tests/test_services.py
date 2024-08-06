import pytest
from src.services import transactions, investment_bank
import json

def test_investment_bank(invest):
    assert investment_bank("2021-12", transactions, 10) == invest