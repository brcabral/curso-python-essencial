import random
from typing import Dict, List, Tuple

# Copiar icones dos nípes: https://www.alt-codes.net/suit-cards.php
NAIPES: List[str] = '♠ ♡ ♣ ♢'.split()
CARTAS: List[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Criar um baralho com 52 cartas"""
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerenciar a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar() -> None:
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores: List['str'] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
