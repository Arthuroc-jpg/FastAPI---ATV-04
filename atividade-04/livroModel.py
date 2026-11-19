from uuid import UUID
from pydantic import BaseModel, Field


class Livro(BaseModel):
    id: UUID
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    ano_publicacao: int = Field(ge=0)
    disponivel: bool