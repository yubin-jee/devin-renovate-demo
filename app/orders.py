from pydantic import BaseModel, field_validator


class Order(BaseModel):
    id: str
    quantity: int
    region: str = "eu-central-1"

    @field_validator("quantity")
    @classmethod
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError("quantity must be positive")
        return v

    def to_payload(self) -> dict:
        return self.model_dump()


def parse_order(raw: str) -> Order:
    return Order.model_validate_json(raw)
