from uuid import UUID, uuid4
from livroModel import Livro

_LIVROS = {
    livro.id: livro
    for livro in (
        Livro(id=uuid4(),titulo="O Diário Perdido de Gravity Falls",autor="Alex Hirsch",ano_publicacao=2016,disponivel=True,),
        Livro(id=uuid4(),titulo="O Guia do Mochileiro das Galáxias",autor="Douglas Adams",ano_publicacao=1979,disponivel=True,),
        Livro(id=uuid4(),titulo="Dom Casmurro",autor="Machado de Assis",ano_publicacao=1899,disponivel=True,),
        Livro(id=uuid4(),titulo="O Pequeno Príncipe",autor="Antoine de Saint-Exupéry",ano_publicacao=1943,disponivel=True,),
        Livro(id=uuid4(),titulo="Diário de um Banana",autor="Jeff Kinney",ano_publicacao=2007,disponivel=True,),
    )
}


def buscarPorId(id: UUID) -> Livro | None:
    livro = _LIVROS.get(id)
    return livro.model_copy() if livro is not None else None