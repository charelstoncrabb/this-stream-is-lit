import pydantic


class DataModel(pydantic.BaseModel):
    my_int: int
    my_float: float
    my_str: str

