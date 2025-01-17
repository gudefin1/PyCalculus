def calcular_limite_aproximado(f, x0, passos=8, tolerancia=1e-6):
    """
    Calcula o limite aproximado de uma função f quando x se aproxima de x0.
    
    Parâmetros:
    - f: função para calcular o limite
    - x0: ponto onde queremos calcular o limite (imagine como o eixo das abscissas)
    - passos: número de divisões para aproximação
    - tolerancia: diferença aceitável entre os limites laterais (atualmente 1 milionésimo)
    
    Retorna:
    - float: valor aproximado do limite
    - str: "indefinido" se os limites laterais não convergirem
    """
    # Cria listas de valores se aproximando de x0 pela esquerda e pela direita
    deltas = [1 / (10 ** i) for i in range(1, passos + 1)]  # Valores cada vez menores
    limites_esq = [f(x0 - delta) for delta in deltas]
    limites_dir = [f(x0 + delta) for delta in deltas]

    # Verifica se os últimos valores pela esquerda e direita convergem
    if abs(limites_esq[-1] - limites_dir[-1]) < tolerancia:
        return (limites_esq[-1] + limites_dir[-1]) / 2
    else:
        return "indefinido"


# Exemplo de uso
def f(x):
    return x**2 + 3*x + 8*x  #EDITE AQUI PARA BRINCAR COM SEUS LIMITES!

resultado = calcular_limite_aproximado(f, 1)
print(resultado)  
