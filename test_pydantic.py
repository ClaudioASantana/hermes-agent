from pydantic import BaseModel
from typing import Union
try:
    from pydantic.fields import FieldInfo
except ImportError:
    pass

class A(BaseModel):
    x: int

try:
    print("Before:", A.model_validate({"x": "2024-11-05"}))
except Exception as e:
    print("Failed before:", e)

A.model_fields['x'].annotation = Union[int, str]
A.model_rebuild(force=True)

try:
    print("After:", A.model_validate({"x": "2024-11-05"}))
except Exception as e:
    print("Failed after:", e)
