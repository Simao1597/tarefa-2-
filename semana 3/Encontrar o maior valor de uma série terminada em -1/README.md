<img width="2120" height="8191" alt="Encontrar o maior valor de uma série terminada em -1" src="https://github.com/user-attachments/assets/18f9e8d5-4169-43a9-b0e0-1dc9c28baf7b" />



Maior Valor de uma Série até -1 — Little Man Computer (LMC)

O programa encontra o maior valor de uma série de números digitados pelo usuário. A entrada continua até que o usuário digite -1, que funciona como o valor de parada.

O primeiro número digitado é utilizado como valor inicial de maior. Depois, cada novo número é comparado com o valor armazenado. Se o novo número for maior, ele passa a ser o novo valor de maior.

 Exemplo

Se o usuário digitar:

5 → 12 → 8 → 20 → 7 → -1

O resultado será:

20

O -1 não é considerado na comparação, pois serve apenas para indicar o final da série.

Fluxograma

O fluxograma representa visualmente o funcionamento do programa: início → entrada do primeiro número → armazenar como maior → entrada de outro número → verificar se é -1 → comparar com o maior → atualizar o maior se necessário → repetir → exibir o maior → fim.

| Execução | Números digitados       | Maior valor |
| -------- | ----------------------- | ----------: |
| 1        | 5, 12, 8, 20, 7         |      **20** |
| 2        | 15, 4, 28, 10, 21       |      **28** |
| 3        | 3, 18, 7, 25, 12, 30, 6 |      **30** |
