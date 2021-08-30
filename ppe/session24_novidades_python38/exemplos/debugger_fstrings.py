"""
Debugando com o fstrings
"""


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.2345, 6.7890)
print(f'O resultado é {resultado:.2f}')

print(f'O resultado é {multiplicar(9, 4)}')

print("--------------------------------------------------")

geek: str = 'Geek University'
print(f'geek="{geek}"')
print(f'{geek}=')
print(f'{geek.upper()[::-1] = }')
