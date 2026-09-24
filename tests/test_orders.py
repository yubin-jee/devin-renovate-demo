import pytest
from app.orders import Order, parse_order


def test_parse_and_serialize():
    o = parse_order('{"id": "o-1", "quantity": 3}')
    assert o.to_payload() == {"id": "o-1", "quantity": 3, "region": "eu-central-1"}


def test_validator_rejects_zero():
    with pytest.raises(Exception):
        Order(id="o-2", quantity=0)
