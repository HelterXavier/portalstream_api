from pydantic import BaseModel, Field
from typing import Optional


class Dto(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    description: Optional[str] = Field(None)
    age: int = Field(..., ge=0)


class UpdateDoc(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    description: Optional[str] = None
    age: Optional[str] = Field(None, ge=0)
