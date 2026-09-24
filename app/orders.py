from pydantic import BaseModel, validator


class Order(BaseModel):
    id: str
    quantity: int
    region: str = "eu-central-1"

    @validator("quantity")
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError("quantity must be positive")
        return v

    def to_payload(self) -> dict:
        return self.dict()


def parse_order(raw: str) -> Order:
    return Order.parse_raw(raw)
