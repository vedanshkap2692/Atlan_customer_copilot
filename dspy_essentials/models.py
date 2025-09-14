from pydantic import BaseModel
from typing import List


class classification(BaseModel):
    topics: List[str]
    sentiment: str
    priority: str
    