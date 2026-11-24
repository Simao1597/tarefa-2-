# Simão Atv 05

n = int(input("Digite um número para a contagem: "))

print("Com while:")
i = n
while i >= 0:
    print(i)
    i -= 1


print("Com for:")
for i in range(n, -1, -1):
    print(i)