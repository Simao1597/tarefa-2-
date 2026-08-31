<img width="2328" height="6159" alt="Soma dos Números Pares até -1" src="https://github.com/user-attachments/assets/df015114-8075-4d34-87d7-86362cf01cb0" />

Soma dos Números Pares até -1 — Little Man Computer (LMC)


O programa soma apenas os números pares de uma série de números digitados pelo usuário. A entrada continua até que o usuário digite -1, que indica o fim da série.

Para verificar se um número é par, o programa utiliza subtrações repetidas de 2. O número é copiado para temp e o valor 2 é retirado várias vezes.

Se temp chegar exatamente a 0, significa que o número é par e ele é adicionado à variável soma. Se temp ficar negativo, o número é ímpar e não é somado.

 Exemplo

Se o usuário digitar:

5
8
3
10
7
6
-1

Os números pares são:

8, 10 e 6

Então:

8 + 10 + 6 = 24

Resultado:

24
 Fluxograma

O fluxograma representa visualmente o funcionamento do programa: início → entrada de um número → verificar se é -1 → copiar o número para temp → subtrair 2 repetidamente → verificar se o número é par → se for, adicionar à soma → solicitar outro número → repetir → exibir a soma → fim.
| Execução | Números pares | Resultado |
| -------- | ------------- | --------: |
| 1        | 8, 10, 6      |    **24** |
| 2        | 4, 12, 6      |    **22** |
| 3        | 10, 8, 14, 2  |    **34** |

