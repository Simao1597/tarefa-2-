<img width="3281" height="6015" alt="Verificar se um número digitado é múltiplo de outro" src="https://github.com/user-attachments/assets/2b1cfaf3-89c9-4923-9b1a-3726e4070c14" />


Verificar se um número é múltiplo de outro — Little Man Computer (LMC)


O programa verifica se um número é múltiplo de outro. Para isso, utiliza subtrações repetidas, já que o LMC tradicional não possui uma instrução pronta para verificar múltiplos.

O primeiro número é armazenado em num e o segundo em divisor. O programa subtrai o divisor do número várias vezes.

 Exemplo

Se o usuário digitar:

12
3

O programa realiza:

12 - 3 = 9
9 - 3 = 6
6 - 3 = 3
3 - 3 = 0

Como o resultado chegou exatamente a 0, significa que 12 é múltiplo de 3.

 Fluxograma

O fluxograma representa visualmente o funcionamento do programa: entrada do número → entrada do divisor → subtrair o divisor → verificar o resultado → se chegar a 0, é múltiplo → se ficar negativo, não é múltiplo → fim.
| Execução | Número | Divisor |              Resultado |
| -------- | -----: | ------: | ---------------------: |
| 1        |     12 |       3 |     **1 — É múltiplo** |
| 2        |     14 |       3 | **0 — Não é múltiplo** |
| 3        |     25 |       5 |     **1 — É múltiplo** |

