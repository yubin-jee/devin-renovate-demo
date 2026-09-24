from app.config import Settings


def test_defaults():
    s = Settings()
    assert s.aws_region == "eu-central-1"
    assert s.table_name == "orders"
