import pydantic


class MyDataModel(pydantic.BaseModel):
    my_int: int
    my_float: float
    my_str: str

