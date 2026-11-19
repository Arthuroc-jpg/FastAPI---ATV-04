from uuid import UUID
import livroRepository
from livroModel import Livro


class LivroNaoEncontrado(Exception):
    pass


def consultarLivro(id: UUID) -> Livro:
    livro = livroRepository.buscarPorId(id)
    if livro is None:
        raise LivroNaoEncontrado(f"Livro com id {id} não encontrado")
    return livro