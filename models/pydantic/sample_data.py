from pydantic import BaseModel
from typing import Optional, Dict, List
from enum import Enum

class ModelName(str, Enum):
    logreg = "logisitc regression"
    linreg = "linear regression"
    ranfor = "random forrest"


class InputData(BaseModel):
    my_string: str
    my_integer: int
    my_float: float
    my_dict: Dict
    my_list: List
    my_optional_str: Optional[str]


class OutputData(BaseModel):
    my_value: str
    
