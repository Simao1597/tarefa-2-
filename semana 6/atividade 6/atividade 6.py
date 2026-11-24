# Simão Atv 06

numeros = []
for i in range(5):
    val = float(input(f"Digite o {i+1}º número: "))
    numeros.append(val)

maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print("Maior (usando o loop):", maior)