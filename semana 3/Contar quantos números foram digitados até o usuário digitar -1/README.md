<img width="1755" height="5532" alt="Contar quantos números foram digitados até o usuário digitar -1" src="https://github.com/user-attachments/assets/7614a410-74d3-4e67-a6b6-284f51f6808f" />






Contador de Números até -1 — Little Man Computer (LMC)

O programa conta quantos números foram digitados pelo usuário. A entrada continua até que o usuário digite -1, que funciona como o valor de parada.

A cada número digitado, o programa aumenta o valor da variável contador em 1. Quando -1 é informado, a contagem é encerrada e o programa exibe o total de números digitados.

Exemplo

Se o usuário digitar:

5 → 8 → 20 → 3 → -1

O resultado será:

4

O -1 não é contado, pois serve apenas para indicar o final da entrada.

Fluxograma

O fluxograma representa visualmente o funcionamento do programa: início → entrada de um número → verificar se é -1 → se não for, aumentar o contador → solicitar outro número → repetir → se for -1, exibir o contador → fim.

| Teste | Números digitados   | Resultado |
| ----- | ------------------- | --------: |
| 1     | 5, 8, 20, 3         |     **4** |
| 2     | 10, 15, 7, 2, 9     |     **5** |
| 3     | 4, 12, 6, 18, 3, 11 |     **6** |
