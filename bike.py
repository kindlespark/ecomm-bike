from pydantic import BaseModel


class Bike(BaseModel):
    id: int
    brand: str
    Engine_capacity: str
    price: str
