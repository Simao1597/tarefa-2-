<img width="2120" height="8191" alt="Encontrar o menor valor de uma série terminada em -1" src="https://github.com/user-attachments/assets/29ba713f-4c35-4042-b677-b294fd346561" />




Menor Valor de uma Série até -1 — Little Man Computer (LMC)


O programa encontra o menor valor de uma série de números digitados pelo usuário. A entrada continua até que o usuário digite -1, que funciona como o valor de parada.

O primeiro número digitado é utilizado como valor inicial de menor. Depois, cada novo número é comparado com o valor armazenado. Se o novo número for menor, ele passa a ser o novo valor de menor.

 Exemplo

Se o usuário digitar:

8 → 5 → 12 → 3 → 7 → -1

O resultado será:

3

O -1 não participa da comparação, pois serve apenas para indicar o final da série.

Fluxograma

O fluxograma representa visualmente o funcionamento do programa: início → entrada do primeiro número → armazenar como menor → entrada de outro número → verificar se é -1 → comparar com o menor → atualizar o menor se necessário → repetir → exibir o menor → fim.

| Execução | Números digitados           | Menor valor |
| -------- | --------------------------- | ----------: |
| 1        | 8, 5, 12, 3, 7              |       **3** |
| 2        | 15, 4, 28, 10, 2, 21        |       **2** |
| 3        | 20, 18, 7, 25, 12, 3, 30, 6 |       **3** |
