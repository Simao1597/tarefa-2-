# Simão Atv 07

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print("Fatorial de 0:", fatorial(0))
print("Fatorial de 5:", fatorial(5))
print("Fatorial de 20:", fatorial(20))


# Em C, tentar calcular o fatorial de 20 em um int comum estoura o limite de memória (overflow) e dá um número errado ou negativo.
# Isso acontece porque o C só guarda números inteiros até mais ou menos 2 bilhões.
# O Python não tem esse limite fixo: ele aumenta o tamanho do número na memória sozinho conforme ele vai crescendo.