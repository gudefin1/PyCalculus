def derivada(funcao, x, h=1e-5):
    """
    Calcula a derivada numérica de uma função em um ponto x.
    
    :parametro funcao: Função a ser derivada (ex.: lambda x: x**2)
    :parametro x: Ponto onde a derivada será calculada
    :parametro h: Pequeno incremento (default: 1e-5)
    :return: Aproximação da derivada em x
    """
    return (funcao(x + h) - funcao(x)) / h


# Definindo a função f(x) 
funcao = lambda x: x**2 + 3*x**3

# Calculando a derivada de f(x)  no ponto x = 2
x_ponto = 1
resultado = derivada(funcao, x_ponto)
print(f"A derivada de f(x) = x^2 no ponto x = {x_ponto} é aproximadamente {resultado}")
