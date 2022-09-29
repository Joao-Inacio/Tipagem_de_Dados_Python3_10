# Tipagem simples em variáveis
from typing import TypeVar
from collections.abc import Callable

string: str = 'Um valor'
inteiro: int = 12345
um_float: float = 1.45
booleano: bool = True
um_set: set = {1, 2, 3}
lista: list = []
tupla: tuple = 1, 2, 3
dicionario: dict = {}

# Tipagem de parâmetros em métodos e funções


def soma(x: int, y: int, z: float) -> float:
    return x * y * z


print(soma(1, 2, 3))

# Tipagem em lista
lista_int: list[int] = [1, 2, 3, 4, 5]
lista_str: list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
lista_tuplas: list[tuple] = [(1, 'a'), (2, 'b'), (3, 'c')]
lista_listas_int: list[list[int]] = [[1], [2], [3], [4]]

# Tipagem de dicionários (dict)
um_dist: dict[str, int] = {
    "A": 0,
    "B": 1,
    "C": 2,
}

um_dict_de_lista: dict[str, list[int]] = {
    "A": [1, 3],
    "B": [2, 4],
    "C": [3, 4],
}

#  Tipagem de sets (conjuntos)
um_set_de_inteiros: set[int] = {1, 2, 3}

# Type Alias (variáveis de tipos)
ListInteiros = list[int]
DictListInteiros = dict[str, ListInteiros]

# Type Union (mais de um tipo)
str_e_int: str | int = 1  # Union

# Tipos opcionais (Optional Typing)


def soma1(x: int, y: float | None = None) -> float:
    if isinstance(y, float):
        print(x + y)
    print(x + x)


soma1(1, 1.5)

# Callable


SomaInteiros = Callable[[int, int], int]


def executa(func: SomaInteiros, a: int, b: int) -> int:
    return func(a, b)


def soma(a: int, b: int) -> int:
    return a + b


def soma2(a: float, b: float) -> float:
    return a + b


print(executa(soma2, 1, 2))

# Typevars

T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 3], 1)  # int
list_str = get_item(['a', 'b', 'c'], 1)  # str
