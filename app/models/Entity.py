from pydantic import BaseModel


class File_len(BaseModel):
    funcName: str
    len: int