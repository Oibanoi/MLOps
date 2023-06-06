from typing import List

from pydantic import BaseModel


class Request(BaseModel):
    id: str
    columns: List[str]
    rows: List[List[str]]
    