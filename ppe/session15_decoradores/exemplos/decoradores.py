"""
Decoradores (Decorators)

O que são decorators?
  - são funções;
  - envolvem outras funções e aprimoram seus comportamentos;
  - são exemplos de Higher Order Functions;
  - tem uma sitaxe própria usando o @ (Syntact Sugar / Açucar Sintático);
"""

# Decorators como funções (Sintaxe não recomendada, pois não tem Syntact Sugar)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')


# Estamos decorando a função saudação (saude a pessoa, mas de forma educada)
teste = seja_educado(saudacao)
teste()

print()


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)
raiva_educada()

print("--------------------------------------------------")

# Decorators com Syntax Sugar (Forma recomendada)


def seja_educado_mesmo(funcao):  # decorator function
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo()  # decorator
def apresentando():
    print('Meu nome é Pedro')


apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


print()
dormir()

# OBS.: Não confunda decorator por decorator functions
