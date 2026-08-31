<img width="3040" height="8192" alt="Calcular a média de uma série terminada em -1" src="https://github.com/user-attachments/assets/2f1a32af-050c-4eb7-be69-00cd62966ba3" />


Média de uma Série até -1 — Little Man Computer (LMC)
 Sobre o código

O programa calcula a média dos números digitados pelo usuário. A entrada continua até que o usuário digite -1, que funciona como o valor de parada.

Durante a execução, o programa armazena a soma dos números na variável soma e conta a quantidade de números digitados na variável contador.

Como o LMC tradicional não possui a instrução DIV, a divisão é realizada por meio de subtrações repetidas. O programa subtrai o valor do contador da soma várias vezes até que não seja mais possível continuar. A quantidade de subtrações realizadas representa o resultado inteiro da média.

 Exemplo

Se o usuário digitar:

10 → 20 → 30 → -1

A soma será:

10 + 20 + 30 = 60

A quantidade de números será:

3

Então:

60 ÷ 3 = 20

Resultado:

20
 Fluxograma

O fluxograma representa visualmente o funcionamento do programa: entrada dos números → verificar se é -1 → somar os valores → contar a quantidade de números → repetir até encontrar -1 → realizar a divisão por subtrações repetidas → exibir a média → fim.
| Execução | Números digitados | Soma | Quantidade | Resultado |
| -------- | ----------------- | ---: | ---------: | --------: |
| 1        | 10, 20, 30        |   60 |          3 |    **20** |
| 2        | 5, 15, 10, 20     |   50 |          4 |    **12** |
| 3        | 8, 12, 16, 4      |   40 |          4 |    **10** |
