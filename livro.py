from uuid import UUID
from fastapi import FastAPI, HTTPException
from livroModel import Livro
from livroService import consultarLivro, LivroNaoEncontrado
import livroRepository

app = FastAPI(title="Biblioteca")


@app.get("/livros", response_model=list[Livro])
def getLivros() -> list[Livro]:
    return list(livroRepository._LIVROS.values())


@app.get("/livros/{id}", response_model=Livro)
def getLivro(id: UUID) -> Livro:
    try:
        return consultarLivro(id)
    except LivroNaoEncontrado as erro:
        raise HTTPException(status_code=404, detail="Livro não encontrado") from erro