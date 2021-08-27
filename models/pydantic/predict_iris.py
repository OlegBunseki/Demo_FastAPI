from pydantic import BaseModel

class InputIris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class OutputIris(BaseModel):
    species: str